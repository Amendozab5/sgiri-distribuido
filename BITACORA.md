# Bitácora del equipo

Registro de las sesiones de trabajo del PFC **SGIRI Distribuido**.
Cada entrada se escribe **el mismo día** de la sesión, no al final de la semana.

## Reglas

- Una entrada por sesión, con fecha, integrantes presentes y decisiones tomadas.
- Las decisiones de arquitectura se registran además como ADR en `docs/adr/`.
- Los problemas resueltos se escriben con la solución aplicada, para que sirvan de evidencia en
  la defensa oral.
- No se registran sesiones que no ocurrieron ni se completan asistencias a posteriori.

## Registro

| # | Fecha | Tipo de sesión | Integrantes presentes | Decisiones tomadas | Problemas resueltos | Evidencia |
|---|---|---|---|---|---|---|
| 1 | 2026-11-18 | Arranque / preparación | *(completar en la reunión de arranque)* | Se adopta la **opción B**: repositorio nuevo y público, con reutilización selectiva del proyecto SGIRI (Aplicaciones Web) debidamente atribuida. Se descarta clonar el repositorio anterior para no arrastrar 98 commits de otro periodo ni autores ajenos al equipo. | Se identificó que el repositorio SGIRI no es la base adecuada: es un monolito y su historial no corresponde a este PFC. Se definió la estructura mínima exigida por el enunciado. | `docs/ATRIBUCION.md`, `README.md` |
| 2 | 2026-11-18 | Revisión del estado de evidencias | | Se documenta que **no existe levantamiento utilizable**: la única conversación fue con un ingeniero de apoyo a la base de datos y sus notas quedaron con un compañero que ya no está en el equipo. Se descarta reconstruir el acta y se activa el plan de recuperación de `docs/levantamiento/`. | Se acordó no usar datos de terceros sin acta firmada ni grabación con consentimiento. | `docs/levantamiento/README.md` |
| 3 | 2026-11-18 | Definición de integrantes y del repositorio | Angello | Se confirma el equipo (Macías, Mendoza, Zambrano) con sus usuarios de GitHub; el repositorio se publica en la cuenta de Amendozab5 con los otros dos como colaboradores. Se aclara que solo Angello participó en FORM-AC-01. | Se resolvió la confusión sobre la composición del equipo: MMZ es este equipo; el grupo de FORM-AC-01 era otro. | `README.md`, `docs/ATRIBUCION.md` |
| 4 | 2026-11-18 | Trabajo individual (Angel) | Angel | Se suben los insumos del caso X de FORM-AC-01 y el diagrama C4 nivel 1 con cuatro personas (cliente, agente, técnico, administrador) y tres sistemas externos (SMTP, Cloudinary, Globalping), integrado por PR #1. | Se decidió dejar el `.drawio` versionado junto al PNG para que el diagrama se pueda editar. | Commits `6f8f891`, `5e2a7c6`; PR #1 |
| 5 | 2026-11-22 | Trabajo individual (Angel) | Angel | Se agrega el C4 nivel 2 con los servicios del ADR-001 y los mecanismos de la tabla de comunicación (REST con timeout de 2 s y 503; AMQP para avisos y adjuntos); los elementos de E2 van punteados. Se completa el ADR-002 con las mediciones de PE-U1 (medianas de 0,05 a 0,15 ms con sockets y de 0,34 a 0,58 ms con gRPC en loopback) y se mantiene REST para E1. Se agrega al ADR-001 el riesgo de exposición del caso X. | La primera exportación del C4 nivel 2 salió con fondo negro por el modo oscuro de draw.io; se volvió a subir con fondo blanco. Se detectó que el ADR-002 y la discusión de PE-U1 podían contradecirse sobre gRPC y se aclaró en el ADR que la diferencia de latencia es menor a 1 ms. | Commits `1862973`, `d291577`, `79993a0`, `3458e05` |
| 6 | 2026-11-22 | Trabajo individual (César) | César | Se redactan los criterios de aceptación (Dado/Cuando/Entonces) y citas de origen para historias de usuario RF-01 a RF-11; se restauran y cuantifican los 7 RNF con ISO/IEC 25010 y sus métodos de verificación; se definen los riesgos R-04 (consistencia distribuida) y R-05 (conectividad móvil en campo) con mitigaciones; se incorporan 3 artículos de revista indexados con DOI posterior a 2021 en la tabla comparativa de trabajos relacionados y referencias.bib. | Se subsanaron todos los campos marcados como pendientes en la revisión de entrega, garantizando trazabilidad con el guion de entrevista y FORM-AC-01. | Commit `95b1375`; `docs/secciones/03-requisitos.tex`, `docs/secciones/04-arquitectura.tex`, `docs/secciones/02-relacionados.tex`, `docs/referencias.bib` |

## Sesiones previstas (no registradas todavía)

| Fecha prevista | Tipo | Objetivo |
|---|---|---|
| 2026-11-20 | Entrevista | Levantamiento con acta firmada (ruta A o B) |
| 2026-11-21 | Sesión de diseño 1 | Primer bosquejo de arquitectura, foto grupal con fecha |
| 2026-11-23 | Revisión de coherencia | Requisitos, C4, ADR y CAP alineados |

## Plantilla de entrada

```markdown
| N | AAAA-MM-DD | Sesión de diseño / desarrollo / revisión | Nombres | Decisiones (con enlace al ADR si aplica) | Problema → causa → solución | Ruta de la foto o del acta |
```
