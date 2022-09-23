import cv2
import mediapipe as mp
import time
import math

class poseDetector():


    def __init__(self, mode= False, modelCom = 1, upBody = False,
                 smooth =True, enSegmen = False, smoothSegmen = True,
                 detectionCon = 0.5, trackCon = 0.5):

        self.mode = mode #modeli daima yeni tanıma arar false olunca tanımadan takibe gecer
        self.modelCom = modelCom
        self.upBody = upBody
        self.smooth = smooth
        self.enSegmen = enSegmen
        self.smoothSegmen = smoothSegmen
        self.detectionCon = detectionCon
        self.trackCon = trackCon



        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.modelCom,self.upBody,
                                     self.smooth,self.enSegmen,self.smoothSegmen
                                     ,self.detectionCon,self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #bgr yi rgb a cevirme
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, #landmark cizimi
                                               self.mpPose.POSE_CONNECTIONS)


        return img
    def findPosition(self, img, draw =True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                #print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)   #cozunurluk degerlerı ıcın yukseklık ve genıslıkle carparız
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

        return self.lmList


    def aciBul(self, img, p1, p2, p3, draw=True):

        #landmarkları al

        x1, y1 = self.lmList[p1][1:]  #landmarkta ozel noktaları belirleyip cizilen noktlara arası acı bulma
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        #aciyi hesapla
        aci = math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        if aci < 0:
            aci += 360
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.line(img, (x3, y3), (x2, y2), (0, 255, 0), 3)

            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)  # cizilen landmarkların rengi boyutu
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(aci)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 0, 255))
            return aci

    def aciBulb(self, img, p1, p2, p3, draw=True):

            # landmarkları al

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        acibacak = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if acibacak < 90:
           acibacak +=360

        #print(aci)

        #ciz
        if draw:
            cv2.line(img,(x1, y1),(x2, y2),(0,255,0), 3)
            cv2.line(img,(x3, y3),(x2, y2),(0,255,0), 3)

            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)    #cizilen landmarkların rengi boyutu
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(acibacak)),(x2 - 50,y2 +50),cv2.FONT_HERSHEY_PLAIN,2,
                        (0,0,255))
        return acibacak


def main():
    cap = cv2.VideoCapture('videolar/videocurl.mp4')
    #cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    while True:
            success, img = cap.read()
            img = detector.findPose(img)
            lmList = detector.findPosition(img, draw=False)
            print(lmList[14])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 5, (0, 255, 0), cv2.FILLED)

            cTime = time.time()  #frame dusurme icin
            fps = 1 / (cTime - pTime)
            pTime = cTime

            cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 0), 3)
            cv2.imshow("Image", img)
            cv2.waitKey(1)


if __name__ == "__main__":
    main()