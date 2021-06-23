# Run the script to see the results

import cv2
from handLmModel import handDetector

def main():
    cap = cv2.VideoCapture(0)
    
    # Set the frame resolution in pixels
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # Instantiation of handDetector class
    detector = handDetector()
    
    while True:
        success, img = cap.read()
        img = cv2.flip(img,1)
        img = detector.findHands(img)
        
        # List of handedness and coordinates of landmarks in pixels
        lmList = detector.findPosition(img,draw=False)
        
        if len(lmList) != 0:
          
            # Print the handedness and landmarks in console(can use this as per your use-case)
            print(lmList)
            
            # Draw the handedness on the wrist of the hand
            if lmList[0] == 'both':
                cv2.putText(img,'Right',(lmList[1][0][1],lmList[1][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,(255, 25, 0), 3)
                cv2.putText(img, 'Left', (lmList[2][0][1], lmList[2][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,(0, 25, 255), 3)
            elif lmList[0] == 'Left':
                cv2.putText(img, 'Left', (lmList[1][0][1], lmList[1][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,
                            (0, 25, 255), 3)
            elif lmList[0] == 'Right':
                cv2.putText(img, 'Right', (lmList[1][0][1], lmList[1][0][2]), cv2.FONT_HERSHEY_PLAIN, 3,
                            (255, 25, 0), 3)

        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
