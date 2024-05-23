import cv2
import numpy as np
img = np.ones((512,512,3),np.uint8)
#img=img*240
img[:]=0,255,150
print(img)
cv2.line(img,(256,256),(512,512),(0,0,0),10)
#cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),5)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),7)
cv2.circle(img,(150,200),30,(255,50,0),5)
#cv2.putText(img," OPENCV  ",(300,200),cv2.FONT_HERSHEY_PLAIN,3,(0,150,0),3
cv2.imshow("Image",img)
cv2.waitKey(0)
