# Encuesta a usuarios potenciales

Ruta de respaldo cuando no hay una organización real disponible (la admite el enunciado de E1).
Mínimo **15 respuestas** y se adjuntan los **resultados crudos**.

## A quién se encuesta

Personas que hoy atienden incidencias o reciben soporte técnico: agentes de mesa de ayuda,
técnicos de campo, responsables de operaciones de proveedores de internet, administradores de red
de empresas pequeñas. No se encuesta a compañeros de clase que nunca han hecho esa tarea: sus
respuestas no describen el problema.

Registrar en el archivo de resultados: fecha de recolección, canal de distribución y cantidad de
respuestas por canal.

## Instrumento (12 ítems)

**Consentimiento (obligatorio, primera pantalla):** «Esta encuesta es para un proyecto académico de
la UTEQ sobre gestión de incidencias técnicas. Es anónima, dura 3 minutos y los resultados se usan
solo con fines académicos. ¿Acepta participar?»

1. ¿Cuál es su rol? (mesa de ayuda / técnico de campo / responsable de operaciones / otro)
2. ¿Cuántas incidencias atiende o registra en una semana normal? (1–5 / 6–15 / 16–30 / 31–60 / más de 60)
3. ¿Cuántas en una semana de corte o emergencia? (mismas opciones)
4. ¿Con qué registra hoy las incidencias? (hoja de cálculo / WhatsApp / cuaderno / sistema propio / otro)
5. ¿Cuánto tarda en registrar una incidencia? (menos de 1 min / 1–3 min / 3–5 min / más de 5 min)
6. ¿Cuánto tarda en asignarla a un técnico? (menos de 5 min / 5–15 min / 15–60 min / más de 1 hora)
7. De cada 10 casos, ¿cuántos se duplican, se pierden o se reabren? (0 / 1–2 / 3–5 / más de 5)
8. ¿El cliente puede consultar el estado sin llamar? (sí / no / a veces)
9. ¿Tienen un tiempo de compromiso (SLA)? (sí, ¿cuántas horas? / no / no sé)
10. ¿Cuántas veces al mes se incumple ese compromiso? (0 / 1–2 / 3–5 / más de 5 / no aplica)
11. ¿En qué horario se atienden las incidencias? (solo oficina / extendido / 24-7)
12. Si pudiera cambiar una sola cosa del proceso actual, ¿cuál sería? (respuesta abierta, 1 línea)

Ítems 2, 3, 5, 6, 7 y 10 son los que alimentan la tabla de consecuencias del documento y los RNF.

## Cómo se recolecta

1. Crear el formulario en Google Forms o Microsoft Forms con las preguntas tal cual (no reformular).
2. Activar «recopilar correos» solo si se necesita; si no, mantener anónimo.
3. Distribuir por: grupos de WhatsApp de técnicos o de la carrera, LinkedIn con el filtro de
   soporte técnico en Quevedo/Quevedo–Babahoyo, contactos directos de proveedores locales.
4. Meta: 15 respuestas en 48 horas. Si al viernes 20 hay menos de 10, insistir por contacto directo.
5. Exportar a CSV y a PDF **sin editar**; guardar ambos en `evidencias/acta/` con fecha.

## Cómo se usa en el documento

- La tabla de consecuencias usa los porcentajes agregados: «7 de cada 10 encuestados (n=17)
  registran en hoja de cálculo; 5 de 17 tardan más de 5 minutos por caso».
- Cada requisito derivado se cita como `[Encuesta, ítem 6, n=17]`.
- En el documento se declara que se usó la ruta de encuesta por no contar con una organización
  disponible, y se explica cómo se eligió a los encuestados.

## Lo que invalida la encuesta

- Recolectar respuestas de personas que no hacen la tarea.
- Completar respuestas «a mano» con conocidos para llegar a 15.
- Presentar porcentajes sin el n y sin la fecha de recolección.
- Editar el CSV antes de guardarlo.
