"""Punto de entrada del Modulo 1 para el equipo de Mineria de Datos."""
from __future__ import annotations
from pathlib import Path
import argparse
import json
from fuente_auditoria import ARCHIVO_LOCAL, descargar_espejo, cargar_y_auditar
from seleccion_normalizacion import seleccionar_y_normalizar, variables_predictoras, OBJETIVOS
from integracion_contextual import integrar_contexto, COLUMNAS_CONTEXTO


def ejecutar(csv:Path, destino:Path, *, version_publica=False):
    datos, auditoria = cargar_y_auditar(csv, exigir_version_referencia=version_publica)
    base=seleccionar_y_normalizar(datos)
    contexto, integracion=integrar_contexto(base)
    if list(base.columns)!=list(datos.columns.drop('Student_ID')):
        raise AssertionError('El orden de columnas normalizado ha cambiado inesperadamente')
    destino=Path(destino); destino.mkdir(parents=True,exist_ok=True)
    base.to_csv(destino/'modulo1_base_normalizada.csv',index=False)
    contexto.to_csv(destino/'modulo1_contexto_solo_exploratorio.csv',index=False)
    evidencias={
       'autor':'Abdelmouiz kobry',
       'modulo':'Seleccion e integracion de informacion',
       'auditoria':auditoria,'integracion':integracion,
       'objetivos':list(OBJETIVOS), 'variables_predictoras_sin_contexto':variables_predictoras(base),
       'variables_externas_no_predictoras':list(COLUMNAS_CONTEXTO),
       'advertencia':'La procedencia del muestreo de Kaggle no ha podido certificarse. Los indicadores agregados espanoles no corresponden a los mismos individuos; no permiten prediccion causal.'
    }
    (destino/'evidencias_modulo1.json').write_text(json.dumps(evidencias,ensure_ascii=False,indent=2),encoding='utf-8')
    return evidencias


if __name__=='__main__':
    p=argparse.ArgumentParser(description='Prepara los datos del Modulo 1 sin sustituciones artificiales')
    p.add_argument('--descargar',action='store_true',help='Descarga y verifica el espejo publico antes de procesar')
    p.add_argument('--csv',type=Path,default=ARCHIVO_LOCAL)
    p.add_argument('--salida',type=Path,default=Path(__file__).resolve().parent.parent/'outputs')
    args=p.parse_args()
    if args.descargar: descargar_espejo(args.csv)
    res=ejecutar(args.csv,args.salida,version_publica=args.descargar)
    print(f"OK: {res['auditoria']['filas']} filas, {res['auditoria']['columnas']} columnas originales")
    print(f"Cobertura contextual: {res['integracion']['cobertura']}")
