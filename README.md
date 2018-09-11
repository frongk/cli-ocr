# cli-ocr
Command Line OCR Tool

## Description
I needed to use OCR for a directory full of image files and was having a hard time finding the right tool to do it. I'm sure it exists out there already, but I though it might be nice to have a quick python cli tool to do it. Some prior image manipulation (e.g. blowing up the image, sharpening it, etc.) was needed to get the text to translate properly. This has also been automated using some tools in the Python Image Library (PIL). 

## Usage
To use, add all of the image files you want to translate into a directory. This tool is intended to run ocr for multiple files when the files are named sequentially. For example, if you have an images of the pages of a book, to use the tool to get text for the book, you would want to name the images something intuitive and sequential like: `page01.png`, `page02.png`, `page03.png`, etc.

If you don't want to set it up a path/make an alias for the `ocr.py` file, the easiest way to run it is:
```
python dir1/dir2/.../ocr.py directory_with_image_files dirA/dirB/.../output_text_file.txt
```

To test this out, use the images in the `testfiles` directory when your terminal is in the cli-ocr directory. 
```
python ocr.py testfiles testfiles/sampleoutput.txt
```

## Main Dependencies
`tesseract`- https://github.com/tesseract-ocr/tesseract (make sure to update your PATH to include it)
`pytesseract` - `pip install pytesseract` (https://pypi.org/project/pytesseract/)
`PIL` - Python Image Library (https://pillow.readthedocs.io/en/5.2.x/)  
`tqdm` - status bars are nice (https://github.com/tqdm/tqdm)
