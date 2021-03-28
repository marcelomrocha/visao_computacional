import cv2

#Reading the image from local disk
img = cv2.imread("celo_cavaco.jpg")

#Resizing image to small size
img = cv2.resize(img,(420,300))
cv2.namedWindow("output", cv2.WINDOW_NORMAL)       
cv2.imshow("output",img)
cv2.resizeWindow('output', 400,400)
cv2.waitKey(0)
cv2.destroyAllWindows()