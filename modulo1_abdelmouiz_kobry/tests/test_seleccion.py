import sys, unittest
from pathlib import Path
import pandas as pd
MODULE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(MODULE))
from fuente_auditoria import cargar_y_auditar
from seleccion_normalizacion import seleccionar_y_normalizar, variables_predictoras

class SeleccionTest(unittest.TestCase):
    def test_seleccion_conserva_filas_y_targets(self):
        raw,_=cargar_y_auditar(MODULE/'tests'/'muestra_publica_17.csv')
        d=seleccionar_y_normalizar(raw)
        self.assertEqual(d.shape,(17,15))
        self.assertNotIn('Student_ID',d.columns)
        self.assertIn('Academic_Performance_GPA',d.columns)
        self.assertIn('Overall_Impact',d.columns)
        self.assertNotIn('Academic_Performance_GPA',variables_predictoras(d))
        self.assertNotIn('Overall_Impact',variables_predictoras(d))
        self.assertIn('Undergrad',set(d['Academic_Level'].dropna()))
        self.assertIn('Often',set(d['Social_Comparison_Frequency'].dropna()))
        self.assertIn('X',set(d['Primary_Platform'].dropna()))
    def test_nulos_no_se_imputan(self):
        raw,_=cargar_y_auditar(MODULE/'tests'/'muestra_publica_17.csv')
        raw.loc[0,'Perceived_Stress_Score']=float('nan')
        d=seleccionar_y_normalizar(raw)
        self.assertTrue(pd.isna(d.loc[0,'Perceived_Stress_Score']))
    def test_no_mutacion(self):
        raw,_=cargar_y_auditar(MODULE/'tests'/'muestra_publica_17.csv')
        before=raw.copy(deep=True)
        _=seleccionar_y_normalizar(raw)
        pd.testing.assert_frame_equal(raw,before)

if __name__=='__main__':unittest.main()
