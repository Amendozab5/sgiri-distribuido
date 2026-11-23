# ADR-001 — Estilo de arquitectura del sistema

- **Estado:** propuesto (a ratificar en la sesión de diseño del 21/11/2026)
- **Fecha:** 2026-11-18
- **Decisores:** Zambrano Yong Angel (Arquitecto), Mendoza Bermello Angello (Líder de Desarrollo), Macías Vásquez César (Calidad)
- **Contexto del PFC:** SGIRI Distribuido — gestión de incidencias técnicas de un proveedor de internet

## Contexto

SGIRI atiende a tres poblaciones que usan el sistema en momentos y lugares distintos: clientes que
reportan una falla, agentes de mesa de ayuda que clasifican y asignan, y técnicos de campo que
actualizan el estado desde el celular. El servicio se usa de lunes a domingo, con picos después de
cortes de red, y el SLA se mide en horas.

Los requisitos no funcionales que presionan la decisión son:

- **RNF-01 (Disponibilidad):** 99,5 % mensual, con un máximo de 3,6 h de indisponibilidad al mes.
- **RNF-02 (Escalabilidad):** sostener 50 usuarios concurrentes en la línea base y 200 en el pico
  posterior a un corte, sin degradar el tiempo de respuesta.
- **RNF-03 (Mantenibilidad):** desplegar un cambio en el módulo de notificaciones sin detener el
  registro de incidencias.
- **RNF-04 (Eficiencia de desempeño):** 95 % de las consultas de disponibilidad de técnicos en
  menos de 300 ms con 50 usuarios simultáneos.

A esto se suma el riesgo **R-02** heredado de FORM-AC-01: el sistema anterior corre en una sola
instancia; una credencial mal configurada en un despliegue deja el servicio completo caído. En
Fastly, un solo cambio de configuración afectó al 85 % de la red.

También pesa el riesgo de exposición del caso X, analizado en FORM-AC-01. El 10 de marzo de 2025,
la red social X sufrió varias caídas y miles de usuarios no podían entrar a sus cuentas, cargar el
feed ni publicar. Downdetector registró más de 40 000 reportes. Elon Musk lo atribuyó a un "ataque
cibernético masivo", y varios analistas lo identificaron como un ataque DDoS. Lo que más sirve de
este caso es cómo entraron. Según los investigadores, algunos servidores de origen de X no estaban
detrás de la protección DDoS de Cloudflare, así que estaban visibles y se podían atacar
directamente. Ciaran Martin, exdirector del Centro Nacional de Ciberseguridad del Reino Unido, lo
explicó así: X dejó algunos de sus servidores delante de la protección de Cloudflare y no detrás.
Para el SGIRI, que hoy es un solo backend en Spring Boot, la lección es que separar en servicios
aumenta las puertas de entrada. Si dividimos incidencias, técnicos, notificaciones e identidad, solo
el API Gateway debería quedar expuesto, con límite de peticiones por ruta. Los demás servicios
deberían quedar en una red interna y no se debería poder llegar a ellos por su IP. Así, si alguien
satura el portal de clientes, los técnicos pueden seguir atendiendo incidencias.

Fuentes: [Reuters, 10/03/2025](https://www.brecorder.com/news/amp/40352214);
[AP, 10/03/2025](https://bronx.news12.com/elon-musk-claims-x-being-targeted-in-massive-cyberattack-as-service-goes-down);
[Field Effect](https://fieldeffect.com/blog/x-massive-ddos-attack).

## Opciones consideradas

| # | Opción | A favor | En contra |
|---|---|---|---|
| A | Monolito único en un servidor | Simple de desarrollar y desplegar; una sola base | Un fallo detiene todo (R-02); no cumple RNF-01 ni RNF-03; el pico obliga a sobredimensionar |
| B | Monolito modular con réplicas y balanceador | Mejora la disponibilidad sin rediseñar el dominio | El despliegue sigue siendo conjunto; el acoplamiento impide escalar solo la asignación; el pico castiga módulos que no lo necesitan |
| C | **Microservicios por dominio con API Gateway** | Despliegue y escalado independientes; aislamiento de fallos; cumple RNF-01 a RNF-04 | Complejidad operativa; consistencia eventual; exige observabilidad y contratos versionados |
| D | Funciones serverless | Escalado automático y costo por uso | Arranque en frío incompatible con RNF-04; difícil de demostrar y de operar en el periodo académico |

## Decisión

Se adopta la **opción C**: microservicios organizados por dominio funcional, con un API Gateway
como punto de entrada único y sin orquestación compleja (sin service mesh, sin coreografía de
sagas en E1).

Servicios previstos para el periodo:

| Servicio | Responsabilidad | Entrega en que se construye |
|---|---|---|
| `servicio-tecnicos` | Catálogo, disponibilidad y carga de trabajo de los técnicos | E1 (esqueleto) |
| `servicio-incidencias` | Alta, estado y asignación de la incidencia | E1 (esqueleto) / E2 |
| `servicio-notificaciones` | Avisos al cliente y al técnico | E2 |
| `servicio-identidad` | Autenticación y roles | E2 |
| API Gateway | Enrutamiento, límites de tasa, punto único de entrada | E2 |

## Consecuencias

**Positivas**

- Un fallo en notificaciones no impide registrar una incidencia (mitiga R-03 y RNF-03).
- El servicio de incidencias escala solo en el pico posterior a un corte (RNF-02).
- Cumplir RNF-01 exige réplicas por servicio, que es justamente lo que el monolito no permite sin
  duplicar todo el sistema.

**Negativas y cómo se asumen**

- **Complejidad operativa:** se compensa con Docker Compose en E2 y con un máximo de cinco
  servicios; no se agrega infraestructura que el equipo no pueda explicar.
- **Consistencia eventual:** se acepta solo donde el negocio lo tolera (notificaciones, métricas).
  Los datos críticos —estado del ticket y asignación— se tratan como consistentes (ver CAP/PACELC
  en el documento).
- **Depuración distribuida:** se mitiga con `X-Correlation-Id` desde E1, obligatorio en todos los
  servicios.

**Qué invalidaría esta decisión**

Si el equipo no logra levantar dos servicios que se comuniquen antes del 25/11, se degrada a la
opción B y se documenta el cambio en este mismo ADR, sin borrar el registro.
