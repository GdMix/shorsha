import cv2
import numpy as np
from PIL import Image
from numba import prange
from colorit import background, init_colorit
import sys


cap = cv2.VideoCapture(0)

while True:
    im = cap.read()[1]
    img = Image.fromarray(im)
    img = img.resize((80,24))
    data = ""
    init_colorit()
    for y in prange(0,24):
        for x in prange(0,80):
            r,g,b = img.getpixel((x,y))
            print(background(" ",(b,g,r)),end="")
    if cv2.waitKey(1) == 27:
        break
