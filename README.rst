Image to Text Robotframework Library
====================================

Introduction
------------
Image to Text Library is a robotframework keyword library to convert image to text.
It uses `tesseract` to convert the image to text.

Installation
------------

1. Install Tesseract
''''''''''''''''''''
The library needs `tesseract` to be installed first.

Follow the installation here: https://github.com/tesseract-ocr/tesseract

2. Install the python package
'''''''''''''''''''''''''''''
The recommended installation method is using
`pip <http://pip-installer.org>`__::

    pip install robotframework-imagetotextlibrary


**or**

Using `setup.py`. Execute commands bellow :

::

    git clone https://github.com/alvingalangcitaka/robotframework-imagetotextlibrary.git
    cd robotframework-imagetotextlibrary
    python setup.py install


Keyword Documentation
---------------------
The keyword documentation can be found here.

Example
-------

::

    *** Setting ***
    Library     ImageToTextLibrary
    Library     BuiltIn

    *** Test Cases ***
    Get Image Text Example
        ${text}=            Get Text From Image         ${CURDIR}/sample-image.png
        Log                 ${text}
        Should Contain      ${text}                     Directory Layout



Directory Layout
----------------
demo/
    A simple demonstration, with an image and `Log` from BuiltIn Robotframework library.

doc/
    Keyword documentation

ImageToTextLibrary/
    Python source code

Contributing
-------------
The project is in development phase, any functionality / test contribution is highly appreciated.
Fork the project, make a change, and send a pull request.