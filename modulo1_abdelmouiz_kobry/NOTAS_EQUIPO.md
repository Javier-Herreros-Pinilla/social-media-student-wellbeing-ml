# Nota para Javier y el resto del equipo

**Entrega de Abdelmouiz kobry.** Se han preparado funciones separadas para la selección del CSV, la normalización de campos y la integración contextual de INE/SIIU/ESTUDES. Se aporta una sección para incorporar al informe académico.

El notebook principal ejecutado anteriormente activa una generación artificial cuando no encuentra el CSV original. La fuente abierta con 4.500 registros contiene 46 valores ausentes de estrés y 85 de GPA; además `Overall_Impact` tiene clases muy desiguales. Por tanto, los resultados y gráficas anteriores no son directamente trasladables a esa fuente.

- Ernesto (Módulo 2): comprobar ausencias y datos atípicos sobre la fuente seleccionada; posponer imputación/LOF supervisado hasta definir particiones si se usarán en predicción.
- Pablo (Módulo 3): evitar derivados de tasas oficiales agregadas como variables predictoras individuales; revisar ordinales y transformaciones.
- Yeni (Módulo 4): recalcular PCA y rankings con las variables definitivas, ajustando transformaciones en entrenamiento y validación.
- Javier (Módulo 5): repetir baselines y métricas (Macro F1 además de accuracy), y confirmar metodología, formato ACM y composición del equipo con el profesor.

No se han modificado los modelos de los demás componentes. Las fuentes están identificadas en `FUENTES_Y_DECISIONES.md` y las salidas locales no se incluyen en el repositorio.
