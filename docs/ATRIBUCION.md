# Atribución y origen del contenido reutilizado

Este repositorio nace en noviembre de 2026 para el PFC de **Aplicaciones Distribuidas**. No es un
clon ni un fork del proyecto anterior: su historial de Git corresponde únicamente a este PFC.

## Regla

Ningún archivo se copia sin registrarlo aquí **en el mismo commit** en que se incorpora, con su
origen exacto (repositorio, commit y autor). Si el archivo proviene de un autor que no pertenece
al equipo, se indica expresamente.

## Procedencia autorizada

| Elemento | Origen | Commit | Autoría | Estado |
|---|---|---|---|---|
| Dominio del problema (incidencias, técnicos, SLA, catálogos) | Repositorio SGIRI / SGIM, Aplicaciones Web | `7eb5587` (`main`) | Amendozab5 (Angello Mendoza, integrante de este equipo) y coautores | Se usa como **referencia conceptual**, sin copiar código |
| Modelo de datos de ejemplo (`SGIM2`, 47 tablas, 2 701 filas) | Respaldo recuperado del historial de SGIRI (2026-03-20) | `5e38f0a` | Amendozab5 y coautores | **Previsto para E3** como semilla de datos de prueba; es un dataset del prototipo académico, no datos de una empresa real |
| Datos de prueba y nombres de catálogos | Mismo respaldo | `5e38f0a` | Amendozab5 y coautores | Previsto para E3 |
| Logotipo | Repositorio SGIRI | `7eb5587` | Amendozab5 y coautores | Opcional; si se usa, se conserva esta fila |

El repositorio de origen pertenece a uno de los integrantes de este equipo, pero su historial muestra también commits de **JustynCruz04**, **DannaN24** y **Andymendoza17**. Que el autor principal participe en este PFC no borra esa autoría compartida: si se reutiliza un archivo de esas líneas, se atribuye también a ellos.

## Lo que no se reutiliza

- El backend monolítico de SGIRI (Spring Boot + Angular, una sola instancia, una sola base): la
  arquitectura de este PFC es de microservicios y el C4 debe describirla, no al monolito.
- Las 98 confirmaciones del historial anterior: no cuentan como trabajo de este periodo y
  confundirían la evidencia de autoría.
- Configuración de Java 25: este proyecto usa **Java 21 LTS**, que es lo que está instalado en los
  equipos del equipo y lo que un tercero puede reproducir.

## Cómo se declara en el documento

El `.tex` incluye una nota en la sección de implementación y en la declaración de uso de IA con el
enlace a este archivo. La tabla de aportes del documento enlaza los commits propios.
