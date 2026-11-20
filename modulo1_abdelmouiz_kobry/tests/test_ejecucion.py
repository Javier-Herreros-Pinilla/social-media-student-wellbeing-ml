import sys, unittest, tempfile
from pathlib import Path
import json
MODULE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(MODULE))
from ejecutar_modulo1 import ejecutar
from integracion_contextual import COLUMNAS_CONTEXTO

class EjecucionTest(unittest.TestCase):
    def test_salidas_controladas(self):
        with tempfile.TemporaryDirectory() as td:
            info=ejecutar(MODULE/'tests'/'muestra_publica_17.csv',Path(td))
            self.assertEqual(info['auditoria']['filas'],17)
            self.assertEqual(info['integracion']['filas_salida'],17)
            self.assertTrue((Path(td)/'modulo1_base_normalizada.csv').is_file())
            self.assertTrue((Path(td)/'modulo1_contexto_solo_exploratorio.csv').is_file())
            self.assertTrue((Path(td)/'evidencias_modulo1.json').is_file())
            saved=json.loads((Path(td)/'evidencias_modulo1.json').read_text(encoding='utf-8'))
            self.assertFalse(set(COLUMNAS_CONTEXTO)&set(saved['variables_predictoras_sin_contexto']))

if __name__=='__main__':unittest.main()
