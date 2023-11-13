import cv2

video = cv2.VideoCapture("AnthonyShkraba.mp4")

while True:
    sucess, frame = video.read()
    cv2.imshow("results", frame)

    if cv2.waitKey(20) == 32:
        break

video.release()
cv2.destroyAllWindows()

    































