##Jason Gupta & Angie Palm
##Because the Internet

from Myro import *

import datetime
import time
#init()
date = datetime.date(2014, 10, 5)
x = datetime.datetime.now().time().minute
y = time.clock()
print (x)
print (type(x))
isComplete = True
while isComplete:
    currMinute = datetime.datetime.now().time().minute
    if (currMinute == 25):
        #play dat beat
        #do dat dance
        print ("Look at me now")
        isComplete = False