##Jason Gupta & Angie Palm
##Because the Internet

from Myro import *

import datetime
import ramblin.py
import ramblin2.py

#init()
songOrDance = "dance"
isComplete = True
while isComplete:
    currMinute = datetime.datetime.now().time().minute
    if (currMinute == 25):
        #play dat beat
        #do dat dance
        if (songOrDance == "dance"):
            

        else if (songOrDance == "song"):
            ramblin.ramblin()
            #ramblin2.ramblin()
        isComplete = False