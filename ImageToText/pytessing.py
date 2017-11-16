import argparse
from PIL import Image
import cv2
import os
import pytesseract
import glob
import para_to_words as p2w
import change_dimens as cdim

def call_at_end(res):
    '''A function that is called at last'''
    print("""
#----------------------------------------#
#     THE TEXT HAS BEEN GENERATED        #
# (Good image quality ensures accuracy)  #
#    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      #
#                                        #
#----------------------------------------#
""")
    print_text(res)
    print("-----------------------------------------------------------------")
    print("""
#----------------------------------------#
#  DO YOU WANT TO PERFORM AUTO-CORRECT?  #
#             Y/N                        #
#    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      #
#                                        #
#  Note: This may/may not                #
#            improve accuracy            #
#----------------------------------------#
""")
    print("-----------------------------------------------------------------")
    choice = str(raw_input("Enter here : "))  
    if choice.lower()=='y':
        for item in res:
            text = p2w.correct_para(' '.join(item))
            print(text)
    else:
        print("Thank you!")

def print_text(res):
    '''Prints the result list of tuples into a big text'''
    '''Also saves as a pdf file'''
    final_string = ' '    
    for item in res:
        print(' '.join(item))
        final_string+=' '.join(item)
    return final_string

def pytest_main():
    '''Main function which does tesseract OCR'''
    img_list = sorted(glob.glob("*.png"))
    text_list = []
    print(img_list)    
    for i,img_name in enumerate(img_list):

        text = pytesseract.image_to_string(Image.open(img_name))
        
        #Un-comment below line to delete the files
        #os.remove(img_name)
        
        
        text_list.append(text)

    res = cdim.change_dimen(text_list)

    call_at_end(res)
    return res

if __name__=="__main__":
    res = pytest_main()
    call_at_end(res)

