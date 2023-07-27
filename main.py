import cv2
import tensorflow as tf

model = tf.keras.models.load_model("keras_model.h5")
vid = cv2.VideoCapture(0)
  
while(True):
    ret, frame = vid.read()

    cv2.imshow('quadro', frame)

    key = cv2.waitKey(1)
    
    if key == 32:
        break
  
vid.release()
cv2.destroyAllWindows()