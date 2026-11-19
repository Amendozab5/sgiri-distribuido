# Diagramas

Los diagramas se elaboran en **draw.io** (app.diagrams.net) y se versionan editables. La imagen
exportada se usa en el documento; el `.drawio` es lo que demuestra autoría y evolución.

## Archivos previstos

| Archivo | Contenido | Nivel C4 |
|---|---|---|
| `c4-n1-contexto.drawio` | SGIRI, sus tres tipos de usuario y los sistemas externos (pasarela de correo, Cloudinary, red del proveedor) | 1 |
| `c4-n2-contenedores.drawio` | Servicios, bases de datos, API Gateway y las flechas con tipo de comunicación | 2 |
| `bosquejo-inicial.jpg` | Foto del primer bosquejo a mano (sesión del 21/11) | — |

Exportaciones: PNG a 300 dpi en `../figuras/` con el mismo nombre base. No se exporta a PDF si el
`.tex` ya incluye el PNG, para no duplicar peso.

## Convenciones

- Cada elemento del nivel 2 debe tener un identificador (`SVC-INC`, `DB-TKT`, `GW-01`) que se use
  también en la tabla del modelo de comunicación y en la tabla de trazabilidad del documento.
- Las flechas llevan etiqueta con el mecanismo y el tipo: `REST/JSON · sincrónica`,
  `AMQP · asincrónica`.
- Los sistemas externos se dibujan fuera del límite del sistema (recuadro punteado).
- No se agregan componentes que no existan en `src/` o que no estén planificados en el plan del
  proyecto: un contenedor dibujado es un compromiso, no una ilustración.

## Regla de coherencia

Si un diagrama cambia, se actualizan en el mismo *pull request*: la tabla de comunicación, el ADR
correspondiente y la sección de CAP/PACELC. El C4 no se redibuja al final para «que se vea mejor».
