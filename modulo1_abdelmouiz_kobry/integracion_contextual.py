"""Cruces exploratorios m:1 con estadisticas publicas, nunca predictores personales."""
from __future__ import annotations
from pathlib import Path
import pandas as pd

DATOS=Path(__file__).resolve().parent/'data'
COLUMNAS_CONTEXTO=(
 'INE_Redes_Sociales_Participacion_Pct_2025',
 'SIIU_Nota_Expediente_Grado_10_2024_25',
 'ESTUDES_RRSS_Uso_Problematico_Pct_2025'
)


def integrar_contexto(base: pd.DataFrame, referencias: Path = DATOS):
    """Tres uniones exploratorias conservan filas y valores NA fuera del ambito."""
    referencias=Path(referencias)
    d=base.copy(deep=True)
    n=len(d)
    ine=pd.read_csv(referencias/'INE_TICH_2025_contexto.csv')
    if not ine['Grupo_Edad_INE'].is_unique: raise ValueError('Claves INE duplicadas')
    d['Grupo_Edad_INE']=d['Age'].between(16,74).map({True:'16-74', False:'fuera'})
    d=d.merge(ine,how='left',on='Grupo_Edad_INE',validate='m:1',sort=False).drop(columns=['Grupo_Edad_INE'])
    siiu=pd.read_csv(referencias/'SIIU_2024_25_contexto.csv')
    if not siiu['Academic_Level'].is_unique: raise ValueError('Claves SIIU duplicadas')
    d=d.merge(siiu,how='left',on='Academic_Level',validate='m:1',sort=False)
    est=pd.read_csv(referencias/'ESTUDES_2025_contexto_edad_sexo.csv')
    if est.duplicated(['Edad_ESTUDES','Gender']).any(): raise ValueError('Claves ESTUDES duplicadas')
    d['Edad_ESTUDES']=d['Age'].where(d['Academic_Level'].eq('High School'),other=-1)
    d=d.merge(est,how='left',on=['Edad_ESTUDES','Gender'],validate='m:1',sort=False).drop(columns=['Edad_ESTUDES'])
    if len(d)!=n or d.index.has_duplicates:
        raise AssertionError('Error en integracion: alteracion del numero de filas')
    cobertura={k: int(d[k].notna().sum()) for k in COLUMNAS_CONTEXTO}
    return d, {'filas_entrada':n,'filas_salida':len(d),'cobertura':cobertura,
       'uso': 'contexto exploratorio, no atributos personales ni predictivos'}
