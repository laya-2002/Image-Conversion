import cv2 
img=cv2.imread('img1.png')
cv2.imshow('Given image',img)
cv2.waitKey(0)
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('Converted image',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()