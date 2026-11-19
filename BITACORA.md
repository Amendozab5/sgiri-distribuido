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
