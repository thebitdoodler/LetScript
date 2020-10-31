# This script hides text behind any media file like jpg, png, mp3, wav, etc.
# This script accepts two parameter for hiding text and one parameter for finding text.
# Please install steganography python library by - pip install -r steganography
# This script is compatible with python 2.7

from import absolute_import, unicode_literals
import argparse
from steganography.stegonography import Steganography

parser=argparse.ArgumentParser()
parser.add_argument("--carrier",help="To give path of carrier file which will contain the text.")
parser.add_argument("--stego_text",help="To enter the text to hide.")
parser.add_argument("--stego_find",help="To give path of image which contains hidden text.")
args=parser.parse_args()

# Function for hide the message
def hideText(carrier_path,secret_text):
    path=carrier_path
    output_path="stego.png"
    text=secret_text
    Steganography.encode(path,output_path,text)

# Function for finding and detecting steganography
def findText(steg_img):
    secret_text=Stegonography.decode(steg_img)
    print "Hidden text found :: "+secret_txt

if args.carrier:
    carriur_path=arg.carrier
    if args.stego_text:
        secret_text=args.stego_text
    hideText(carrier_path,secret_text)

if args.stego_hide:
    steg_img=args.stego_find
    findText(steg_jpg)
