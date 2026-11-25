import sys
import unittest
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fuente_auditoria import cargar_y_auditar
from integracion_contextual import COLUMNAS_CONTEXTO, integrar_contexto
from seleccion_normalizacion import seleccionar_y_normalizar


class IntegracionTest(unittest.TestCase):
    def setUp(self):
        d, _ = cargar_y_auditar(ROOT / "tests" / "muestra_publica_17.csv")
        self.base = seleccionar_y_normalizar(d)

    def test_left_join_y_ambito(self):
        final, stats = integrar_contexto(self.base)
        self.assertEqual(len(final), len(self.base))
        self.assertEqual(stats["filas_entrada"], stats["filas_salida"])
        self.assertEqual(len(final.columns), len(self.base.columns) + 3)
        self.assertEqual(final.loc[0, "INE_Redes_Sociales_Participacion_Pct_2025"], 69.5)
        self.assertEqual(final.loc[0, "SIIU_Nota_Expediente_Grado_10_2024_25"], 7.42)
        self.assertTrue(pd.isna(final.loc[0, "ESTUDES_RRSS_Uso_Problematico_Pct_2025"]))
        # 17 anos, sexo Female, High School: dato agregado OEDA = 15.1%, no riesgo individual
        self.assertEqual(final.loc[2, "ESTUDES_RRSS_Uso_Problematico_Pct_2025"], 15.1)
        for col in COLUMNAS_CONTEXTO:
            self.assertIn(col, final.columns)

    def test_grupo_fuera_del_ambito_na(self):
        b = self.base.copy(deep=True)
        b.loc[0, "Age"] = 15
        b.loc[0, "Academic_Level"] = "Postgrad"
        final, _ = integrar_contexto(b)
        self.assertTrue(pd.isna(final.loc[0, "INE_Redes_Sociales_Participacion_Pct_2025"]))
        self.assertTrue(pd.isna(final.loc[0, "SIIU_Nota_Expediente_Grado_10_2024_25"]))
        self.assertTrue(pd.isna(final.loc[0, "ESTUDES_RRSS_Uso_Problematico_Pct_2025"]))

    def test_base_intacta(self):
        before = self.base.copy(deep=True)
        integrar_contexto(self.base)
        pd.testing.assert_frame_equal(self.base, before)


if __name__ == "__main__":
    unittest.main()
