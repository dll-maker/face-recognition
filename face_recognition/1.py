import cv2
import glob

dir_path = "D:/face_recognition/face_data/else"
save_path = "D:/face_recognition/face_data/else/%s.pgm"
image_height = 200
image_width = 200
directory_path = dir_path + "/*.jpg"
files = glob.glob( directory_path )   #得到该类别样本路径下的所有文件名
print(files)
count = 0
for f in files:
    print(f)
    image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)    #在stranger_facedata里面读取的数据有灰度的也有彩色的
    image = cv2.resize( image, (image_width, image_height) )
    print(image.shape)#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite( save_path % str(count), image)
    count += 1