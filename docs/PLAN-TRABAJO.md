# Plan de trabajo — TA-PFC-E1 (v3.1, 18 de noviembre de 2026, 20:30)

Reemplaza la v2. Cambios: se reconoce que **no hay levantamiento utilizable**, se activa el plan de
recuperación de evidencias y se abre la consulta al docente por el alcance de FORM-AC-01, porque el
equipo de E1 no coincide con el que firmó esa formativa.

## 1. Estado real al 18/11

| # | Situación | Efecto |
|---|---|---|
| B1 | No hay entrevista ni acta. La única conversación fue con un ingeniero de apoyo a la base y sus notas están con un excompañero. | Sin levantamiento, D3 = 0 y los requisitos quedan sin origen |
| B2 | El equipo de E1 no es el que firmó FORM-AC-01 (allí figuran Cedeño, Mendoza, Sánchez y Zambrano Triviño). | El criterio de piso «no entregaron las formativas» puede aplicar al equipo |
| B3 | FORM-TL-02 y FORM-IC-01 todavía no abren. | No se puede cerrar el piso; hay que prepararlas con el trabajo de E1 |
| B4 | No hay mediciones de PE-U1 con cifras propias. | El ADR-002 queda justificado solo cualitativamente |
| B5 | Solo Angello participó en FORM-AC-01; Angel y César no aparecen en esa entrega. | El piso depende de la respuesta del docente |

## 2. Acciones de hoy (miércoles 18)

1. **Correo al docente** (Angel), con tres preguntas concretas: si la FORM-AC-01 entregada por el
   grupo de Cedeño, Sánchez y Zambrano Triviño cubre a este equipo, considerando que solo Angello
   participó; cuándo abren TL-02 e IC-01; y si se puede presentar E1 mientras esas formativas estén
   pendientes. Guardar la respuesta en `evidencias/`.
2. **Lista de contactos** para la entrevista: cinco candidatos (proveedores de internet locales,
   egresados que trabajen en soporte, el ingeniero que apoyó la base de datos). Enviarles el guion.
3. **Publicar el repositorio** desde la cuenta de `@Amendozab5` y agregar a `@iMouraad` y
   `@CesarMacias007` como colaboradores, con el tablero en visibilidad pública.
4. **Confirmar la entrega de FORM-AC-01** en el SGA y guardar la captura en `evidencias/`.

## 3. Recuperación del levantamiento (18 al 22)

| Fecha | Acción | Quién | Terminado cuando |
|---|---|---|---|
| Mié 18 | Contactar a los cinco candidatos y agendar | Angel | Al menos una fecha confirmada |
| Jue 19 | Publicar la encuesta de 12 ítems y distribuirla | César | Enlace activo; primeras respuestas |
| Vie 20 | Entrevista 1 con guion impreso y acta | Los tres | Acta firmada o audio con consentimiento |
| Sáb 21 | Entrevista 2 si aparece; cerrar encuesta con ≥15 respuestas | César / Angel | CSV crudo exportado |
| Dom 22 | Vaciar cifras en la tabla de consecuencias y en la trazabilidad | César | Cada cifra con su cita `[Acta, P#]` o `[Encuesta, ítem #]` |

Detalle en [`levantamiento/README.md`](levantamiento/README.md), con guion, acta y encuesta.

## 4. Semana 5 — 23 al 29 de noviembre

| Fecha | Angel | Angello | César | Cierre del día |
|---|---|---|---|---|
| Lun 23 | C4 nivel 1, ADR-001, documento definitivo | `servicio-tecnicos` en marcha | RF1–RF5 con criterios citando la entrevista | Diagrama 1 versionado |
| Mar 24 | C4 nivel 2 y tabla de interacciones | `servicio-incidencias` y llamada al proveedor | RF6–RF11 y RNF definitivos | Interacción con `X-Correlation-Id` en logs |
| Mié 25 | ADR-002 y justificación distribuida | Manejo de `503`, timeout; capturas 1 y 2 | Trabajos relacionados (3, con DOI) | Esqueleto reproducible desde el README |
| Jue 26 | CAP/PACELC por dato crítico | Captura 3 y robustez | Riesgos definitivos (5, 3 de FORM-AC-01) | Coherencia RF ↔ C4 ↔ ADR ↔ CAP |
| Vie 27 | Documento integrado y compilado | Sección de implementación | Revisión de cifras y de referencias | `main.pdf` compila sin errores |
| Sáb 28 | Video 5–7 min y tabla de aportes | Demo en el video | Referencias verificadas (8, 4 con DOI) | Video enlazado en README |
| Dom 29 | Compilar desde un clon limpio; PDF de una página del SGA | Cerrar issues | Cerrar issues | Todo cerrado antes de 23:55 |

## 5. Reglas de trabajo

1. Una rama por tarea (`feat/…`, `docs/…`), *pull request* a `main`, aunque la apruebe otro
   integrante.
2. Un issue por tarea, con criterio de aceptación, asignado y cerrado al integrar el PR.
3. *Daily* de 15 minutos y entrada en `BITACORA.md` el mismo día.
4. Toda decisión de arquitectura se registra como ADR antes de implementarse.
5. Ningún integrante sube trabajo de otro; cada quien confirma con su cuenta.
6. Antes de cada push: `git pull --rebase`.

## 6. Riesgos del propio plan

| Riesgo | Señal temprana | Plan B |
|---|---|---|
| No hay entrevista al 20 | Sin fecha confirmada el jueves | Encuesta como evidencia principal, con ≥15 respuestas y declaración del motivo |
| El docente dice que FORM-AC-01 no cubre al equipo | Respuesta negativa | Hacer la actividad con el formato de FORM-AC-01 y entregarla antes del 26 |
| TL-02 / IC-01 abren después del 29 | Sin noticias al 24 | Escalar por escrito y guardar la respuesta; dejar E1 listo para subir en horas |
| El esqueleto no arranca en otro equipo | Falla el 25 al probar desde cero | Reducir a un endpoint por servicio y documentar el mínimo verificable |
| Se acumula el documento al final | El 26 no compila `main.pdf` | Congelar contenido el 27; el 28 solo video y referencias |
