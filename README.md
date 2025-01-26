# face-recognition
1.环境设置
  opencv的下载
  python的下载
  其他一些代码要用到的软件包的下载
  
  安装步骤
  pip install opencv-python==4.10.0.84
  pip install opencv-contrib-python==4.11.0.86
  pip install numpy==1.21.6

  我当时遇到一个报错 模拟电赛的时候也遇到了一个 最后解决办法好像都是升级了一下opencv-contrib-python （报错是什么忘记 
  了）

2.数据集准备
  目录结构
    face_recognition/
  ├── face_data/
  │   ├── me/
  │   │   └── *.jpg/png
  │   └── else/
  │       └── *.jpg/png
  ├── haarcascades/
  │   ├── *.xml

  然后运行1.py里那个代码 把我face_data文件夹下的me和else文件夹里的图片转换成灰度图并且固定尺寸200*200
   
最后就是用 人脸识别分类器：haarcascade_frontalface_default.xml 这个东西大概意思就是“从图像中提取有意义的特征并将其放入有用的表示中，然后对其进行一些分类”   总体流程就是我传入我想要识别的人脸图片（me）以及else 经过预备处理后 通过这个人脸识别分类器将输入的人脸图像与用户相关的人脸图像进行比较 以找到与该输入面相匹配的用户

问题就是识别不准 效果不好 感觉如果解决的话应该就是多传点照片进去 还有就是处理图片那里再多加工加工 还有就是换个其他的人脸识别分类器试试？

最后还有个问题就是我一开始运行那个2.py那个代码图像窗口还能跳出来 感觉我什么也没动然后后面再试的时候就窗口跳不出来了 但是我代码什么的都能正常运行
  
