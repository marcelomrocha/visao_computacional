import cv2

classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
camera = cv2.VideoCapture(0)

# cria uma janela
cv2.namedWindow("Face", cv2.WINDOW_NORMAL)

while(True):
    conectado, imagem = camera.read()
    cv2.imshow("Face", imagem)
    cv2.waitKey(0)
camera.release()
cv2.destroyAllWindows()