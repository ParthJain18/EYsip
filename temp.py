import cv2

img = cv2.imread("debug.jpg")

#url
# cv2.imshow("frame", img[250: 300, 385: 600])

#google_search
cv2.imshow("Frame", img[250: 300, 385: 600])

cv2.waitKey(0)