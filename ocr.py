import os
import argparse
from PIL import Image, ImageEnhance
from pytesseract import image_to_string

from tqdm import tqdm


def ocr(image_file):
    # function parses the images into text
    img = Image.open(image_file)
    img = ImageEnhance.Brightness(img).enhance(1.1)
    img = ImageEnhance.Contrast(img).enhance(1.1)
    img = img.resize((img.size[0]*4,img.size[1]*4), Image.ANTIALIAS)
    img = ImageEnhance.Sharpness(img).enhance(2.0)
    text = image_to_string(img)
    return text


def main(dir_):
    # function pulls in files from directory and uses ocr to convert all files into text
    files = os.listdir(dir_)
    pic_extensions = ['jpg', 'png', 'gif', 'svg', 'jpeg', 'eps', 'ico', 'tiff']
    picture_files = [dir_ + '/' + x for x in files if x.lower().split('.')[-1] in pic_extensions]
    txt = ''

    for picture in tqdm(picture_files, desc='parsing files'):
        txt = txt + '\n' + ocr(picture)

    return txt


def write_out(o_file, text):
    with open(o_file, 'wb') as fi:
        fi.write(words.encode('utf-8'))


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='cli OCR tool')
    parser.add_argument('directory', metavar='dir', type=str,
                        help='directory in which text images are located')
    parser.add_argument('outputfile', metavar='outputfile', type=str,
                        help='file (+path) where output text file will be stored')

    args = parser.parse_args()

    words = main(args.directory)
    write_out(args.outputfile, words)

    
