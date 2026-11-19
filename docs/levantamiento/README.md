# Levantamiento de información: plan de recuperación (18–22 de noviembre)

Situación de partida, al 18/11/2026: **no hay evidencia de levantamiento utilizable**. La única
conversación registrada fue con un ingeniero que apoyó la base de datos, y sus notas quedaron en
poder de un compañero que ya no está en el equipo.

Eso no es un problema de redacción: sin levantamiento real, la dimensión D3 vale **0** y los
requisitos quedan sin origen verificable. Este documento define cómo se resuelve en cuatro días.

## Lo que NO se puede hacer

- **No se reconstruye el acta de memoria.** Un acta escrita después, sin firma ni grabación, es
  evidencia fabricada y lleva la entrega a cero.
- **No se usa la firma ni el nombre de nadie** sin que esa persona firme o autorice la grabación.
- **No se reciclan los datos del compañero ausente** como si fueran del equipo. Si se recuperan,
  solo valen si traen fecha, nombre y cargo del entrevistado y su firma o consentimiento de
  grabación; y aun así hay que citar quién entrevistó.
- **No se entrevista a un técnico de bases de datos como si fuera usuario del dominio.** Un apoyo
  técnico del proyecto no es responsable de operaciones ni usuario del sistema; sirve como fuente
  secundaria, no como evidencia principal.

## Tres rutas válidas (elegir una principal y, si se puede, sumar la encuesta)

| Ruta | Qué es | Costo | Calidad de evidencia |
|---|---|---|---|
| **A. Entrevista con la organización real** | 45 min con el responsable de operaciones o mesa de ayuda de un proveedor de internet | 1 gestión + 1 hora | La mejor: da cifras, contexto y autorización |
| **B. Entrevista con el ingeniero de apoyo** | Recuperar el contacto y repetir la conversación con acta y firma | 1 llamada | Media: aporta lo técnico, no el proceso de negocio |
| **C. Encuesta a ≥15 usuarios potenciales** | Formulario con resultados crudos adjuntos | 3 días de recolección | Aceptada por el enunciado cuando no hay organización real |

**Recomendación:** A como principal, C como respaldo y complemento (la encuesta da los números que
la entrevista no alcanza a cubrir). B solo si A no se concreta antes del viernes 20.

## Cronograma de recuperación

| Día | Acción | Responsable | Resultado |
|---|---|---|---|
| Mié 18 | Listar 5 contactos posibles (proveedores de internet locales, egresados, técnicos conocidos) y escribirles hoy mismo | Quien tenga la red de contactos | Al menos 2 respuestas |
| Jue 19 | Publicar la encuesta y distribuirla en grupos de soporte técnico, WhatsApp y LinkedIn | César | Enlace activo y primeras respuestas |
| Vie 20 | Entrevista 1 (ruta A o B) con guion y acta impresa | Los tres si es posible | Acta firmada o audio con consentimiento |
| Sáb 21 | Entrevista 2 si aparece; cierre de la encuesta con ≥15 respuestas | César / Angel | Exportación CSV cruda |
| Dom 22 | Vaciar los datos en la tabla de consecuencias del `.tex` y en la tabla de trazabilidad | César | Requisitos con origen |

## Reglas de la evidencia

1. El acta se firma **al final de la entrevista**, no después.
2. Si el entrevistado prefiere no firmar, se graba con consentimiento expreso en el audio y se
   guarda el enlace en `evidencias/acta/`.
3. Se pide autorización para citar la organización; si no la da, se usa un seudónimo y se declara.
4. Cada cifra usada en el documento lleva su origen: `[Acta, P7]` o `[Encuesta, ítem 4, n=17]`.
5. Las respuestas crudas de la encuesta se versionan tal como salen de la plataforma; no se
   «limpian» ni se resumen antes de guardarlas.

## Archivos

- [`guion-entrevista.md`](guion-entrevista.md) — 14 preguntas con el dato que produce cada una.
- [`acta-plantilla.md`](acta-plantilla.md) — formato para imprimir y firmar.
- [`encuesta.md`](encuesta.md) — instrumento de 12 ítems y plan de recolección.
