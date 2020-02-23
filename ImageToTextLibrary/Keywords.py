import pytesseract as Tess
from PIL import Image
from distutils.spawn import find_executable

class Keywords():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def get_text_from_image(self, image_file_path):
        """
        Get text of an image

        Args:
         - image_file_path - the absolute path of the image

        Usage:
        | ${text}= | Get Text From Image | ${CURDIR}/doc/robot/sample-image.png |
        """
        if not image_file_path:
            raise Exception('Parameter image_file_path is required')

        if not find_executable("tesseract"):
            raise Exception('"tesseract" is not found\n'
                            'Tesseract installation is required. see: https://github.com/tesseract-ocr/tesseract')
        img = Image.open(image_file_path)
        text = Tess.image_to_string(img)
        return text
