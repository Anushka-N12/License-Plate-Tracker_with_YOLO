# import cv2 as cv
import os
import numpy as np
from bs4 import BeautifulSoup

mainpath = r'C:\Users\anush\Downloads'

def yoloformat(file, filepath):
    with open(filepath, 'r') as f:
        fdata = f.read()
    xmldata = BeautifulSoup(fdata, "xml")
    
    xmin = int(xmldata.find('xmin').text)
    ymin = int(xmldata.find('ymin').text)
    xmax = int(xmldata.find('xmax').text)
    ymax = int(xmldata.find('ymax').text)
    width = int(xmldata.find('width').text)
    height = int(xmldata.find('height').text)
        # xmin, ymin, xmax, ymax
    x = ((xmax + xmin) / 2) / width
    y = ((ymax + ymin) / 2) / height
    w = (xmax - xmin) / width
    h = (ymax - ymin) / height
    return [x, y, w, h]

def cvrtfolder(folder):
    folderpath = os.path.join(mainpath, folder)
    for file in os.listdir(folderpath):
        filepath = os.path.join(folderpath, file)
        name = os.path.basename(filepath).split('/')[-1]
        if name.endswith('.xml'):
            yolof = yoloformat(file, filepath)
            os.remove(filepath)
            with open(os.path.join(folderpath, name[:-4]+'.txt'), 'w') as f:
                text = " ".join([str(x) for x in yolof])
                f.write(f'0 {text}')
    return f'{folder} updated!'

print(cvrtfolder('d1'))
print(cvrtfolder('d2'))

# I downloaded 3 datasets from links below and am putting them all into one format
# 1 - https://www.kaggle.com/datasets/mykaggle193/license-plate-annotation-xml?select=LPs+XML+annotation
# 2 - https://www.kaggle.com/datasets/aslanahmedov/number-plate-detection
# 3 - https://www.kaggle.com/datasets/andrewmvd/car-plate-detection

# imgpath = r'C:\Users\anush\Downloads\LPD\images'
# for img in os.listdir(imgpath):
#     path = os.path.join(imgpath, img)
#     image = cv.imread(path)
#     name = os.path.basename(path).split('/')[-1]
#     c = coordinates(name[:-4]+'.xml')
#     print(c)
#     cv.rectangle(image, (c[0],c[1]), (c[0]+c[2],c[1]+c[3]), (0,255,0), thickness=2)
#     cv.imshow('LP', image)
#     cv.waitKey(0)
#     if cv.waitKey(0) & 0xFF == ord('d'):  
# 	    break