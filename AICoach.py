import cv2
import numpy as np
import time
import PoseModule as pm



#cap = cv2.VideoCapture("videolar/squat1.mov") #video konumu
#cap = cv2.VideoCapture("videolar/videocurl.mp4") #video konumu
#cap = cv2.VideoCapture("videolar/benchpress.mp4") #video konumu
cap = cv2.VideoCapture(0) #video kamera

detector = pm.poseDetector()
say1 = 0
say2 = 0
yon1 = 0
yon2 = 0
say3 = 0
say4 = 0
yon3 = 0
yon4 = 0
pTime=0
stage = None
case=input("KAMERANIZI BAŞLATILIYOR POZISYON ALIP SEÇİM YAPINIZ :\nSquat(bacak için '1' e basınız\nDumbell(kol) için = '2'ye basınız")
if case == '1' or case== '2':
    if case == '1':
        while True:
            success, img = cap.read()  # videoyu okuma
            img = cv2.resize(img, (1280, 720))  # cozunurluk
            # img = cv2.imread("videolar/dips.jpeg")
            img = detector.findPose(img, True)
            lmList = detector.findPosition(img, draw=False)  # false sadece koldaki linelara odaklanıyor
            # print(lmList)
            if len(lmList) != 0:
                # sag bacak
                aci3 = detector.aciBulb(img, 24, 26, 28)  # mediapipe pose cizelgeseine gore sağ bacak
                per3 = np.interp(aci3, (200, 310), (0, 100))
                bar1 = np.interp(aci3, (210, 310), (650, 100))

                # sol bacak
                aci4 = detector.aciBulb(img, 23, 25, 27)  # mediapipe pose cizelgeseine gore sol bacak
                per4 = np.interp(aci4, (200, 310), (0, 100))
                bar2 = np.interp(aci4, (210, 310), (6520, 100))
                renk1 = (0, 255, 0)
                if per3 == 100:  #eger yüzde 100 rengi değiştir
                    renk1 = (255, 0, 255)
                    if yon3 == 0:
                        say3 += 0.5
                        yon3 = 1
                if per3 == 0:
                    renk1 = (0, 255, 0)
                    if yon3 == 1:
                        say3 += 0.5
                        yon3 = 0
                print(say1)
                if per4 == 100:  #barın rengini değişstir
                    renk2 = (255, 0, 255)
                    if yon4 == 0:
                        say4 += 0.5
                        yon4 = 1
                if per4 == 0:
                    renk2 = (0, 255, 0)
                    if yon4 == 1:
                        say4 += 0.5
                        yon4 = 0


                #bacak squat

                # bar cizim

            renk3 = (255, 255, 100)

            cv2.rectangle(img, (1100, 100), (1175, 650), renk1, 3)

            cv2.rectangle(img, (1100, int(bar1)), (1175, 650), renk1, cv2.FILLED)
            cv2.rectangle(img, (1100, int(bar2)), (1175, 650), renk1, cv2.FILLED)
            cv2.putText(img, f'{int(per4)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        renk3, 4)
            # curl sayma cizimi


            # curl sayma cizimi
            cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(say3 + say4)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 12,
                        (255, 0, 0), 25)

            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

            cv2.imshow("Goruntu", img)
            cv2.waitKey(1)
    else:
        while True:
            success, img = cap.read()  # videoyu okuma
            img = cv2.resize(img, (1280, 720))  # cozunurluk
            # img = cv2.imread("videolar/dips.jpeg")
            img = detector.findPose(img, True)
            lmList = detector.findPosition(img, draw=False)  # false sadece koldaki linelara odaklanıyor
            # print(lmList)
            if len(lmList) != 0:

                # sağ kol
                aci1 = detector.aciBul(img, 12, 14, 16)
                per1 = np.interp(aci1, (200, 310), (0, 100))
                bar1 = np.interp(aci1, (210, 310), (650, 100))  # mediapipe pose cizelgeseine gore sağ kol
                # sol
                aci2 = detector.aciBul(img, 11, 13, 15)
                per2 = np.interp(aci2, (200, 310), (0, 100))
                bar2 = np.interp(aci2, (210, 310), (650, 100))

                # print(aci,per)

                # dumbell curlu kontrol et
                #barın percentege değerleri ve sayma

                renk1 = (0, 255, 0)
                if per1 == 100:
                    renk1 = (255, 0, 255)
                    if yon1 == 0:
                        say1 += 0.5
                        yon1 = 1
                if per1 == 0:
                    renk1 = (0, 255, 0)
                    if yon1 == 1:
                        say1 += 0.5
                        yon1 = 0
                print(say1)
                if per2 == 100:
                    renk2 = (255, 0, 255)
                    if yon2 == 0:
                        say2 += 0.5
                        yon2 = 1
                if per2 == 0:
                    renk2 = (0, 255, 0)
                    if yon2 == 1:
                        say2 += 0.5
                        yon2 = 0



                print(say2)
                # bar cizim
                renk3 = (255, 255, 100)
                cv2.rectangle(img, (1100, 100), (1175, 650), renk1, 3)

                cv2.rectangle(img, (1100, int(bar1)), (1175, 650), renk1, cv2.FILLED)
                cv2.rectangle(img, (1100, int(bar2)), (1175, 650), renk1, cv2.FILLED)
                cv2.putText(img, f'{int(per1 + per2)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                            renk3, 4)

                # curl sayma cizimi


                # curl sayma cizimi
                cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, str(int(say2 + say1)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                            (255, 0, 0), 25)


            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 5)

            cv2.imshow("Goruntu", img)
            cv2.waitKey(1)
else:
    print("Squat için 1 \nDumbell Curl için 2 \nbasmanız gerek yeniden başlatınız.")
