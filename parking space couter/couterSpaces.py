import cv2
import pickle
import numpy as np

spaces = []

with open('spaces.pkl', 'rb') as arquive:
    spaces = pickle.load(arquive)

video = cv2.VideoCapture('videoEstacionamento.mp4')
while True:
    check, img = video.read()
    img = cv2.resize(img, (640, 420))
    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgThreshold = cv2.adaptiveThreshold(
        imgCinza, 
        255, #max value a pixel can be(white)
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY_INV, 
        25,
        16)
    
    imgMedian = cv2.medianBlur(imgThreshold, 5) #eliminates noise
    kernel = np.ones((3, 3), np.uint8)
    imgDilation = cv2.dilate(imgMedian, kernel) #dilates the image

    openSpaces = 0
    for x, y, w, h in spaces:
        space = imgDilation[y:y+h, x:x+w]
        count = cv2.countNonZero(space) #counts white pixels
        # cv2.putText(
        #     img, 
        #     str(count),
        #     (x, y+h-10), 
        #     cv2.FONT_HERSHEY_SIMPLEX, 
        #     0.5,
        #     (255, 255, 255),
        #     1)
            
        if count < 350:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1) #Green
            openSpaces += 1
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1) #Red

        if openSpaces < 13:
            color = (0, 0, 255) #Red
        if openSpaces < 15:
            color = (0, 255, 255) #Yellow
        else:
            color = (0, 255, 0) #Green
        cv2.rectangle(img, (0,0), (640, 35), color, -1)
        cv2.putText(
            img, 
            f'Open Spaces: {openSpaces}/69', 
            (10, 25), 
            cv2.FONT_HERSHEY_SIMPLEX, 
            1,
            (255, 255, 255), #white
            2)

        
    
    cv2.imshow('Video', img)
    #cv2.imshow('VideoTHRESHOLD', imgDilation) #pre-processing output
    cv2.waitKey(10)

print(spaces)
