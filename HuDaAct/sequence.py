import cv2
import numpy as np


video_path = '/data4/jiali/data/32frames_video_train/train_deep_32frames_whole/052/K_10344.avi'

cap = cv2.VideoCapture(video_path)

snapshot_list = [5, 8, 16, 22, 28]

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    print i
    i += 1
    cv2.imshow('frame', frame)
    cv2.imwrite('seq_depth/img_%d.jpg' % i, frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
