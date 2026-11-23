"""
Servicio de incidencias (consumidor) - puerto 8082

Esqueleto de TA-PFC-E1. Demuestra la comunicacion sincronica REST/JSON que
decide el ADR-002: al pedir una incidencia, este servicio consulta al de
tecnicos y devuelve los datos combinados.

Si el servicio de tecnicos no responde, responde 503 con un mensaje de
dominio, no un 500 con la traza: es la mitigacion del riesgo R-03 de
FORM-AC-01 (el alta no debe romperse porque falle una dependencia).

Ejecutar:  python app.py
Probar:    curl -i http://localhost:8082/api/incidencias/1
"""

import json
import uuid
import urllib.error
import urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PUERTO = 8082
URL_TECNICOS = "http://localhost:8081"
TIEMPO_LIMITE = 2.0  # segundos

# Datos en memoria: en E1 no hay base de datos.
INCIDENCIAS = {
    1: {"id": 1, "titulo": "Sin servicio de internet en el sector sur", "estado": "asignada",
        "tecnico_id": 1, "sla_horas": 8},
    2: {"id": 2, "titulo": "Corte intermitente en el nodo 3", "estado": "en_proceso",
        "tecnico_id": 2, "sla_horas": 4},
    3: {"id": 3, "titulo": "Cambio de router en oficina", "estado": "nueva",
        "tecnico_id": None, "sla_horas": 24},
}


def consultar_tecnico(tecnico_id, correlacion):
    """Consulta el servicio de tecnicos con tiempo limite explicito."""
    peticion = urllib.request.Request(
        f"{URL_TECNICOS}/api/tecnicos/{tecnico_id}",
        headers={"X-Correlation-Id": correlacion, "Accept": "application/json"},
    )
    with urllib.request.urlopen(peticion, timeout=TIEMPO_LIMITE) as respuesta:
        return json.loads(respuesta.read().decode("utf-8"))


class Manejador(BaseHTTPRequestHandler):

    def _responder(self, codigo, cuerpo, correlacion):
        datos = json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.send_header("X-Correlation-Id", correlacion)
        self.end_headers()
        self.wfile.write(datos)

    def do_GET(self):
        correlacion = self.headers.get("X-Correlation-Id") or str(uuid.uuid4())
        print(f"{datetime.now():%Y-%m-%d %H:%M:%S} [{correlacion}] GET {self.path}", flush=True)

        if self.path == "/actuator/health":
            return self._responder(200, {"status": "UP", "servicio": "servicio-incidencias"}, correlacion)

        if self.path.startswith("/api/incidencias/"):
            try:
                incidencia_id = int(self.path.rsplit("/", 1)[1])
            except ValueError:
                return self._responder(400, {"error": "el id debe ser un numero"}, correlacion)

            incidencia = INCIDENCIAS.get(incidencia_id)
            if incidencia is None:
                return self._responder(404, {"error": f"la incidencia {incidencia_id} no existe"}, correlacion)

            respuesta = dict(incidencia)
            if incidencia["tecnico_id"] is None:
                respuesta["tecnico"] = None
                respuesta["aviso"] = "sin asignar"
                return self._responder(200, respuesta, correlacion)

            try:
                respuesta["tecnico"] = consultar_tecnico(incidencia["tecnico_id"], correlacion)
            except urllib.error.HTTPError as error:
                # El servicio de tecnicos respondio, pero con un error.
                return self._responder(
                    error.code,
                    {"error": "el servicio de tecnicos rechazo la consulta",
                     "detalle": error.reason, "incidencia_id": incidencia_id},
                    correlacion,
                )
            except (urllib.error.URLError, TimeoutError, OSError) as error:
                # El servicio de tecnicos no responde: se degrada el servicio,
                # no se rompe la consulta de la incidencia.
                return self._responder(
                    503,
                    {"error": "el servicio de tecnicos no esta disponible",
                     "detalle": str(error), "reintentar": True,
                     "incidencia_id": incidencia_id},
                    correlacion,
                )

            return self._responder(200, respuesta, correlacion)

        self._responder(404, {"error": "ruta no encontrada"}, correlacion)

    def log_message(self, formato, *args):
        pass


if __name__ == "__main__":
    print(f"servicio-incidencias escuchando en http://localhost:{PUERTO}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PUERTO), Manejador).serve_forever()
