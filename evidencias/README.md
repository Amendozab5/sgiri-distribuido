# Evidencias de autoría

Todo lo que se guarda aquí debe ser **real y fechado**. Manipular un acta, una foto, una captura o
los resultados de una encuesta se trata como evidencia fabricada y lleva la calificación de la
entrega a cero. Si algo no se pudo hacer, se documenta el motivo; no se simula.

## Organización

```
evidencias/
  acta/       acta firmada de la entrevista, o consentimiento y enlace de la grabación,
              y los resultados crudos de la encuesta si se usó ese camino
  fotos/      fotografías de las sesiones de diseño (mínimo 2)
  capturas/   capturas de ejecución del esqueleto (mínimo 3)
```

## Nombres de archivo

`AAAA-MM-DD_descripcion-corta.extension`

- `2026-11-21_sesion-diseno-01.jpg`
- `2026-11-20_acta-entrevista-firmada.pdf`
- `2026-11-26_captura-02-servicio-incidencias.png`

## Acta de entrevista — contenido mínimo

1. Lugar y fecha.
2. Nombre completo, cargo y organización del entrevistado.
3. Nombre de los integrantes que participaron.
4. Preguntas y respuestas (o resumen fiel, si el entrevistado prefiere no transcribir).
5. Datos con cifras que sostienen los requisitos: volumen de casos, tiempos, errores, costos.
6. Firma del entrevistado y, si aplica, consentimiento para grabar.
7. Autorización para citar la organización en el documento, o el seudónimo que se usará.

Si no hay organización real, se aplica una encuesta a **al menos 15 usuarios potenciales** y se
adjuntan los resultados crudos: formulario, exportación CSV y constancia de la fecha de recolección.

## Fotografías de sesión (mínimo 2)

- Rostros de los integrantes presentes y la fecha visibles (pizarrón con la fecha, o reloj visible).
- Al menos una debe mostrar el **primer bosquejo de la arquitectura**, para poder contrastarlo con
  el C4 final en el documento.
- No se editan ni se recortan para ocultar que la sesión fue otra.

## Capturas de ejecución (mínimo 3)

Cada captura debe mostrar, en la misma imagen:

- el usuario del sistema en el *prompt* o en la barra de la terminal;
- el nombre de la máquina;
- la fecha y la hora del sistema;
- el comando ejecutado y la respuesta del servicio (o la URL y la respuesta en el navegador);
- preferiblemente los logs de ambos servicios con el mismo `X-Correlation-Id`.

Comando sugerido para que todo aparezca en una sola toma:

```powershell
Write-Host "$env:USERNAME@$env:COMPUTERNAME  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
curl.exe -i http://localhost:8082/api/incidencias/1
```

## Registro en el documento

Cada evidencia se cita en el `.tex` con su ruta relativa, y su existencia se refleja en
`BITACORA.md` el día en que se obtuvo.
