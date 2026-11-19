# ADR-002 — Mecanismo de comunicación entre servicios

- **Estado:** propuesto (a ratificar en la sesión de diseño del 21/11/2026)
- **Fecha:** 2026-11-18
- **Decisores:** Zambrano Yong Angel (Arquitecto), Mendoza Bermello Angello (Líder de Desarrollo), Macías Vásquez César (Calidad)
- **Relacionado con:** ADR-001, riesgos R-02 y R-03 de FORM-AC-01

## Contexto

Con la arquitectura de microservicios definida en ADR-001 hay que decidir cómo se hablan los
servicios. Las interacciones del diagrama de contenedores son de dos naturalezas:

1. **Consultas que el usuario está esperando:** disponibilidad de un técnico al asignar, estado de
   una incidencia al abrir el detalle. Si no responden, la pantalla queda vacía.
2. **Efectos secundarios que no deben bloquear:** notificar al cliente, subir un adjunto a
   Cloudinary, registrar la métrica del SLA. Si fallan, el ticket ya está registrado.

El riesgo **R-03** de FORM-AC-01 muestra qué pasa cuando se confunde una cosa con la otra: el alta
de la incidencia dependía de la subida del adjunto y terminaba en error 500.

## Opciones consideradas

| # | Mecanismo | A favor | En contra | Medición de PE-U1 |
|---|---|---|---|---|
| A | **REST/JSON síncrono** | Simple, depurable con `curl`, contrato OpenAPI, sin infraestructura extra | Acoplamiento temporal; hay que poner timeouts explícitos | *(completar con la cifra medida)* |
| B | gRPC | Contrato binario, menor latencia, *streaming* | Requiere `protoc` y generación de código; difícil de mostrar en capturas; sobredimensionado para E1 | *(completar)* |
| C | Mensajería asíncrona (RabbitMQ) | Desacopla, absorbe picos, reintentos y cola de fallos | Requiere un *broker*; consistencia eventual; más difícil de explicar | *(completar)* |
| D | GraphQL | Una sola llamada para varias consultas | Complejidad de esquema y de autorización; no aporta en E1 | no medida |

## Decisión

Se adopta un **modelo híbrido**, con un mecanismo principal y uno secundario acotado:

- **Principal — REST/JSON síncrono** para las consultas cuyo resultado el usuario está esperando
  (`GET /api/tecnicos/{id}`, `GET /api/incidencias/{id}`). Contrato documentado con OpenAPI 3.1 y
  versionado en `/docs/api/`.
- **Secundario — mensajería asíncrona** (RabbitMQ) para notificaciones y subida de adjuntos a
  partir de E2. En E1 se deja el punto de extensión documentado, sin implementar el *broker*.

Reglas obligatorias de la comunicación síncrona:

| Regla | Valor | Motivo |
|---|---|---|
| *Timeout* de conexión y de lectura | 2 s | Evitar que un servicio lento arrastre al otro (R-02) |
| Reintentos | 2, con espera exponencial | Cubrir fallos transitorios sin amplificar la carga |
| Idempotencia | `Idempotency-Key` en todo `POST` | Un reintento no debe duplicar un ticket |
| Trazabilidad | `X-Correlation-Id` propagado | Permite reconstruir una transacción entre logs |
| Respuesta ante caída del proveedor | `503` con mensaje de dominio | El consumidor degrada, no revienta con 500 (R-03) |

## Consecuencias

**Positivas**

- El equipo puede demostrar la comunicación en E1 con dos comandos y sin infraestructura extra.
- Las consultas críticas mantienen latencia baja y comportamiento predecible.
- El camino asíncrono queda justificado por un riesgo real, no por preferencia técnica.

**Negativas y cómo se asumen**

- **Acoplamiento temporal en las consultas:** se mitiga con *timeout*, reintentos y `503`
  controlado; en E2 se agrega *circuit breaker* en el Gateway.
- **Dos mecanismos que mantener:** se acota a un solo *broker* y a dos tipos de evento
  (`ticket.creado`, `adjunto.solicitado`); no se adopta coreografía de sagas.
- **Consistencia eventual en notificaciones:** aceptable para el negocio; se documenta en el
  análisis PACELC como `PA/EL`.

**Pendiente antes de ratificar**

Completar la columna de PE-U1 con las mediciones del equipo (latencia p50/p95 y throughput de REST
frente a gRPC o mensajería en el equipo de trabajo). Si no hay medición propia, se hace un
*benchmark* de dos horas el 22/11 y se anexa la tabla; sin cifras, este ADR queda como decisión
justificada solo cualitativamente y pierde peso en D2.
