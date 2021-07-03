import cv2
import mediapipe as mp

class handDetector():
    """
    Initiating:
    mode = False --> when using dynamic video capture
    maxHands --> How many hands to detect
    detectionCon --> success of detection
    trackCon --> used for tracking of hand, might have increased latency
    """
    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, trackCon=0.7):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    """
    Finds hand and draws points (21 points total)
    """
    def findHands(self,img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            handLms = self.results.multi_hand_landmarks[0]
            if draw:
                self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)

        return img
    """
    Used to find postions of points of hand
    """
    def findpositions(self, img):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[0]
            """
            id represents as shown in hand_landmarks.png
            """
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                x, y = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, x, y])
                
            return self.lmList

detector = handDetector()

def cv2_handdetector(img):
    
    original = img.copy()
    #
    img = detector.findHands(img)

    lmk_list = detector.findpositions(img)

    points_to_get = [0,4,8,12,16,20,2,5,9,13,17]
    
    if lmk_list != None:
        new_list = []
        for i in lmk_list:
            if i[0] in points_to_get:
                new_list.append(i)
        return new_list,original
    else:
        return None, original


