import cv2
import numpy as np
import imutils
import os

path = "./kait_img_crop"
file_list = os.listdir(path)
print("file_list: {}".format(file_list))
#print(len(file_list))

i=0
count = 0

while True:
    
    #Read image
    #im = cv2.imread("batch_applefile_17896339_1.jpg")
    im = cv2.imread("./kait_img_crop/"+ file_list[i])

    i=i+1
    if i==10236:
        break

    #cv2.imshow('input image', im)
    #cv2.waitKey(0)

    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    img2 = 255-gray
    img3 = cv2.GaussianBlur(img2, (5, 5), 0)



    #cv2.imshow('input image',gray)
    #cv2.waitKey(0)

    edged=cv2.Canny(img3,30,200)
    #cv2.imshow('canny edges',edged)
    #cv2.waitKey(0)

    #_, contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #cnts = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cnts = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    #print(len(cnts))
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
    

        if not (400 < w < 1300 and 400 < h < 1200):
            #print("skip " + str(w) + " - " + str(h))
            continue
        
        #저장된 이미지에 상자 그린거는 없어야할듯그래서 주석처리함
        #cv2.rectangle(im,(x,y),(x+w,y+h),(3,255,4),2)

        #cv2.rectangle(image,(x,y),(x+w,y+h),(3,255,4),2)
        #cv2.imshow("image",im)
        #cv2.waitKey(0)
    
        count = count+1
        cv2.imwrite("output/Img"+str(count)+".jpg", im[y: y + h, x: x + w])


    cv2.destroyAllWindows





