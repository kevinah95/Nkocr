import unittest
from src.ocr_table import OCRTable


class TestTable(unittest.TestCase):
    
    def test_of_tests(self):
        self.assertTrue(True)

    def test_image_processing(self):
        text = OCRTable("test/ocr.png",False)
        type_output = isinstance(text,str)
        self.assertTrue(type_output)