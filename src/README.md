# `src/` — esqueleto funcional (TA-PFC-E1)

Dos servicios independientes que se comunican por **REST/JSON síncrono**, el mecanismo que decide
el ADR-002. No tienen lógica de negocio: demuestran que la base técnica distribuida funciona.

| Servicio | Puerto | Rol | Archivo |
|---|---|---|---|
| `servicio-tecnicos` | 8081 | Proveedor: catálogo y disponibilidad de técnicos | `servicio_tecnicos/app.py` |
| `servicio-incidencias` | 8082 | Consumidor: consulta al proveedor y devuelve los datos combinados | `servicio_incidencias/app.py` |

## Por qué Python y no Spring Boot

Para que el jurado pueda ejecutarlo **sin descargar dependencias ni instalar un JDK**: solo se
necesita Python 3.10 o superior, que ya viene instalado o se instala en dos minutos. El objeto de
E1 no es el framework, es demostrar la comunicación entre servicios y el comportamiento ante
fallos. El día que se cambie de stack, el contrato (REST/JSON, timeout, `503`, correlación) sigue
siendo el mismo.

## Cómo se ejecuta

```powershell
# Terminal 1
cd src\servicio_tecnicos
python app.py

# Terminal 2
cd src\servicio_incidencias
python app.py
```

Verificación, en una tercera terminal:

```powershell
curl.exe -i http://localhost:8081/actuator/health
curl.exe -i -H "X-Correlation-Id: prueba-001" http://localhost:8082/api/incidencias/1
```

La segunda llamada no devuelve datos guardados en el servicio de incidencias: el campo `tecnico`
lo trae de una petición HTTP real al puerto 8081. Eso es lo que hay que mostrar en el video.

## Comportamiento ante fallos (lo que se califica)

1. Detener el servicio de técnicos (cerrar su terminal).
2. Pedir de nuevo `http://localhost:8082/api/incidencias/1`.
3. Debe responder **`503`** con `{"error": "el servicio de tecnicos no esta disponible",
   "reintentar": true}`, **no** un `500` con traza.

Esa es la mitigación del riesgo R-03 de FORM-AC-01: la incidencia se puede consultar aunque falle
una dependencia. Es la tercera captura y es el argumento técnico más fuerte del esqueleto.

## Qué hay que poder explicar en el video

- Qué hace cada servicio y por qué son dos procesos distintos y no uno.
- Qué pasa en el código cuando llega `GET /api/incidencias/1`.
- Por qué el tiempo límite es de 2 segundos y qué evita.
- Qué es `X-Correlation-Id` y para qué sirve cuando algo falla.
- Por qué un `503` es mejor que un `500` en este caso.

Si alguien del equipo no puede responder estas cinco preguntas, no está listo para la verificación
oral del docente.

## Qué no se construyó (y se dice en el documento)

Base de datos, contenedores, API Gateway, autenticación y carga real de archivos: corresponden a E2,
E3 y E4. En E1 se declara el alcance, no se finge.

## Capturas obligatorias (3)

Guardar en `evidencias/capturas/` como `AAAA-MM-DD_HHMM_descripcion.png`, mostrando en la misma
imagen: usuario del sistema, nombre de la máquina, fecha y hora, el comando ejecutado y la respuesta.
