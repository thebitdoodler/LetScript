#!/usr/bin python3

from PIL import Image

img1 = Image.open(r'certificate.jpg')
pf = img1.convert('RGB')
pf.save(r'certificate.pdf')
