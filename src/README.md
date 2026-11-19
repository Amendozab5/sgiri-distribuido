# `src/` — esqueleto funcional (TA-PFC-E1)

Contrato de lo que debe existir en esta carpeta al cierre del **domingo 29 de noviembre de 2026**.
No se requiere lógica de negocio completa: se requiere demostrar que la base técnica distribuida
funciona y que un tercero la levanta siguiendo solo el `README.md` de la raíz.

## Servicios

| Servicio | Responsable | Puerto | Rol en el esqueleto |
|---|---|---|---|
| `servicio-tecnicos` | Angello | 8081 | Catálogo de técnicos y su disponibilidad. Es el servicio **proveedor**. |
| `servicio-incidencias` | Angello | 8082 | Registra consultas de incidencia y **consume** al de técnicos para asignar. Es el servicio **consumidor**. |

## Interacción mínima exigida

1. `GET http://localhost:8081/api/tecnicos` → lista de técnicos (datos en memoria, sin base de datos en E1).
2. `GET http://localhost:8081/api/tecnicos/{id}` → un técnico; `404` si no existe.
3. `GET http://localhost:8082/api/incidencias/{id}` → la incidencia **con los datos del técnico
   resueltos por llamada HTTP al puerto 8081** (no datos duplicados ni copiados a mano).
4. `GET http://localhost:8081/actuator/health` y `:8082/actuator/health` → `{"status":"UP"}`.

Si el puerto 8081 está apagado, el servicio de incidencias debe responder `503` con un mensaje
claro, **no** un error 500 con traza. Esto es la mitigación mínima del riesgo R-02 y del R-03
heredados de FORM-AC-01 (ver `docs/FORM-AC-01-insumos.md`).

## Requisitos técnicos de la implementación

- Java 21 (LTS) y Maven Wrapper (`mvnw`). **No** usar Java 25 como en SGIRI: no está instalado en
  los equipos del equipo y rompe la reproducibilidad.
- Spring Boot 3.4.x. Sin base de datos en E1 (`Map` en memoria o `H2` en memoria).
- Comunicación según ADR-002: REST/JSON síncrono con `RestClient` y timeout explícito
  (`connect-timeout` y `read-timeout` de 2 s).
- Propagar `X-Correlation-Id` en la llamada entre servicios y registrarlo en ambos logs.
- `README.md` de la raíz con: requisitos, comandos exactos, URLs y resultado esperado.

## Qué NO se construye en E1

- Base de datos distribuida, réplicas o particionado (es E3).
- Contenedores y API Gateway (es E2).
- Autenticación completa, frontend o carga de archivos real.

## Capturas obligatorias (3)

Guardar en `evidencias/capturas/` con el nombre `AAAA-MM-DD_HHMM_descripcion.png` y, en la misma
imagen, mostrar: usuario del sistema, nombre de la máquina, fecha y hora, el comando ejecutado
(`curl` o navegador) y la respuesta. Ver `evidencias/README.md`.
