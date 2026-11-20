# Fuentes y decisiones para el Módulo 1

Responsable: Abdelmouiz kobry. Curso: Minería de Datos, UCLM, 2026/2027.

## Datos del trabajo

- Dataset anunciado: *Impact of Social Media on Life*, publicado en Kaggle: https://www.kaggle.com/datasets/harishyadav0506/impact-of-social-media-on-life
- Copia abierta con esquema coincidente, inspeccionada para reproducibilidad: https://github.com/marupakanandhini269/Impact-of-Social-Media-on-Life/blob/main/Social_media_impact_on_life.csv
- La copia mencionada tiene 4.500 registros y 16 columnas, 46 valores vacíos en `Perceived_Stress_Score` y 85 en `Academic_Performance_GPA`.
- Variable objetivo de clasificación: `Overall_Impact` (3.681 Beneficial, 654 Neutral, 165 Negative). Segundo objetivo posible: `Academic_Performance_GPA`.
- La copia se identifica mediante tamaño y SHA-1 de objeto Git. El script también registra SHA-256 en el JSON de evidencia, sin necesidad de subir un archivo manifiesto.
- No hemos podido demostrar que la edición actual de Kaggle y esta copia GitHub sean bit a bit idénticas, ni verificar el muestreo original. Sin ficha metodológica no puede afirmarse que sea una encuesta representativa de estudiantes reales.

## INE, Encuesta TIC-H 2025

Referencia: https://www.ine.es/infografias/infografia_tichogares.pdf

En la población española de 16 a 74 años, 69,5% participó en redes sociales en los tres últimos meses. Esta cifra NO mide horas de uso ni sueño. Su unión por edad se utiliza solo como referencia contextual; no caracteriza a cada alumno.

## SIIU, Estadística de rendimiento 2024/2025

Referencia: https://www.ciencia.gob.es/Ministerio/Estadisticas/SIIU/Rendimiento.html

La nota media del expediente de Grado es 7,42/10; Máster es 8,32/10. Solo se usa la primera para una correspondencia descriptiva de `Undergrad`, sin equivalencia demostrada con el GPA personal de la fuente ni extrapolación a alumnos de otros países.

## OEDA, Encuesta ESTUDES 2025

Referencia: https://www.sanidad.gob.es/gabinetePrensa/notaPrensa/pdf/2025_090226112109595.pdf

Figura 28 (página impresa 65): prevalencia de *posible uso problemático de redes sociales* por edad y sexo, entre estudiantes de 14 a 18 años de centros españoles. No representa tecnoestrés clínico, probabilidad individual ni prevalencia por plataforma. Los valores transcritos figuran en `data/ESTUDES_2025_contexto_edad_sexo.csv`. Se añaden solo al grupo de Secundaria que coincida en edad y sexo.

## Criterio de integración

Se emplean uniones `LEFT JOIN` con claves únicas en las tablas de referencia y validación `many-to-one`. Se preserva el número de registros y el valor ausente cuando el emparejamiento no es válido. Debido a que el dataset de alumnos no identifica país o ámbito muestral, las columnas agregadas de España son solo una vista de contexto ecológico. No pueden utilizarse como predictores individuales ni fundamentar inferencias causales.

## Decisiones transferidas a Módulos 2 a 5

- No imputar los valores faltantes en esta etapa; más adelante usar partición train/test y ajustar cualquier imputador y escalador dentro del entrenamiento y de la validación cruzada.
- No usar `Student_ID`, columnas contextuales oficiales ni el otro objetivo como predictor de manera automática.
- Comprobar la construcción de la etiqueta `Overall_Impact`, el desequilibrio de clases y la posible fuga de datos antes de cualquier evaluación.
- Rehacer las gráficas, PCA y baselines del cuaderno anterior sobre la versión de datos que apruebe el equipo: el cuaderno anterior se ejecutó con una réplica generada automáticamente cuando faltaba el CSV.
