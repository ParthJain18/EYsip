import cv2
from ocr import extract_text_from_image


cap = cv2.VideoCapture('team1.mp4')

if not cap.isOpened():
    print("Error opening video file")

i = 0

while (cap.isOpened()):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()

    if ret == True:
        i += 30

        frame = frame[220: 260, 385: 1000]
        frame = cv2.rectangle(frame, (5,7), (900, 35),(0, 255, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        text = extract_text_from_image(frame, config='--psm 7')
        # text = "example \n"

        # cv2.imwrite("debug.jpg", frame)
        seconds = round(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)

        with open("log_team_1(1).txt", 'a') as file:
            file.writelines(str(seconds) + ", " + text)


    else:
        break

cap.release()
