# Insumos de FORM-AC-01 (caída de X, 10 de marzo de 2025) para TA-PFC-E1

Actividad entregada por Angel Zambrano con el equipo MPZ.
Fuente principal: análisis de tráfico de Bitsight (Umbelino, 14/03/2025).

## Qué pasó
X tuvo caídas intermitentes durante el 10 de marzo de 2025 por un ataque DDoS desde una botnet de cámaras IP y grabadores de video. Algunos servidores de origen de X no estaban detrás de la protección DDoS de Cloudflare y sus IP eran visibles desde Internet, así que el tráfico llegó directo a ellos.

## Riesgos para SGIRI
| Riesgo | Cómo se ve en SGIRI | Medida preventiva |
|---|---|---|
| Servicios expuestos directamente | Si servicio-incidencias o servicio-tecnicos aceptan tráfico desde cualquier IP, se puede saturarlos sin pasar por el gateway | En E2, solo el API gateway queda publicado; los servicios aceptan tráfico únicamente de la red interna |
| Peticiones sin límite | Un cliente o un script puede crear tickets sin parar y llenar la cola | Límite de peticiones por IP y por usuario en el gateway |
| Caída que nadie detecta | La mesa de ayuda se entera de que el sistema cayó cuando los clientes reclaman | /actuator/health en cada servicio, alertas y registro de incidentes |
