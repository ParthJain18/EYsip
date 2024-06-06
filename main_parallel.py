import cv2
import concurrent.futures
from ocr import extract_text_from_image

def process_chunk(chunk):
    start_frame, end_frame = chunk
    cap = cv2.VideoCapture('team1.mp4')
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    results = []

    for i in range(start_frame, end_frame, 30):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()

        if ret == True:
            frame = frame[220: 260, 385: 1000]
            frame = cv2.rectangle(frame, (5,7), (900, 35),(0, 255, 0), 2)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            text = extract_text_from_image(frame, config='--psm 7').replace(",", "")

            seconds = round(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)

            results.append((seconds, text))

    cap.release()

    return results

if __name__ == "__main__":
    cap = cv2.VideoCapture('team1.mp4')
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()

    chunk_size = 1000
    chunks = [(i, min(i + chunk_size, total_frames)) for i in range(385560, total_frames, chunk_size)]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for chunk_results in executor.map(process_chunk, chunks):
            with open("log_parallel_team_1.txt", 'a') as file:
                for seconds, text in chunk_results:
                    file.writelines(str(seconds) + ", " + text)