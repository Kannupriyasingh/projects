import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'attendenceimg'
images = []
classnames = []
mylist = os.listdir(path)
print(mylist)
for cls in mylist:
    currimg = cv2.imread(f'{path}/{cls}')
    images.append(currimg)
    classnames.append(os.path.splitext(cls)[0])
print(classnames)

def findencodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markattendence(name):
    with open('attendence.csv','r+') as f:
        mydatalist = f.readline()
        namelist = []
        for line in mydatalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')

encodelistforknownfaces = findencodings(images)
print('encoding complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgsmall = cv2.resize(img,(0,0),None,0.25,0.25)
    imgsmall = cv2.cvtColor(imgsmall, cv2.COLOR_BGR2RGB)

    facecurrframe = face_recognition.face_locations(imgsmall)
    encodecurrframe = face_recognition.face_encodings(imgsmall, facecurrframe)

    for encodeface, faceloc in zip(encodecurrframe, facecurrframe):
        matches = face_recognition.compare_faces(encodelistforknownfaces, encodeface)
        facedis = face_recognition.face_distance(encodelistforknownfaces, encodeface)
        #print(facedis)
        matchindex = np.argmin(facedis)

        if matches[matchindex]:
            name = classnames[matchindex].upper()
            #print(name)
            y1,x2,y2,x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img, name, (x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendence(name)



    cv2.imshow('Webcam',img)
    cv2.waitKey(1)

#faceloc = face_recognition.face_locations(imgElon)[0]
#encodeElon = face_recognition.face_encodings(imgElon)[0]
#cv2.rectangle(imgElon,(faceloc[3], faceloc[0]),(faceloc[1],faceloc[2]), (255,0,255),2)

#faceloctest = face_recognition.face_locations(imgElon)[0]
#encodeElontest = face_recognition.face_encodings(imgElon)[0]
#cv2.rectangle(imgtest,(faceloctest[3], faceloctest[0]),(faceloctest[1],faceloctest[2]), (255,0,255),2)

#results = face_recognition.compare_faces([encodeElon], encodeElontest)
#facedis = face_recognition.face_distance([encodeElon], encodeElontest)
