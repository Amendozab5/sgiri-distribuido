# SGIRI Distribuido — Sistema de Gestión de Incidencias

Proyecto Fin de Curso (PFC) de **Aplicaciones Distribuidas**, 7.º nivel, paralelo B.
Entrega **TA-PFC-E1**: definición, requisitos y arquitectura base del sistema distribuido.
Cierre de la entrega: **domingo 29 de noviembre de 2026, 23:55**.

SGIRI resuelve la gestión de incidencias técnicas de un proveedor de servicios de internet: alta
del ticket, asignación al técnico, seguimiento del SLA y comunicación con el cliente. El sistema se
construye como **microservicios** porque los usuarios (técnicos de campo, mesa de ayuda y clientes)
están distribuidos, el servicio debe seguir operando fuera del horario de oficina y cada módulo
necesita desplegarse sin detener los demás.

> **Estado:** E1 en construcción. La estructura, el documento LaTeX y los ADR ya están
> versionados; el esqueleto de `src/` lo implementa el Líder de Desarrollo según
> `src/README.md`.

## Integrantes y roles

| Integrante | GitHub | Rol | Responsable de |
|---|---|---|---|
| Zambrano Yong Angel Daniel | [@iMouraad](https://github.com/iMouraad) | Arquitecto **y** Responsable de Documentación | Diagramas C4, ADR-001 y ADR-002, modelo de comunicación, análisis CAP/PACELC, justificación distribuida, integración del documento, tablero, bitácora |
| Mendoza Bermello Angello Agustín | [@Amendozab5](https://github.com/Amendozab5) | Líder de Desarrollo | Esqueleto en `src/`, comunicación entre servicios, instrucciones de ejecución, capturas |
| Macías Vásquez César Abraham | [@CesarMacias007](https://github.com/CesarMacias007) | Responsable de Calidad | Historias de usuario, requisitos no funcionales con ISO/IEC 25010, riesgos, trabajos relacionados, pruebas y revisión de coherencia |

Equipo de tres integrantes: el Arquitecto asume además el rol de Documentación.

Repositorio: <https://github.com/Amendozab5/sgiri-distribuido> · Colaboradores con permiso de
escritura: `@CesarMacias007` y `@iMouraad`.

## Estructura del repositorio

```
/                       README.md, BITACORA.md, .gitignore
/src/                   servicios del esqueleto (Java 21 + Spring Boot)
/docs/                  main.tex, referencias.bib, secciones/, figuras/, PDF compilado
/docs/adr/              ADR-001 y ADR-002 en Markdown
/docs/diagramas/        archivos editables .drawio y sus exportaciones
/evidencias/            acta o encuesta, fotografías de sesiones y capturas de ejecución
```

## Documento LaTeX

Archivo principal: `docs/main.tex`. Bibliografía: `docs/referencias.bib` (biblatex + biber,
estilo IEEE). El PDF compilado se versiona en `docs/main.pdf`.

**Dependencias:** TeX Live o MiKTeX con `pdflatex`, `biber` y los paquetes `babel-spanish`,
`biblatex`, `biblatex-ieee`, `csquotes`, `booktabs`, `tabularx`, `lmodern`, `microtype`,
`caption`, `xcolor` y `hyperref`.

**Orden de compilación** (desde `docs/`):

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Se compila desde cero al clonar el repositorio: no hay rutas absolutas ni archivos fuera de
`docs/`. Las figuras viven en `docs/figuras/` y se referencian con ruta relativa.

## Ejecución del esqueleto

Verificado el 22 de noviembre de 2026. Requiere Python 3.10 o superior y nada más.

```bash
# Terminal 1 — servicio proveedor
cd src/servicio_tecnicos && python app.py       # http://localhost:8081

# Terminal 2 — servicio consumidor
cd src/servicio_incidencias && python app.py    # http://localhost:8082

# Verificación
curl -i http://localhost:8082/api/incidencias/1
```

Con el servicio de técnicos apagado, la misma llamada responde `503` (degradación controlada),
no `500`. El detalle está en [`src/README.md`](src/README.md).

## Video de presentación

> Pendiente. Enlace público de 5 a 7 minutos: cada integrante explica su rol y se muestra el
> esqueleto en ejecución. Se publica aquí y en la entrega del SGA.

## Tablero de trabajo

GitHub Projects del repositorio, con los issues de E1 y E2 asignados por integrante.
Cada issue tiene criterio de aceptación y se cierra al integrar su pull request.

## Origen del proyecto y atribución

Este repositorio es nuevo y su historial corresponde solo a este PFC. Reutiliza de forma selectiva
—y atribuida— piezas del proyecto **SGIRI / SGIM** de Aplicaciones Web. El detalle de qué se tomó,
de qué commit y de qué autores está en [`docs/ATRIBUCION.md`](docs/ATRIBUCION.md).

## Documentos de trabajo

- [`docs/PLAN-TRABAJO.md`](docs/PLAN-TRABAJO.md) — cronograma vigente y reparto por integrante.
- [`docs/TABLERO.md`](docs/TABLERO.md) — issues de E1 y E2 para GitHub Projects.
- [`docs/levantamiento/`](docs/levantamiento/) — guion de entrevista, acta y encuesta.
- [`docs/FORM-AC-01-insumos.md`](docs/FORM-AC-01-insumos.md) — qué se extrae del análisis del
  incidente de Fastly para los riesgos y las mitigaciones de E1.
- [`BITACORA.md`](BITACORA.md) — sesiones, decisiones y problemas resueltos.
