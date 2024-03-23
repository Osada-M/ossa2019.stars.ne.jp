#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2, datetime
#form = cgi.FieldStorage() 
#os.chdir('./')

def main():
    capture = cv2.VideoCapture(0)
    
    while(True):
        ret, frame = capture.read()
        windowsize = (800, 600)
        frame = cv2.resize(frame, windowsize)
        cv2.imshow('title',frame)
        a = cv2.waitKey(1) & 0xFF
        if a == ord('q'):
            break
        elif a == ord('s'):
            print('\a')
            n = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            n += '.png'
            cv2.imwrite(n, frame)
    
    capture.release()
    cv2.destroyAllWindows()

def soon():
    capture = cv2.VideoCapture(0)
    ret, frame = capture.read()
    windowsize = (800, 600)
    frame = cv2.resize(frame, windowsize)
    n = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    n += '.png'
    cv2.imwrite(n, frame)
    
soon()


htmlText = '''
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="shift-jis">
</head>
<body>
<h1>
You are an idiot.
</h1>
</body>
</html>
'''

#print("Content-Type: text/html")
#print()
#print( htmlText.encode("cp932", 'ignore').decode('cp932') )
