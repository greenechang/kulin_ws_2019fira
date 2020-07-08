import cv2

camera = cv2.VideoCapture(0)
ret, img = camera.read()


path = "/home/robotis/Kulin_ws/Other Codes/aruco_data/"
count = 0
while True:
    print("-------------------")
    print("count: ",count)
    name = path + str(count)+".jpg"
    ret, img = camera.read()
    cv2.imshow("img", img)

    
    if cv2.waitKey(20) & 0xFF == ord('c'):
        cv2.imwrite(name, img)
        cv2.imshow("img", img)
        print("count: ",count)
        count += 1
        print("count: ",count)
        continue
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break;
