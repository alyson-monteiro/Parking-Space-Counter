import cv2
import pickle

img = cv2.imread('estacionamento.png')
img = cv2.resize(img, (640,420))

spaces =[]

for i in range(69):
    space = cv2.selectROI('Select the spaces', img, False)
    cv2.destroyWindow('Select the spaces')
    spaces.append(space)
    print(f"Space {i+1}: {space}")

    for x, y, w, h in spaces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

with open('spaces.pkl', 'wb') as arquive:
    pickle.dump(spaces, arquive)