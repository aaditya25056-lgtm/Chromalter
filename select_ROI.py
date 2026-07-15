import cv2
image = cv2.imread('wall3.png')
img=cv2.imread('frame1.jpg')


opt = input("Choose 1 or 2: ")
print(opt)

if int(opt)> 1:
    while True:
        cv2.imshow("Original Image", image)
        key=cv2.waitKey()

        if key == ord('a'):
            (x,y,w,h) = cv2.selectROI("Image", image, fromCenter=False, showCrosshair=False)

            croppped_roi = image[y:y+h, x:x+w]
            cv2.imshow("Croppped", croppped_roi)

            print("Coordinates: ({}, {}), Width: {}, Height: {}".format(y, x, w, h))
            height=h
            width=w
            resize_dim = (width, height)

            resized_img = cv2.resize(img, resize_dim, interpolation = cv2.INTER_AREA)
            #cv2.imshow("Second Image", img)
            cv2.imshow('Resized image', resized_img)

            cropped_img = resized_img
            rows, cols, channels = cropped_img.shape
            image[y:y + rows, x:x + cols] = cropped_img

            
            cv2.imwrite('new_wall.jpg', image)
        elif key == ord('q'):
            break
    

else:
    while True:
        import color_1
        R=color_1.r
        G=color_1.g
        B=color_1.b

        cv2.imshow("Original Image", image)
        key=cv2.waitKey()

        if key == ord('a'):
            (x,y,w,h) = cv2.selectROI("Image", image, fromCenter=False, showCrosshair=False)

            croppped_roi = image[y:y+h, x:x+w]
            cv2.imshow("Croppped", croppped_roi)

            print("Coordinates: ({}, {}), Width: {}, Height: {}".format(y, x, w, h))
            height=h
            width=w
            resize_dim = (width, height)

            

            

            cv2.rectangle(image,(x,y),(x+w,y+h),(B,G,R),-1)
            cv2.imwrite('new_wall.jpg', image)
            

            
            

        elif key == ord('q'):
                break





cv2.destroyAllWindows()

