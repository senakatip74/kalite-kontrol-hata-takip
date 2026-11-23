"""Hata kaydı oluşturma özelliğinin temel testleri."""
import tempfile
import unittest
from pathlib import Path
from storage import create_defect, list_defects


class DefectStorageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.database = Path(self.temp.name) / "test.db"

    def tearDown(self):
        self.temp.cleanup()

    def test_create_and_persist_defect(self):
        record_id = create_defect("Metal Parça", "Çizik", "Yüzey çizik", 2, self.database)
        records = list_defects(self.database)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["id"], record_id)
        self.assertEqual(records[0]["product_name"], "Metal Parça")
        self.assertEqual(records[0]["quantity"], 2)

    def test_invalid_blank_product_is_rejected(self):
        with self.assertRaises(ValueError):
            create_defect(" ", "Çizik", "Yüzey çizik", 1, self.database)
        self.assertEqual(list_defects(self.database), [])

    def test_invalid_quantity_is_rejected(self):
        with self.assertRaises(ValueError):
            create_defect("Metal", "Çizik", "Açıklama", 0, self.database)


if __name__ == "__main__":
    unittest.main()
