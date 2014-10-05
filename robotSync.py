##Jason Gupta & Angie Palm
##Because the Internet

from Myro import *

import urllib
import datetime
#import ramblin.py
#import ramblin2.py

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
    currMinute = datetime.datetime.now().time().minute
    if (currMinute == 25):
        #play dat beat
        #do dat dance
        if (songOrDance == "dance"):
            print("HI")
        elif (songOrDance == "song"):
            ramblin.ramblin()
            #ramblin2.ramblin()
        isComplete = False


#def switchAndSlide():

