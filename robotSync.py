##Jason Gupta & Angie Palm
##Because the Internet

from Myro import *

import datetime
import urllib
import ramblin.py
import ramblin2.py

#init()
songOrDance = "dance"
isComplete = True

f = urllib.urlopen("http://www.unixtimestamp.com/index.php")
stringList = (f.readlines())
timeStamp = ""
for string in stringList:
    count = 0
    aList = []
    if "(UTC)" in string:
        print(string[92:102])

while isComplete:
    #currMinute = datetime.datetime.now().time().minute
    #if (currMinute == 25):
    #old condition ^ where we use computer time
    if (words):
        #play dat beat
        #do dat dance
        if (songOrDance == "dance"):
            

        elif (songOrDance == "song"):
            ramblin.ramblin()
            #ramblin2.ramblin()
        isComplete = False


def backAndForth():
    forward(1,0.5)
    backward(1,0.5)
def spinLeftRight():
    turnLeft(1,0.5)
    turnRight(1,0.5)
    turnRight(1,0.5)
    turnLeft(1,0.5)
def moveTurnRight():
    turnRight(1,0.5)
    forward(1,1)
    backward(1,1)
    turnLeft(1,0.5)
def moveTurnLeft():
    turnLeft(1,0.5)
    forward(1,1)
    backward(1,1)
    turnRight(1,0.5)
