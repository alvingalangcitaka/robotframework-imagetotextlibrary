import os
from ImageToTextLibrary.Keywords import Keywords
from ImageToTextLibrary.version import VERSION

__version__ = VERSION


class ImageToTextLibrary(Keywords):
    """ImageToTextLibrary is robotframework keyword library to obtain text in an image

            = Prerequisite =

            The library uses Tesseract to convert the image into text.
            The machine has to be able to execute command `tesseract`.
            Follow the installation link : https://github.com/tesseract-ocr/tesseract
        
        """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        pass
