# Especificación para dibujar los C4 (a mano, en draw.io)

Esta especificación es para que **ustedes** dibujen los diagramas en
[app.diagrams.net](https://app.diagrams.net). No se genera con un script: la devolución de
FORM-AC-01 fue clara en que un diagrama producido por código no demuestra comprensión.

Tiempo estimado: 25 minutos el nivel 1 y 30 minutos el nivel 2.

## Reglas generales

- Un solo archivo por nivel: `docs/diagramas/c4-n1-contexto.drawio` y `c4-n2-contenedores.drawio`.
- Exportar PNG a 300 dpi en `docs/figuras/` con el mismo nombre base.
- Cada caja lleva **nombre + identificador entre paréntesis** (`Servicio de incidencias (SVC-INC)`).
- Cada flecha lleva etiqueta con el mecanismo: `REST/JSON · sincrónica` o `AMQP · asincrónica`.
- Los sistemas externos van fuera del recuadro punteado del sistema.
- Guardar el `.drawio` (editable), no solo el PNG.

## Nivel 1 — contexto

Personas (rectángulos redondeados, a la izquierda y a la derecha):

| Elemento | Etiqueta |
|---|---|
| Persona 1 | Agente de mesa de ayuda |
| Persona 2 | Técnico de campo |
| Persona 3 | Cliente del proveedor |

Sistema (un rectángulo grande al centro, con borde grueso):

| Elemento | Etiqueta |
|---|---|
| Sistema | SGIRI Distribuido — gestión de incidencias técnicas |

Sistemas externos (rectángulos grises, alrededor):

| Elemento | Etiqueta |
|---|---|
| Externo 1 | Servicio de correo (notificaciones) |
| Externo 2 | Almacenamiento de archivos (adjuntos) |
| Externo 3 | Red del proveedor (origen de la falla) |

Flechas (5): las tres personas apuntan al sistema; el sistema apunta a correo y a almacenamiento;
el externo 3 apunta al sistema con la etiqueta `eventos de red`.

Sin números de versión, sin protocolos en este nivel: el nivel 1 es de personas y sistemas.

## Nivel 2 — contenedores

Recuadro punteado grande con el nombre del sistema. Dentro, de izquierda a derecha:

| # | Contenedor | Identificador | Qué poner dentro de la caja |
|---|---|---|---|
| 1 | API Gateway | `GW-01` | Autenticación, límites de tasa, punto de entrada |
| 2 | Servicio de incidencias | `SVC-INC` | Alta, estado, asignación |
| 3 | Servicio de técnicos | `SVC-TEC` | Catálogo y disponibilidad |
| 4 | Servicio de notificaciones | `SVC-NOT` | Avisos al cliente y al técnico |
| 5 | Base de datos de incidencias | `DB-INC` | PostgreSQL (E3) |
| 6 | Base de datos de técnicos | `DB-TEC` | PostgreSQL (E3) |
| 7 | Cola de mensajes | `MQ-01` | RabbitMQ (E2) |
| 8 | Almacenamiento de adjuntos | `ALM-ADJ` | Externo, con Cloudinary como referencia |

Flechas y etiquetas obligatorias:

| Desde | Hacia | Etiqueta |
|---|---|---|
| Agente, Técnico, Cliente | `GW-01` | HTTPS |
| `GW-01` | `SVC-INC` | REST/JSON · sincrónica |
| `GW-01` | `SVC-TEC` | REST/JSON · sincrónica |
| `SVC-INC` | `SVC-TEC` | REST/JSON · sincrónica (consulta de disponibilidad) |
| `SVC-INC` | `MQ-01` | AMQP · asincrónica |
| `MQ-01` | `SVC-NOT` | AMQP · asincrónica |
| `MQ-01` | `ALM-ADJ` | AMQP · asincrónica |
| `SVC-INC` | `DB-INC` | JDBC |
| `SVC-TEC` | `DB-TEC` | JDBC |

**Importante:** las cajas 4 a 7 no existen todavía en `src/`; están planificadas para E2 y E3. En el
diagrama se marcan con borde punteado y una nota al pie: «planificado para E2/E3». Dibujar algo como
si ya existiera es lo que después no se puede sostener en la defensa.

## Cómo se ve que el diagrama es de ustedes

- Los nombres de los técnicos y de las zonas son los del código (`Luis Vera`, `Quevedo centro`).
- Las cajas están alineadas a mano, no perfectamente equidistantes.
- En el video, uno de ustedes señala el diagrama y explica por qué `SVC-INC` consulta a `SVC-TEC` y
  no guarda una copia del técnico: porque el técnico cambia de disponibilidad y una copia quedaría
  desactualizada.
