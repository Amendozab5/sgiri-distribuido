# Guion del video — parte de Angello Mendoza (Líder de Desarrollo)

Duración total de tu parte: **2 minutos 50** repartidos en dos clips.
Se graban por separado y después se pegan con los de Angel y César.

| Clip | Contenido | Duración | Archivo |
|---|---|---|---|
| 1 | Apertura con el repositorio | 30 s | `clip-01-apertura.mp4` |
| 2 | Demostración del esqueleto | 2 min 20 | `clip-04-demo.mp4` |

Orden final de la película: clip 1 (tú), C4 (Angel), requisitos y riesgos (César), demo (tú),
CAP (Angel), cierre (César). Total: unos 6 minutos.

---

## Antes de grabar (5 minutos)

1. Cierra las pestañas del navegador que no sean el repositorio.
2. Abre la terminal maximizada y sube la letra con **Ctrl + scroll** hasta que se lea desde el celular.
3. Limpia la pantalla con `cls`, para que no aparezcan comandos de pruebas anteriores.
4. Arranca los dos servicios **antes** de encender la grabación:

```powershell
Start-Process python -ArgumentList "app.py" -WorkingDirectory "src\servicio_tecnicos" -WindowStyle Hidden
Start-Process python -ArgumentList "app.py" -WorkingDirectory "src\servicio_incidencias" -WindowStyle Hidden
```

5. Prueba el micrófono 10 segundos, escucha y borra.
6. Deja este guion **al lado de la cámara**, no debajo de la pantalla. No se lee: se miran las ideas.

---

## CLIP 1 — Apertura (30 segundos)

**Qué se ve:** el repositorio en GitHub, página principal, con el README y la tabla de integrantes.

**Qué dices:**

> Buenas noches. Somos Zambrano, Mendoza y Macías, y este es SGIRI Distribuido, nuestro proyecto fin
> de curso de Aplicaciones Distribuidas.
>
> SGIRI gestiona las incidencias técnicas de un proveedor de internet: el cliente reporta la falla,
> la mesa de ayuda la asigna y el técnico la atiende desde el celular.
>
> En esta primera entrega presentamos la definición, los requisitos, la arquitectura y un esqueleto
> que ya funciona. Yo soy el Líder de Desarrollo y me encargo del esqueleto y de la demostración.

**Acciones:**

- Al decir «este es SGIRI Distribuido», señala la barra del navegador:
  `github.com/Amendozab5/sgiri-distribuido`.
- Al decir «somos», deja que se lea la tabla de integrantes del README.

**Corte.** No sigas con la demo en el mismo clip: si algo falla, pierdes la apertura.

---

## CLIP 2 — Demostración (2 minutos 20)

Vuelve a la terminal, ejecuta `cls` otra vez y graba pantalla completa.
Aquí puede ser solo tu voz: el rostro ya apareció en el clip 1.

### Paso 1 — El servicio proveedor (20 s)

**Ejecutas:**

```powershell
curl.exe -s http://localhost:8081/api/tecnicos
```

**Dices:**

> Este es el servicio de técnicos, el que provee los datos. Está en el puerto 8081 y devuelve cuatro
> técnicos con su zona, su disponibilidad y cuántos casos tiene abiertos cada uno.

**Pausa de 2 segundos** para que la respuesta se lea en pantalla.

---

### Paso 2 — El filtro (20 s)

**Ejecutas:**

```powershell
curl.exe -s "http://localhost:8081/api/tecnicos?disponible=true"
```

**Dices:**

> Le agregué un filtro para pedir solo los disponibles. Ahora devuelve tres: Jorge Paredes no aparece
> porque tiene cuatro casos abiertos y está marcado como no disponible.
>
> El filtro va en el proveedor y no en el consumidor, para no traer datos que no se van a usar.

**Pausa de 2 segundos.**

---

### Paso 3 — La comunicación entre servicios (45 s)

**Ejecutas:**

```powershell
curl.exe -i -H "X-Correlation-Id: demo-001" http://localhost:8082/api/incidencias/1
```

**Dices, mientras aparece la respuesta:**

> Ahora el servicio de incidencias, en el puerto 8082. Este servicio no guarda una copia del técnico:
> cuando le piden la incidencia 1, hace una petición HTTP al 8081 y arma la respuesta con los dos
> datos. Por eso ven el objeto `tecnico` dentro de la incidencia.
>
> Miren el identificador de correlación: es el mismo que envié y vuelve en la respuesta. En los logs
> de los dos servicios aparece el mismo valor, y eso es lo que permite seguir una petición de
> principio a fin cuando algo falla.

**Pausa de 3 segundos** con la respuesta a la vista. Es el momento más importante del video:
debe leerse `"tecnico": {"id": 1, "nombre": "Luis Vera"...}`.

---

### Paso 4 — La degradación controlada (45 s)

**Ejecutas** (una sola línea, larga: cópiala y pégala para no equivocarte):

```powershell
Get-NetTCPConnection -LocalPort 8081 -State Listen | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

**Dices:**

> Ahora apago el servicio de técnicos, como si se cayera. El servicio de incidencias sigue arriba.

Espera dos segundos y ejecuta:

```powershell
curl.exe -i http://localhost:8082/api/incidencias/1
```

**Dices:**

> Responde 503, con un mensaje de dominio y la indicación de reintentar. No es un 500 con la traza:
> el consumidor se degrada, avisa y el cliente ve algo entendible.
>
> Esa es la mitigación del riesgo R-03 que analizamos en FORM-AC-01: la incidencia no se pierde
> porque falle una dependencia externa.

**Pausa de 3 segundos** para que el 503 se lea completo.

---

### Cierre del clip (10 s)

**Dices:**

> Con eso queda demostrado que los dos servicios se comunican y que el sistema tolera la caída de uno
> de ellos.

**Corte.**

---

## Qué NO debe aparecer en cámara

- La raíz `http://localhost:8081/` con su `ruta no encontrada`: parece un error y no lo es.
- El `KeyboardInterrupt` de cuando se detiene un servicio con Ctrl + C.
- Pestañas del navegador que no sean el repositorio.
- La terminal con comandos viejos: `cls` antes de grabar.

---

## Después de grabar

1. Guarda los archivos como `clip-01-apertura.mp4` y `clip-04-demo.mp4`.
2. Escúchalos una vez. Si el audio está bajo o hay eco, regrábalos ahora: son 3 minutos, no 30.
3. Pásalos a Angel y César junto con los tiempos de cada uno: 60 s el C4, 60 s los requisitos,
   60 s el CAP, 45 s el cierre.
4. Con los seis clips: pegar en Clipchamp en orden, exportar en 1080p, subir a YouTube como
   **no listado** y pegar el enlace en el `README.md`.

---

## Si algo falla durante la grabación

| Síntoma | Qué hacer, sin cortar la grabación |
|---|---|
| El `curl` al 8082 responde 200 pero sin `tecnico` | Corta, reinicia los dos servicios y repite el clip |
| El paso 4 devuelve 200 en vez de 503 | El proceso del 8081 no murió: repite el `Get-NetTCPConnection` y verifica con `curl.exe -s http://localhost:8081/actuator/health` que ya no responde |
| Te equivocas en una frase | Detente, respira y repite **el paso completo**; se recorta en Clipchamp |

---

## Chuleta de comandos (para tenerla a la vista)

```powershell
# arrancar (fuera de cámara)
Start-Process python -ArgumentList "app.py" -WorkingDirectory "src\servicio_tecnicos" -WindowStyle Hidden
Start-Process python -ArgumentList "app.py" -WorkingDirectory "src\servicio_incidencias" -WindowStyle Hidden

# paso 1
curl.exe -s http://localhost:8081/api/tecnicos

# paso 2
curl.exe -s "http://localhost:8081/api/tecnicos?disponible=true"

# paso 3
curl.exe -i -H "X-Correlation-Id: demo-001" http://localhost:8082/api/incidencias/1

# paso 4
Get-NetTCPConnection -LocalPort 8081 -State Listen | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
curl.exe -i http://localhost:8082/api/incidencias/1
```

---

## Verificación oral: si te piden repetir la demo en vivo

Cinco respuestas que debes tener sin mirar nada:

1. **¿Qué hace cada servicio?** Técnicos provee el catálogo y la disponibilidad; incidencias registra
   y consulta, y pide el técnico al otro servicio.
2. **¿Por qué dos procesos y no uno?** Porque el catálogo cambia con otro ritmo y otra carga, y así
   uno puede caerse sin detener al otro.
3. **¿Por qué el timeout es de 2 segundos?** Porque el agente está esperando la respuesta; si el
   proveedor se cuelga, es mejor cortar y responder 503 que dejar la pantalla cargando.
4. **¿Qué es `X-Correlation-Id`?** Un identificador que viaja con la petición y se repite en los logs
   de los dos servicios, para reconstruir qué pasó cuando algo falla.
5. **¿Por qué 503 y no 500?** Porque 503 significa «el servicio no está disponible ahora, reintenta»;
   500 significa «hay un error en mi código», y aquí el código está bien: falta una dependencia.
