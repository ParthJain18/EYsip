import cv2
from ocr import extract_text_from_image
from multiprocessing import Process

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video file")

    i = 0
    seconds = 0

    while (cap.isOpened()):

        ret, frame = cap.read()

        if ret == True:
            i += 1

            if i % 150 != 0:
                continue

            text = extract_text_from_image(frame[220: 260, 385: 1000])

            with open(f"log_{video_path}.txt", 'a') as file:
                file.writelines(str(seconds) + ", " + text)

            seconds += 5

        else:
            break

    cap.release()

if __name__ == "__main__":
    video_files = ['team1.mp4', 'team2.mp4', 'team3.mp4']
    processes = []

    for video_file in video_files:
        p = Process(target=process_video, args=(video_file,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()