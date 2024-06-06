import cv2
from ocr import extract_text_from_image


cap = cv2.VideoCapture('team1.mp4')

if not cap.isOpened():
    print("Error opening video file")

i = 0

google_time_dict = {'1025': 45.0,
 '1090': 30.0,
 '1125': 25.0,
 '1155': 5.0,
 '1275': 15.0,
 '1295': 400.0,
 '1820': 95.0,
 '2900': 100.0,
 '5200': 45.0,
 '5445': 50.0,
 '5500': 5.0,
 '5650': 10.0,
 '5805': 105.0,
 '6330': 5.0,
 '6465': 10.0,
 '8505': 20.0,
 '10470': 20.0,
 '10640': 460.0,
 '11135': 265.0,
 '12055': 15.0,
 '12435': 100.0,
 '15760': 890.0,
 '16725': 75.0,
 '18345': 25.0,
 '18375': 5.0}


while (cap.isOpened()):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()

    if ret == True:
        i += 150

        for j in google_time_dict.keys():
            if i/30 >= int(j) and i/30 < (int(j) + int(google_time_dict[j])):

                text = extract_text_from_image(frame[250: 300, 385: 600])
                seconds = round(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)


                with open("log_google_team_1.txt", 'a') as file:
                    file.writelines(str(seconds) + ", " + text)


    else:
        break

cap.release()