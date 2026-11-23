# Entrega express: de 20:40 a 23:59

El cierre es hoy. No se puede hacer E1 completo, así que se hace **el mínimo que se sostiene en pie
y que el equipo puede explicar**. Lo que no se alcanza se declara como alcance de E2/E3/E4, no se
finge.

## 1. Decisión de alcance

| Sí entra | No entra |
|---|---|
| Esqueleto de dos servicios que se comunican por REST y degradan a `503` | Base de datos, contenedores, API Gateway |
| Los dos diagramas C4 dibujados a mano en draw.io | Versión "bonita" con iconos y sombras |
| 10 RF y 6 RNF con cifra, con la cita del acta | Trazabilidad exhaustiva de las 11 historias |
| Justificación distribuida ligada a RNF-01 y RNF-02 | Estudio comparativo de cinco sistemas |
| CAP/PACELC de tres datos críticos | Análisis de los seis |
| 3 riesgos de FORM-AC-01 + 2 propios | Riesgos con simulación o prueba de caos |
| Acta de una entrevista real de 30 minutos | Encuesta a 15 personas (no da el tiempo) |

## 2. Reloj

| Hora | Quién | Qué |
|---|---|---|
| 20:40–21:00 | César | **Llamada real** a un contacto del dominio, con grabación y consentimiento. Es la acción de mayor valor de la noche |
| 20:40–21:10 | Angel | Dibujar C4 nivel 1 en draw.io según `docs/diagramas/ESPECIFICACION-C4.md`; exportar PNG |
| 20:40–21:10 | Angello | Arrancar los dos servicios, probar los tres casos y tomar las 3 capturas con usuario, máquina, fecha y hora |
| 21:10–21:45 | Angel | Dibujar C4 nivel 2; exportar PNG; reemplazar los recuadros del `.tex` |
| 21:00–21:50 | César | Vaciar las cifras de la llamada en la tabla de consecuencias, RNF y trazabilidad; quitar todos los `[PENDIENTE]` |
| 21:50–22:20 | Angel | Compilar, revisar coherencia RF ↔ C4 ↔ ADR ↔ CAP, corregir portada (asignatura y facultad) |
| 22:20–23:05 | Los tres | Grabar el video con el guion de la sección 4 |
| 23:05–23:20 | Angello | Subir el video, pegar el enlace en el README, compilar `docs/sga.tex` |
| 23:20–23:40 | Cada uno | **Commits propios**, en su cuenta, de sus archivos; cerrar sus issues |
| 23:40–23:55 | Angel | Clonar en otra carpeta, compilar, verificar el PDF del SGA y subirlo |

Si la llamada de las 20:40 no se concreta, no se inventa nada: se escribe en el documento que el
levantamiento quedó pendiente y por qué. Es peor un acta falsa que un requisito sin cita.

## 3. Reglas para no repetir la devolución de FORM-AC-01

1. **El diagrama lo dibujan ustedes** en app.diagrams.net. Nada de generar el `.drawio` con un
   script ni de pegar un SVG hecho por un asistente. La devolución fue explícita: un script no
   demuestra que entienden las causas.
2. **Un commit por etapa y por persona**, con mensajes en español escritos por ustedes. Sin
   prefijos `feat:`, `docs:`, `build:` ni ráfagas de tres archivos por minuto al final.
3. **Estilo IEEE**: ya está configurado (`biblatex` con `style=ieee`). No cambiar a `plain`.
4. **Compila desde un clon limpio**: nombres de archivo exactos y rutas relativas. El error de
   `seccion_leonel.tex` contra `secion_leonel.tex` costó un criterio entero.
5. **Portada correcta**: la asignatura es *Aplicaciones Distribuidas*, la facultad hay que
   escribirla bien. Hoy el `.tex` tiene `[PENDIENTE: facultad y carrera]` y
   `[PENDIENTE: periodo]`.
6. **Extensión razonable**: 12 a 16 páginas está bien. No inflar para parecer completo.
7. **Declaración de IA verdadera y específica**: qué herramienta, para qué se usó y cómo se
   verificó. Si el texto lo escribió un asistente, en la defensa oral se nota.

## 4. Guion del video (5 a 7 minutos)

| Min | Quién | Qué dice y qué muestra |
|---|---|---|
| 0:00–0:30 | Angello | Presentación: equipo, proyecto, entrega |
| 0:30–1:30 | Angel | Problema real, cómo se atiende hoy, y los dos requisitos que obligan a distribuir (RNF-01 y RNF-02) |
| 1:30–2:30 | César | Requisitos y los tres riesgos heredados de FORM-AC-01, con su mitigación |
| 2:30–4:30 | Angello | **Demo en vivo**: arranca los dos servicios, `curl` al 8081, `curl` al 8082 con datos combinados, apaga el 8081, repite y muestra el `503`; enseña los logs con el mismo `X-Correlation-Id` |
| 4:30–5:30 | Angel | Diagrama C4 de contenedores y una decisión de CAP: por qué el estado del ticket es CP |
| 5:30–6:30 | César | Qué queda para E2 y E3, y cierre |

Toda la demo con el `prompt` visible: usuario, máquina y fecha deben coincidir con las capturas.

## 5. Checklist de las 23:30

- [ ] `docs/main.pdf` compila desde un clon limpio y no queda ningún `[PENDIENTE]`
- [ ] Los dos PNG del C4 están en `docs/figuras/` y se ven en el PDF
- [ ] Las 3 capturas están en `evidencias/capturas/` con usuario, máquina y fecha
- [ ] El acta está en `evidencias/acta/` (firmada o con consentimiento de grabación)
- [ ] El enlace del video está en el `README.md` y abre sin iniciar sesión
- [ ] `docs/sga.pdf` tiene **una sola página** y la URL completa en una línea
- [ ] Cada integrante tiene al menos un commit propio de hoy y sus issues asignados
- [ ] El tablero de Projects es público
