import sys, tempfile, unittest
from pathlib import Path
import pandas as pd

MODULE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE))
from fuente_auditoria import COLUMNAS, cargar_y_auditar

class FuenteTest(unittest.TestCase):
    def setUp(self):
        self.fixture=MODULE/'tests'/'muestra_publica_17.csv'
    def test_esquema_y_auditoria(self):
        d,a=cargar_y_auditar(self.fixture)
        self.assertEqual(d.shape,(17,16))
        self.assertEqual(list(d.columns),COLUMNAS)
        self.assertEqual(a['ids_unicos'],17)
    def test_falta_csv_no_genera_datos(self):
        with self.assertRaises(FileNotFoundError):
            cargar_y_auditar(MODULE/'no_existe.csv')
    def test_cambio_esquema_rechazado(self):
        d=pd.read_csv(self.fixture).drop(columns=['Overall_Impact'])
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'bad.csv';d.to_csv(p,index=False)
            with self.assertRaises(ValueError):cargar_y_auditar(p)
    def test_id_duplicado_rechazado(self):
        d=pd.read_csv(self.fixture)
        d.loc[1,'Student_ID']=d.loc[0,'Student_ID']
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'dup.csv';d.to_csv(p,index=False)
            with self.assertRaises(ValueError):cargar_y_auditar(p)

if __name__=='__main__':unittest.main()
