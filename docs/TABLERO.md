# Tablero de trabajo

Lista de issues para crear en GitHub Projects. Cada issue se crea con la plantilla
«Tarea de entrega», se asigna a un integrante, se agrega al proyecto y se cierra al integrar su
pull request.

## Configuración del proyecto

1. Repositorio → **Projects** → **New project** → plantilla *Board*.
2. Nombre: `PFC SGIRI — E1 a E4`. Visibilidad: **pública**.
3. Columnas: `Backlog`, `En curso`, `En revisión`, `Hecho`.
4. Milestones en el repositorio: `E1 — 29/11/2026`, `E2 — semana 9`, `E3 — semana 13`,
   `E4 — semana 17`.

## Issues de E1

| # | Título | Responsable | Criterio de aceptación |
|---|---|---|---|
| 1 | Estructura del repositorio, README y bitácora | Angel | Un tercero entiende el proyecto y compila el PDF siguiendo el README |
| 2 | Diagrama C4 nivel 1 (contexto) | Angel | `.drawio` versionado en `docs/diagramas/` y PNG exportado |
| 3 | Diagrama C4 nivel 2 (contenedores) | Angel | Servicios, bases y flechas con mecanismo; coincide con la tabla de comunicación |
| 4 | ADR-001 estilo de arquitectura | Angel | Contexto, opciones, decisión y consecuencias; enlazado desde el `.tex` |
| 5 | ADR-002 mecanismo de comunicación | Angel | Incluye la tabla de mediciones de PE-U1 |
| 6 | Justificación distribuida y CAP/PACELC | Angel | Cada afirmación se apoya en un RNF y en un dato crítico |
| 7 | Historias de usuario RF-01 a RF-11 | César | Cada una con ≥2 criterios y su cita del acta |
| 8 | Requisitos no funcionales con ISO/IEC 25010 | César | 7 RNF con cifra y método de verificación |
| 9 | Análisis de riesgos (5) | César | 3 derivados de FORM-AC-01, con mitigación verificable |
| 10 | Trabajos relacionados (3) con DOI | César | DOI verificado en doi.org y datos coincidentes con Crossref |
| 11 | Servicio `servicio-tecnicos` | Angello | `GET /api/tecnicos` y `/actuator/health` responden |
| 12 | Servicio `servicio-incidencias` con llamada al proveedor | Angello | `GET /api/incidencias/{id}` devuelve el técnico resuelto |
| 13 | Degradación controlada y `X-Correlation-Id` | Angello | Con el proveedor apagado responde `503`, no `500` |
| 14 | Instrucciones de ejecución y 3 capturas | Angello | Usuario, máquina, fecha y hora visibles en cada captura |
| 15 | Documento integrado y PDF | Angel | Compila desde un clon limpio |
| 16 | Video de 5 a 7 minutos | Los tres | Cada rol explicado y esqueleto en ejecución |
| 17 | PDF de una página para el SGA | Angel | URL completa en una sola línea, sin cortes |

## Issues de E2 (se crean ahora, se ejecutan en la semana 9)

| # | Título | Responsable |
|---|---|---|
| 18 | API Gateway y enrutamiento | Angello |
| 19 | Contratos OpenAPI versionados | César |
| 20 | Contenedores con Docker Compose | Angello |
| 21 | Servicio de notificaciones con mensajería | Angello |
| 22 | Pruebas de humo del despliegue en contenedores | Angel |

## Regla

Un issue sin criterio de aceptación no se crea: si no se puede comprobar que está hecho, no es una
tarea, es una intención.
