from Myro import*
init("sim")

def highF(time):
    if time==3:
        beep(.5,1396.91)
    if time==2:
        beep(.222,1396.91)
        beep(.111,0)
    if time==1:
        beep(.083,1396.91)
        beep(.083,0)

def highE(time):
    if time==3:
        beep(.5,1318.51)
    if time==2:
        beep(.222,1318.51)
        beep(.111,0)
    if time==1:
        beep(.083,1318.51)
        beep(.083,0)

def highD(time):
    if time==3:
        beep(.5,1174.66)
    if time==2:
        beep(.222,1174.66)
        beep(.111,0)
    if time==1:
        beep(.083,1174.66)
        beep(.083,0)

def highC(time):
    if time==3:
        beep(.5,1046.50)
    if time==2:
        beep(.222,1046.50)
        beep(.111,0)
    if time==1:
        beep(.083,1046.50)
        beep(.083,0)

def highB(time):
    if time==3:
        beep(.5,932.33)
    if time==2:
        beep(.222,932.33)
        beep(.111,0)
    if time==1:
        beep(.083,932.33)
        beep(.083,0)

def highA(time):
    if time==3:
        beep(.5,880.00)
    if time==2:
        beep(.222,880.00)
        beep(.111,0)
    if time==1:
        beep(.083,880.00)
        beep(.083,0)

def highG(time):
    if time==3:
        beep(.5,783.99)
    if time==2:
        beep(.222,783.99)
        beep(.111,0)
    if time==1:
        beep(.083,783.99)
        beep(.083,0)
    if time==0:
        beep(.833,783.99)

def lowF(time):
    if time==3:
        beep(.5,698.46)
    if time==2:
        beep(.222,698.46)
        beep(.111,0)
    if time==1:
        beep(.083,698.46)
        beep(.083,0)
    if time==0:
        beep(.833,698.46)

def lowE(time):
    if time==3:
        beep(.5,659.25)
    if time==2:
        beep(.222,659.25)
        beep(.111,0)
    if time==1:
        beep(.083,659.25)
        beep(.083,0)

def rest(time):
    if time==3:
        beep(.5,0)
    if time==2:
        beep(.222,0)
        beep(.111,0)
    if time==1:
        beep(.167,0)

def ramblin():
    #intro
    highF(3)
    highD(3)
    highC(3)
    highA(3)
    highC(1)
    highD(1)
    highC(1)
    highB(1)
    highA(1)
    highG(1)
    lowF(1)
    rest(2)

    #chorus1
    #Phrase1
    highA(2)
    highG(1)
    lowF(2)
    lowF(1)
    lowF(2)
    highG(1)
    highA(2)
    highA(1)
    highA(1)
    highG(1)
    lowF(1)
    highG(1)
    highA(1)
    highG(1)
    lowF(2)
    lowE(1)
    lowF(0)
    #Phrase2
    highG(1)
    highA(1)
    highA(1)
    highA(1)
    highA(2)
    highB(1)
    highC(1)
    highC(1)
    highC(1)
    highC(2)
    highC(1)
    highC(1)
    highG(1)
    highG(1)
    highG(2)
    highA(1)
    highG(0)
    #Phrase3
    highC(1)
    highD(2)
    highB(1)
    highD(2)
    highB(1)
    highD(1)
    highF(3)
    highE(1)
    highD(1)
    highC(2)
    highA(1)
    highC(2)
    highA(1)
    highC(1)
    rest(2)
    #Phase3
    highA(2)
    highG(1)
    lowF(2)
    lowF(1)
    lowF(2)
    highG(1)
    highA(2)
    highA(1)
    highA(1)
    highG(1)
    lowF(1)
    highG(1)
    highA(1)
    highG(1)
    lowF(2)
    lowE(1)
    lowF(2)
    rest(1)

    #chorus2
    #Phrase1
    highA(2)
    highG(1)
    lowF(2)
    lowF(1)
    lowF(2)
    highG(1)
    highA(2)
    highA(1)
    highA(1)
    highG(1)
    lowF(1)
    highG(1)
    highA(1)
    highG(1)
    lowF(2)
    lowE(1)
    lowF(0)
    #Phrase2
    highG(1)
    highA(1)
    highA(1)
    highA(1)
    highA(2)
    highB(1)
    highC(1)
    highC(1)
    highC(1)
    highC(2)
    highC(1)
    highC(1)
    highG(1)
    highG(1)
    highG(2)
    highA(1)
    highG(0)
    #Phrase3
    highC(1)
    highD(2)
    highB(1)
    highD(2)
    highB(1)
    highD(1)
    highF(3)
    highE(1)
    highD(1)
    highC(2)
    highA(1)
    highC(2)
    highA(1)
    highC(1)
    rest(2)
    #Phase3
    highA(2)
    highG(1)
    lowF(2)
    lowF(1)
    lowF(2)
    highG(1)
    highA(2)
    highA(1)
    highA(1)
    highG(1)
    lowF(1)
    highG(1)
    highA(1)
    highG(1)
    lowF(2)
    lowE(1)
    lowF(2)
    rest(1)

    #chorus3
    #Phrase1
    highA(2)
    highG(1)
    lowF(2)
    lowF(1)
    lowF(2)
    highG(1)
    highA(2)
    highA(1)
    highA(1)
    highG(1)
    lowF(1)
    highG(1)
    highA(1)
    highG(1)
    lowF(2)
    lowE(1)
    lowF(0)
    #Phrase2
    highG(1)
    highA(1)
    highA(1)
    highA(1)
    highA(2)
    highB(1)
    highC(1)
    highC(1)
    highC(1)
    highC(2)
    highC(1)
    highC(1)
    highG(1)
    highG(1)
    highG(2)
    highA(1)
    highG(0)
    #Phrase3
    highC(1)
    highD(2)
    highB(1)
    highD(2)
    highB(1)
    highD(1)
    highF(3)
    highE(1)
    highD(1)
    highC(2)
    highA(1)
    highC(2)
    highA(1)
    highC(2)
    rest(1)
    #Ending
    highB(1)
    #intro(part 2)
    highF(3)
    highD(3)
    highC(3)
    highA(3)
    highC(1)
    highD(1)
    highC(1)
    highB(1)
    highA(1)
    highG(1)
    lowF(3)
    highF(1)
ramblin()
