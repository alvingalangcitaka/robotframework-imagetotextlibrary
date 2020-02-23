import unittest
import os
from ImageToTextLibrary.Keywords import Keywords


class KeywordsTests(unittest.TestCase):
    def test_get_text_from_image_success(self):
        keywords = Keywords()
        resultText = keywords.get_text_from_image('sample-image.png')
        self.assertTrue(self, resultText is not None)

    def test_get_text_from_image_empty_image_path(self):
        keywords = Keywords()
        self.assertRaises(Exception, keywords.get_text_from_image, '')

    def test_get_text_from_image_no_tesseract(self):
        existing_path = os.environ["PATH"]
        os.environ["PATH"] = ""
        keywords = Keywords()
        self.assertRaises(Exception, keywords.get_text_from_image, 'sample-image.png')
        os.environ["PATH"] = existing_path
