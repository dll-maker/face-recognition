import os
import sys
import cv2
import numpy as np

names=['me','else']
path = "D:/face_recognition/face_data"
cascade = 'D:/face_recognition/haarcascades/haarcascade_frontalface_default.xml'

c = 0
x, y = [], []
for dirname, dirnames, filenames in os.walk(path):
    print(f"读取人脸数据库:{dirname}")
    for subdirname in dirnames:
        subject_path = os.path.join(dirname, subdirname)
        for filename in os.listdir(subject_path):
            try:
                if (filename == ".directory"):
                    continue
                filepath = os.path.join(subject_path, filename)
                im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                if (im is None):
                    print("image " + filepath + " is none")
                else:
                    print(filepath)
                x.append(np.asarray(im, dtype=np.uint8))
                y.append(c)
            except IOError as e:  # python2到python3的修改
                print("I/O error({0}): {1}".format(e.errno, e.strerror))  # python2到python3的修改
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise
        c = c + 1
print("done!")

y = np.asarray(y, dtype=np.int32)
model = cv2.face.EigenFaceRecognizer_create()
model.train(np.asarray(x), np.asarray(y))
camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cascade)

while (True):
    read, img = camera.read()
    faces = face_cascade.detectMultiScale(img, 1.1, 5)#        print('faces的数据为：',faces)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        roi = gray[x:x + w, y:y + h]
        try:
            roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
            print(roi.shape)
            params = model.predict(roi)
            print("Label: %s, Confidence: %.2f" % (params[0], params[1]))
            cv2.putText(img, names[params[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            if (params[0] == 1):
                cv2.imwrite('face_rec.jpg', img)
                break
        except:
            continue
        cv2.imshow("camera", img)
        if cv2.waitKey(1) & 0xff == ord("q"):  # 修改
            break
cv2.destroyAllWindows()