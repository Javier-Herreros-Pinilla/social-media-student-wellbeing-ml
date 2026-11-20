"""Seleccion de variables y normalizacion sin imputacion ni fuga de datos."""
from __future__ import annotations
import pandas as pd

OBJETIVOS = ('Overall_Impact', 'Academic_Performance_GPA')
MAPAS = {
    'Academic_Level': {'Undergraduate':'Undergrad', 'Postgraduate':'Postgrad'},
    'Primary_Platform': {'X (Twitter)':'X'},
    'Social_Comparison_Frequency': {'Frequently':'Often'}
}


def _booleano(valor):
    if pd.isna(valor): return pd.NA
    if isinstance(valor, bool): return valor
    val=str(valor).strip().casefold()
    if val in ('true','1','yes','si','sí'): return True
    if val in ('false','0','no'): return False
    raise ValueError(f'Late_Night_Usage desconocido: {valor}')


def seleccionar_y_normalizar(datos: pd.DataFrame) -> pd.DataFrame:
    if 'Student_ID' not in datos or any(t not in datos for t in OBJETIVOS):
        raise ValueError('El CSV no contiene el identificador o ambos objetivos.')
    d=datos.copy(deep=True)
    for col in ('Gender', 'Academic_Level', 'Primary_Platform', 'Device_Type',
                'Social_Comparison_Frequency', 'Overall_Impact'):
        d[col]=d[col].astype('string').str.strip().str.normalize('NFKC')
    for col, mapa in MAPAS.items():
        d[col]=d[col].replace(mapa)
    d['Late_Night_Usage']=d['Late_Night_Usage'].map(_booleano).astype('boolean')
    for col in ('Age','Daily_Usage_Hours','Weekend_Extra_Hours','Sleep_Duration_Hours',
                'Sleep_Quality_Score','Perceived_Stress_Score',
                'Mental_Health_Index','Academic_Performance_GPA'):
        d[col]=pd.to_numeric(d[col],errors='raise')
    d=d.drop(columns=['Student_ID'])
    if len(d)!=len(datos):
        raise AssertionError('La seleccion no debe eliminar observaciones.')
    return d


def variables_predictoras(datos: pd.DataFrame) -> list[str]:
    return [c for c in datos.columns if c not in OBJETIVOS]
