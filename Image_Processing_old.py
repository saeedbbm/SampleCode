import cv2
import pickle
import time
from PyQt5.QtCore import QTimer
import os

class image_processor():

    def __init__(self):
        super().__init__()
        self.upFolder = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        self.Flag_showResult=False
        self.timer = QTimer()

        # load face cascade classifier
        self.face_cascade = cv2.CascadeClassifier(self.upFolder + '/haarcascade_frontalface_default.xml')

        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.color = (255, 255, 255)
        self.stroke = 3

        self.PublicID2 = 1001
        self.labels = {}
        with open(self.upFolder + "/labels.pickle", "rb") as f:
            org_labels = pickle.load(f)
            self.labels = {v: k for k, v in org_labels.items()}

        self.ct = 1
        self.NumfacePic = 0
        self.NummotionPic = 0
        self.NumcapturedPic = 0
        
        self.FacePicSignal = 0
        self.MotionPicSignal = 0
        self.OperatorPicSignal = 0
        
        self.NumcapturedVid1 = 0
        self.NumcapturedVid2 = 0
        
        self.ret1 = False
        self.ret2 = False

        self.timer.timeout.connect(self.getFrame1)
        time.sleep(0.2)
        self.timer.timeout.connect(self.getFrame2)

    def capture_frame(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.start(20)

    def getFrame1(self):
        self.ct += 1
        self.ret = self.cap.grab()
        if self.ct % 1 == 0: # skip some frames
            self.ret1, self.frame1 = self.cap.retrieve()

    def getFrame2(self):
        self.ret = self.cap.grab()
        self.ret2 = False
        if self.ct % 1 == 0: # skip some frames
            self.ret2, self.frame2 = self.cap.retrieve()

    def capturedPic(self,position):
        self.NumcapturedPic +=1
        name = self.upFolder +'/'+str(self.PublicID3+1)+ '.jpg'
        cv2.imwrite(name,self.frame1)
        self.OperatorPicSignal = 1

    def capturedVid_Start(self):
        if self.NumcapturedVid2 == 0:
            self.NumcapturedVid1 +=1
            nameVid = self.upFolder + '/'+str(self.NumcapturedVid1) + '.avi'
            height, width, channel = self.frame1.shape
            self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.out = cv2.VideoWriter(nameVid, self.fourcc, 5, (width,height))
            self.NumcapturedVid2 = 1
        self.out.write(self.frame1)

    def capturedVid_End(self):
        self.NumcapturedVid2 = 0
        self.out.release()

    # detect face
    def detectFaces(self):

        # convert frame to GRAY format
        gray = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)

        # detect rect faces
        face_rects = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        # for all detected faces
        for (x, y, w, h) in face_rects:
            # draw green rect on face
            cv2.rectangle(self.frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(self.frame1, "Unknown", (x, y - 6), self.font, 2, self.color, self.stroke, cv2.LINE_AA)

#             roi_gray = gray[y:y + h, x:x + w]
#             id_, conf = self.face_recognizer.predict(roi_gray)
#             if conf >= 45 and conf <= 85:
#                 # print(id_)
#                 # print(labels[id_])
#                 # print(conf)
#                 name = self.labels[id_]
#                 # else:
#                 #     name = "Unknown"
# 
#                 # name = labels[id_]
#                 cv2.putText(self.frame1, name, (x, y - 6), self.font, 2, self.color, self.stroke, cv2.LINE_AA)

            self.NumfacePic += 1
            self.PublicID2 +=1
            name = self.upFolder + str(self.PublicID2) + '.jpg'
            cv2.imwrite(name, self.frame1)
            self.FacePicSignal = 1

    def detectMotion(self):
        diff = cv2.absdiff(self.frame1, self.frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # blur = cv2.GaussianBlur(gray, (51, 51), 0)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # blur = gray

        _, thresh = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            if cv2.contourArea(contour) < 700:
                continue
            else:
                cv2.rectangle(self.frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                self.NummotionPic +=1
                self.PublicID2 +=1
                name = self.upFolder + str(self.PublicID2) + '.jpg'
                cv2.imwrite(name,self.frame1)
                self.MotionPicSignal = 1

    def checkOption(self,motionCheck,faceCheck):

        self.Flag_showResult = False

        if self.ret1 and self.ret2:
            if motionCheck & faceCheck:
                self.detectFaces()
                self.detectMotion()
                self.Result()
                self.Flag_showResult = True
            elif motionCheck:
                self.detectMotion()
                self.Result()
                self.Flag_showResult = True
            elif faceCheck:
                self.detectFaces()
                self.Result()
                self.Flag_showResult = True
            else:
                self.Result()
                self.Flag_showResult = True

        return self.Flag_showResult

    def Result(self):
        return self.frame1

