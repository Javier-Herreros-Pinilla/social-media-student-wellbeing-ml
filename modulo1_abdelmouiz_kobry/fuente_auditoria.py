"""Origen y auditoria de datos para la primera fase KDD."""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import pandas as pd
from urllib.request import Request, urlopen

COLUMNAS = [
    'Student_ID','Age','Gender','Academic_Level','Primary_Platform',
    'Daily_Usage_Hours','Weekend_Extra_Hours','Device_Type',
    'Sleep_Duration_Hours','Sleep_Quality_Score','Late_Night_Usage',
    'Social_Comparison_Frequency','Perceived_Stress_Score',
    'Mental_Health_Index','Academic_Performance_GPA','Overall_Impact'
]
ESPEJO_URL = ('https://raw.githubusercontent.com/marupakanandhini269/'
    'Impact-of-Social-Media-on-Life/main/Social_media_impact_on_life.csv')
KAGGLE_REFERENCIA = 'https://www.kaggle.com/datasets/harishyadav0506/impact-of-social-media-on-life'
GIT_BLOB_ESPERADO = '0fa68d5f03c79c51eb817d67514980d04f0cd6be'
LONGITUD_ESPERADA = 475478
ARCHIVO_LOCAL = Path(__file__).resolve().parent / 'data' / 'origen.csv'


def git_blob_sha1(content: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(content)).encode() + b'\0' + content).hexdigest()


def descargar_espejo(destino: Path = ARCHIVO_LOCAL) -> Path:
    """Baja una copia publica fija; no certifica identidad con la edicion de Kaggle."""
    req = Request(ESPEJO_URL, headers={'User-Agent': 'UCLM-MineriaDatos-E2/1.0'})
    with urlopen(req, timeout=45) as res:
        data = res.read()
    if len(data) != LONGITUD_ESPERADA or git_blob_sha1(data) != GIT_BLOB_ESPERADO:
        raise ValueError('La copia publica ha cambiado. Verifica su procedencia antes de continuar.')
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(data)
    return destino


def cargar_y_auditar(ruta: Path, *, exigir_version_referencia: bool = False):
    ruta = Path(ruta)
    if not ruta.is_file():
        raise FileNotFoundError(f'No existe el CSV: {ruta}. No se generan datos alternativos.')
    contenido = ruta.read_bytes()
    df = pd.read_csv(ruta, encoding='utf-8-sig', low_memory=False)
    if list(df.columns) != COLUMNAS:
        raise ValueError('El esquema o el orden de columnas no coincide con los 16 atributos esperados.')
    if df['Student_ID'].isna().any() or df['Student_ID'].duplicated().any():
        raise ValueError('Student_ID no puede contener vacios ni duplicados.')
    clases = {'Beneficial', 'Neutral', 'Negative'}
    if not set(df['Overall_Impact'].dropna().unique()).issubset(clases):
        raise ValueError('El fichero tiene categorias desconocidas en Overall_Impact.')
    if exigir_version_referencia and (len(df) != 4500 or len(contenido) != LONGITUD_ESPERADA
        or git_blob_sha1(contenido) != GIT_BLOB_ESPERADO):
        raise ValueError('No es la version publica de 4.500 registros verificada previamente.')
    resumen = {
        'fuente': 'copia publica en GitHub, no descarga directa de Kaggle',
        'url_espejo': ESPEJO_URL,
        'kaggle_referencia': KAGGLE_REFERENCIA,
        'sha256_archivo_local': hashlib.sha256(contenido).hexdigest(),
        'git_blob_sha1': git_blob_sha1(contenido),
        'filas': int(len(df)), 'columnas': int(df.shape[1]),
        'nulos': {c: int(n) for c,n in df.isna().sum().items()},
        'duplicados_excluyendo_id': int(df.drop(columns=['Student_ID']).duplicated().sum()),
        'ids_unicos': int(df['Student_ID'].nunique()),
        'clases': {str(k):int(n) for k,n in df['Overall_Impact'].value_counts(dropna=False).items()}
    }
    if exigir_version_referencia:
        assert resumen['nulos']['Perceived_Stress_Score'] == 46
        assert resumen['nulos']['Academic_Performance_GPA'] == 85
        assert resumen['clases'] == {'Beneficial':3681,'Neutral':654,'Negative':165}
    return df, resumen


if __name__ == '__main__':
    import argparse
    p=argparse.ArgumentParser(description='Descarga y audita el CSV sin generar muestras artificiales')
    p.add_argument('--descargar', action='store_true')
    p.add_argument('--csv', type=Path, default=ARCHIVO_LOCAL)
    args=p.parse_args()
    if args.descargar: descargar_espejo(args.csv)
    _, resumen=cargar_y_auditar(args.csv, exigir_version_referencia=args.descargar)
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
