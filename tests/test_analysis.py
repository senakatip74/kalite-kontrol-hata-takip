"""Hata türlerine göre analiz testleri."""
import tempfile
import unittest
from pathlib import Path

from analysis import summarize_defects
from storage import create_defect


class AnalysisTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.database = Path(self.temp.name) / "test.db"

    def tearDown(self):
        self.temp.cleanup()

    def test_grouping_three_defect_types(self):
        create_defect("A", "Çizik", "Yüzey", 2, self.database)
        create_defect("B", "Çizik", "Kenar", 3, self.database)
        create_defect("C", "Ölçü hatası", "Boyut", 4, self.database)
        create_defect("D", "Renk hatası", "Boya", 1, self.database)
        rows = summarize_defects(self.database)
        totals = {row["error_type"]: row["total_quantity"] for row in rows}
        self.assertEqual(totals, {"Çizik": 5, "Ölçü hatası": 4, "Renk hatası": 1})
        self.assertEqual(sum(row["record_count"] for row in rows), 4)

    def test_empty_database(self):
        self.assertEqual(summarize_defects(self.database), [])


if __name__ == "__main__":
    unittest.main()
