#importing opencv
import cv2

print(cv2.__version__)

#Reading the image from local disk
img = cv2.imread("celo_cavaco.jpg")

#Resizing image to small size
#img = cv2.resize(img,(420,300))

# cria uma janela
cv2.namedWindow("Janela da Imagem", cv2.WINDOW_NORMAL)

#displaying the original image
cv2.imshow("Janela da Imagem",img)

cv2.resizeWindow('Janela da Imagem', 400,400)

#applying algorithm to blur the image
img = cv2.blur(img, ksize = (10, 10))

# cria uma janela
cv2.namedWindow("Imagem com blur", cv2.WINDOW_NORMAL)

#displaying the blur image
cv2.imshow("Imagem com blur",img)

# espera por uma tecla
cv2.waitKey(0)

#fecha a janela
cv2.destroyAllWindows()