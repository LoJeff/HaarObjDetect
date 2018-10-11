
import numpy as np
import cv2

#--cascades example--
face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_alt2.xml')
cat_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalcatface.xml')
#face_cascade = cv2.CascadeClassifier('lbp/lbpcascade_frontalface_improved.xml')
#cat_cascade = cv2.CascadeClassifier('lbp/lbpcascade_frontalcatface.xml')

#baseball_cascade = cv2.CascadeClassifier('haar/haarcascade_baseball.xml')

def init_video():
    cv2.namedWindow("cam")
    vc = cv2.VideoCapture(2)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
        frame = None

    return vc, rval, frame

if __name__ == "__main__":
    vc, rval, frame = init_video()

    while rval:
        rval, frame = vc.read()
        
        #--Drawing and detecting code example--
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)

        cats = cat_cascade.detectMultiScale(gray)
        for (x, y, w, h) in cats:
            frame = cv2.circle(frame, (int(x+w/2), int(y+h/2)), int((w+y)/2), (0, 255, 0), 2)

        cv2.imshow("cam", gray)

        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
        elif key == ord('w'):
            num += 1
        elif key == ord('s'):
            num -= 1

    cv2.destroyAllWindows()