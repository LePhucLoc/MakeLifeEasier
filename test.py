import cv2
import numpy
  
i = 2

while 1:
    frame = cv2.imread('./downloads/nienluan2019/hinh75'+str(i)+'.jpg')
    frame = cv2.resize(frame,(800,640))
    cv2.imshow("cap", frame)
    i += 1
    cv2.waitKey(100)
    t = input()

cv2.destroyAllWindows()