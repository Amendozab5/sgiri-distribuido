"""
Servicio de tecnicos (proveedor) - puerto 8081

Esqueleto de TA-PFC-E1: no tiene logica de negocio, solo demuestra que el
servicio responde por HTTP y que otro servicio puede consultarlo.

Ejecutar:  python app.py
Probar:    curl http://localhost:8081/api/tecnicos
           curl http://localhost:8081/actuator/health
"""

import json
import uuid
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PUERTO = 8081

# Datos en memoria: en E1 no hay base de datos.
TECNICOS = {
    1: {"id": 1, "nombre": "Luis Vera", "zona": "Quevedo centro", "disponible": True, "casos_abiertos": 2},
    2: {"id": 2, "nombre": "Marta Solis", "zona": "Buena Fe", "disponible": True, "casos_abiertos": 1},
    3: {"id": 3, "nombre": "Jorge Paredes", "zona": "Valencia", "disponible": False, "casos_abiertos": 4},
}


class Manejador(BaseHTTPRequestHandler):
    """Atiende las peticiones GET del servicio."""

    def _responder(self, codigo, cuerpo, correlacion):
        datos = json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.send_header("X-Correlation-Id", correlacion)
        self.end_headers()
        self.wfile.write(datos)

    def do_GET(self):
        # El identificador de correlacion llega del servicio que llama; si no
        # viene, se genera uno. Asi se puede seguir una peticion entre los dos
        # servicios revisando los logs.
        correlacion = self.headers.get("X-Correlation-Id") or str(uuid.uuid4())
        print(f"{datetime.now():%Y-%m-%d %H:%M:%S} [{correlacion}] GET {self.path}", flush=True)

        if self.path == "/actuator/health":
            return self._responder(200, {"status": "UP", "servicio": "servicio-tecnicos"}, correlacion)

        if self.path == "/api/tecnicos":
            return self._responder(200, list(TECNICOS.values()), correlacion)

        if self.path.startswith("/api/tecnicos/"):
            try:
                tecnico_id = int(self.path.rsplit("/", 1)[1])
            except ValueError:
                return self._responder(400, {"error": "el id debe ser un numero"}, correlacion)

            tecnico = TECNICOS.get(tecnico_id)
            if tecnico is None:
                return self._responder(404, {"error": f"el tecnico {tecnico_id} no existe"}, correlacion)
            return self._responder(200, tecnico, correlacion)

        self._responder(404, {"error": "ruta no encontrada"}, correlacion)

    def log_message(self, formato, *args):
        # Se silencia el log por defecto: ya se imprime una linea por peticion.
        pass


if __name__ == "__main__":
    print(f"servicio-tecnicos escuchando en http://localhost:{PUERTO}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PUERTO), Manejador).serve_forever()
