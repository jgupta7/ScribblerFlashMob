from Myro import*
init("sim")

d=.4#set tempo
q=2*d/3
e=q/2

def highF(time):
    if time==3:
        beep(d,1396.91)
    if time==2:
        beep(q,1396.91)
    if time==1:
        beep(e,1396.91)
def highE(time):
    if time==3:
        beep(d,1318.51)
    if time==2:
        beep(q,1318.51)
    if time==1:
        beep(e,1318.51)
def highD(time):
    if time==3:
        beep(d,1174.66)
    if time==2:
        beep(q,1174.66)
    if time==1:
        beep(e,1174.66)
def highC(time):
    if time==3:
        beep(d,1046.50)
    if time==2:
        beep(q,1046.50)
    if time==1:
        beep(e,1046.50)
def highB(time):
    if time==3:
        beep(d,932.33)
    if time==2:
        beep(q,932.33)
    if time==1:
        beep(e,932.33)
def highA(time):
    if time==3:
        beep(d,880.00)
    if time==2:
        beep(q,880.00)
    if time==1:
        beep(e,880.00)
def highG(time):
    if time==3:
        beep(d,783.99)
    if time==2:
        beep(q,783.99)
    if time==1:
        beep(e,783.99)
    if time==0:
        beep(2*q,783.99)
def lowF(time):
    if time==3:
        beep(d,698.46)
    if time==2:
        beep(q,698.46)
    if time==1:
        beep(e,698.46)
    if time==0:
        beep(2*q,698.46)
def lowE(time):
    if time==3:
        beep(d,659.25)
    if time==2:
        beep(q,659.25)
    if time==1:
        beep(e,659.25)
def rest(time):
    if time==3:
        beep(d,0)
    if time==2:
        beep(q,0)
    if time==1:
        beep(e,0)

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
