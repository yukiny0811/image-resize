import glob
import cv2
import numpy as np
import random
import string
import tqdm
import math

s = 512 #クロップする大きさ

files = glob.glob("./images/*g")

for file in tqdm.tqdm(files):
    img = cv2.imread(str(file))
    w, h, ch = img.shape
    if w > h:
        ratio = s / h
        im_resized = cv2.resize(img, dsize=None, fx=ratio, fy=ratio)
        rw, rh, rch = im_resized.shape
        fro = int((rw - s) / 2)
        cropped = im_resized[fro:rw-fro,:]
        cv2.imwrite("./processed/" + str(file)[9:], cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    else:
        ratio = s / w
        im_resized = cv2.resize(img, dsize=None, fx=ratio, fy=ratio)
        rw, rh, rch = im_resized.shape
        fro = int((rh - s) / 2)
        print(fro)
        cropped = im_resized[:,fro:rh-fro]
        cv2.imwrite("./processed/" + str(file)[9:], cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 100])