import cv2
f = open("caption1.txt", "a")
c = 0
i = 837



while i <= 1000:
    if c % 5 == 0:
        i += 1
        img = './downloads/nienluan2019/hinh'+str(i)+'.jpg'
        frame = cv2.imread(img)
        frame = cv2.resize(frame,(600,400))
        cv2.imshow("cap", frame)
        cv2.waitKey(300)
        c = 0
    temp = "hinh" + str(i) + ".jpg#" + str(c) + " " 
    cap = input(temp)
    temp += cap + " .\n"
    f.write(temp)
    c += 1

cv2.destroyAllWindows()
