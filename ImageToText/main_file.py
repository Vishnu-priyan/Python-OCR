from deWarp import *
from deWarp import page_dewarp as warp
import os
import glob
import shutil
from pytessing import pytest_main
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

curr_dir = os.getcwd()

os.chdir("/home/mr/Pictures/Webcam")

#dest - Destination is where you want to place the captured Image. (in imgfiles)
dest     = "/home/mr/Programming-Python/OCRproject/ImageToText/imgfiles"

file_list = sorted(os.listdir("."))






#Change the path according to your System
for i,item in enumerate(file_list):
    shutil.move("/home/mr/Pictures/Webcam/"+item,dest+"/"+str(i)+"_image.jpg")


os.chdir(dest)

input_images = sorted(glob.glob("*.jpg"))

print(input_images)

os.chdir(curr_dir)

for file_name in input_images:
    try:    
        print("./imgfiles/{0}".format(file_name))
        warp.main("./imgfiles/{0}".format(file_name))
        #Un-comment below line to delete the files
        #os.remove("./imgfiles/{0}".format(file_name))
    except:
        print("The image: {0} cannot be loaded".format(file_name).upper())
        #Un-comment below line to delete the files
        #os.remove("./imgfiles/{0}".format(file_name))

pytest_main()




