# This script contains a base model for hand tracking and landmarks detection. We can make use of this script in other projects by instantiating the class.

import cv2
import mediapipe as mp

#  Hand detector class
class handDetector():
  
    ## Class constructor
    """
    args: static mode(bool, def=false): toggle static mode on when dealing with stationary images,
          maxHands(int, def=2): specify the expected number of hands in the frame,
          detectionCon(float,range=0-1,def=0.7): The confidence level with which the hands should be detected,
          trackingCon(float,range=0-1,def=0.5)
    """
    def __init__(self, mode=False, maxHands=2, detectionCon=0.7, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
  
    # Find Hands method
    """
    Generates coordinates of landmarks in the image and returns an image with landmarks drawn on it
    args: img:- the image on which the landmarks are to be searched and drawn
          draw:- True if the landmarks and connections are to be drawn else false
    """
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    # Find position method
    """
    This method is used to detect handedness and the coordinates of the landmarks on the hands detected in the frame.
    It returns a list which contains the following parameters:
      Handedness: left/right/both
      coordinates: list of x and y coordinates of 21 landmarks of each hand
    """
    def findPosition(self, img, draw=True):
        rlmlist = []

        if self.results.multi_hand_landmarks:
            if len(self.results.multi_hand_landmarks) == 2:
                rlmlist.append('both')
            elif len(self.results.multi_hand_landmarks) == 1:
                rlmlist.append(self.results.multi_handedness[0].classification[0].label)

            for n in self.results.multi_hand_landmarks:
                lmList = []
                myHand = n
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                rlmlist.append(lmList)

        return rlmlist


