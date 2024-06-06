import cv2
import pytesseract


img = cv2.imread('debug.jpg')

# URL bar
# frame = img[220: 260, 385: 1000]

# Search bar
frame = img[250: 300, 385: 600]

text1 = pytesseract.image_to_string(frame)

# URL bar
# frame = cv2.rectangle(frame, (5,7), (900, 35),(0, 255, 0), 2)


# search bar
frame = cv2.rectangle(frame, (10, 20), (200, 40),(0, 255, 0), 2)


# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
text2 = pytesseract.image_to_string(frame, config='--psm 7')

print("text1: ", text1)
print("text2: ", text2)

cv2.imshow('image', frame)

# pytesseract.image_to_string(img[220: 260, 385: 1000])
cv2.waitKey(0)
