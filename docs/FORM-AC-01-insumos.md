# Insumos de FORM-AC-01 (incidente Fastly, 8 de junio de 2021) para TA-PFC-E1

Documento de trabajo. No es entregable por sí mismo: alimenta las secciones **Riesgos**,
**Justificación de la arquitectura** y **Requisitos no funcionales** del documento de E1.

- Actividad: **FORM-AC-01**, análisis de caso de fallo real.
- Repositorio: <https://github.com/jcedenoi4/FORM-AC-01>
- Sección de la que se extrae: `informe/secciones/02_causas.tex`
  («Tres riesgos de SGIRI vinculados a estas causas»), elaborada por Angello Mendoza.
- Estado: entregada antes de E1; debe conservarse la constancia de la entrega en el SGA.

## 1. Hechos verificados del incidente

Fuente primaria: informe oficial de Fastly (Nick Rockwell, 8 de junio de 2021).

| Dato | Valor | Uso en E1 |
|---|---|---|
| Cambio desencadenante | Un cliente modificó su configuración y activó un defecto introducido el 12 de mayo (27 días latente) | Argumento de «configuración válida que activa un defecto latente» |
| Alcance | 85 % de la red devolvió errores | Magnitud del fallo: un cambio pequeño, alcance global |
| Recuperación | 95 % de la red operativa en 49 minutos | Línea base para el RTO y el objetivo de disponibilidad |
| Detección | Aviso de estado a los 11 minutos del inicio (09:47 → 09:58 UTC) | La detección no fue el problema: la **identificación** sí |
| Identificación | 09:47 → 10:27 UTC: **40 minutos** para hallar la configuración culpable | Justifica observabilidad y trazabilidad de cambios |
| Mitigación | 12:35 UTC; corrección permanente desde las 17:25 UTC | Distinguir mitigar de corregir |

## 2. Los tres riesgos ya redactados para SGIRI

Estos tres riesgos fueron escritos en FORM-AC-01 aplicados a **SGIRI**, que es el PFC de este
equipo. Cumplen el requisito de E1 de «al menos 3 riesgos derivados de las lecciones del incidente
analizado en FORM-AC-01» y se incorporan al documento con esta referencia.

| ID | Riesgo (categoría del diagrama de Ishikawa) | Consecuencia | Medida verificable en E1 |
|---|---|---|---|
| **R-01** | Un cambio válido en las reglas que mueven el ticket entre estados (nuevo → asignado → en proceso → resuelto → cerrado) deja el ticket sin salida y con el reloj del SLA corriendo. *(personas y procesos)* | Tickets atrapados; SLA vencido sin que nadie lo note; reclamos | Validar la máquina de estados y rechazar transiciones no permitidas con `409`; probar todas las transiciones y verificar que el estado y el contador del SLA no cambian ante una transición inválida |
| **R-02** | Una versión nueva del backend con una credencial o una URL de base de datos mal puesta no arranca y, al ser una sola instancia, el sistema completo queda caído. *(tecnología)* | Indisponibilidad total; pérdida de solicitudes en curso | Dos instancias detrás de un *proxy* con verificación de salud antes de recibir tráfico; conservar el artefacto anterior para revertir; comprobar el arranque en un entorno de prueba antes de publicar |
| **R-03** | El alta de una incidencia depende de un servicio externo (Cloudinary) para los adjuntos; si falla o tarda, el alta termina en error 500 y el ticket no se registra. *(entorno)* | Cliente sin ticket; trabajo perdido; reintentos manuales | Separar el alta del adjunto: registrar el ticket primero y subir después, con tiempo límite y reintento; comprobar con el servicio externo bloqueado que el ticket **sí** se registra |

## 3. Qué se hace con esto en E1 (cinco acciones)

1. **Riesgos (César).** Llevar R-01, R-02 y R-03 a la tabla de riesgos del documento como los tres
   primeros, con probabilidad, impacto y la columna «deriva de FORM-AC-01». Agregar dos riesgos
   propios del proyecto (por ejemplo, coherencia de datos entre servicios y dependencia de la red
   del local del cliente) para llegar a cinco.
2. **Requisitos (César).** Cada medida verificable se convierte en un requisito con cifra:
   - R-02 → RNF de disponibilidad (99,5 % mensual; RTO 30 min) y RNF de mantenibilidad
     (despliegue sin detener el servicio).
   - R-03 → RNF de tolerancia a fallos / degradación (el alta responde en < 2 s incluso con el
     servicio de adjuntos caído; el ticket se registra igual).
   - R-01 → RF de máquina de estados con criterio de aceptación explícito (transición inválida →
     `409` y estado intacto).
3. **Justificación (Angel).** Usar el incidente como argumento de por qué no basta un monolito en
   una sola instancia: en Fastly un solo cambio afectó al 85 % de la red; en SGIRI una sola
   instancia significa el 100 % del servicio caído (R-02), y una sola base significa un único
   punto de fallo. Enlazar con Gilbert y Lynch y con Abadi para el CAP y el PACELC.
4. **ADR-002 (Angel).** R-03 es la razón concreta para que el mecanismo principal no sea solo
   síncrono: la subida de adjuntos y las notificaciones van por mensajería asíncrona, mientras las
   consultas van por REST. Esto conecta el ADR con un riesgo real, no con una preferencia.
5. **Esqueleto (Angello).** Implementar al menos **una** de las tres mitigaciones y demostrarla en
   las capturas: la más barata es la de R-02/R-03 — `timeout` de 2 s, `503` con mensaje claro
   cuando el proveedor está caído y `X-Correlation-Id` en ambos logs. Con eso el documento puede
   afirmar «medida comprobada», no «medida propuesta».

## 4. Lo que FORM-AC-01 todavía no aporta

- No hay sección de lecciones específica para SGIRI fuera de `02_causas.tex`: los otros tres
  bloques de lecciones corresponden a otro PFC (Pre-Sustentaciones). **No se pueden mezclar.**
- Las pruebas descritas son propuestas, no ejecutadas. E1 debe ejecutar al menos una y decirlo.
- Las referencias de FORM-AC-01 (2012–2016) son clásicas y válidas, pero **no cuentan** para el
  requisito de E1 de 8 referencias de los últimos cinco años con 4 artículos indexados con DOI:
  hay que buscar esas por separado.

## 5. Advertencia de alcance del equipo

FORM-AC-01 está firmada por Cedeño, Mendoza, Sánchez y Zambrano Triviño; el equipo de este PFC es
Zambrano Yong, Mendoza y Macías. Solo Angello coincide. Antes de presentar hay que confirmar con el
docente si la formativa entregada por ese grupo cubre a este equipo; si no, hay que resolverlo con
él **antes del 29 de noviembre**, porque es un criterio de piso.
