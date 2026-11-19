# Módulo 1. Selección e integración de información

**Responsable:** Abdelmouiz kobry

Parte del proyecto *Impacto de las Redes Sociales en el Bienestar y Rendimiento Estudiantil*. Esta unidad corresponde a la fase KDD de selección de fuentes, elección de atributos, auditoría de entrada y documentación de uniones externas.

## Orden de trabajo

1. `fuente_auditoria.py` lee la copia pública del CSV, verifica su esquema e informa sobre duplicados, nulos y clases. La descarga se solicita expresamente; el código no genera datos alternativos.
2. `seleccion_normalizacion.py` normaliza unas pocas categorías documentadas y excluye `Student_ID`, conservando los dos objetivos y sin imputación.
3. `integracion_contextual.py` agrega una vista exploratoria de INE, SIIU y ESTUDES mediante tres `LEFT JOIN`, con control de claves y conservación de filas. La vista no se usa para entrenamiento.
4. `ejecutar_modulo1.py` ejecuta la cadena completa y exporta CSV de base normalizada, CSV de contexto, y JSON de evidencia al directorio `outputs/` (ignorado por Git).

Para ejecutar con el CSV abierto verificado:

```bash
python -m pip install -r requirements.txt
python ejecutar_modulo1.py --descargar
python -m unittest discover -s tests -v
```

No afirmar que la copia alojada en GitHub sea idéntica a la revisión de Kaggle sin cotejo adicional. El significado clínico de variables como `Perceived_Stress_Score` debe comprobarse con la documentación original antes de usar etiquetas diagnósticas.

## Entrega académica

El texto para el informe se encuentra en `Seccion_1_Abdelmouiz_kobry.docx`. Javier debe integrarlo en el informe global de 2 a 8 páginas, con el formato ACM especificado por el profesor. Los demás módulos deben rehacer el análisis al cambiar la fuente; no utilizar la tarjeta de datos generada previamente como evidencia empírica.
