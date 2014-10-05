from Myro import*
initialize("sim")

#set tempo here
q=.5 #set tempo
w=4*q #whole note
h=2*q #half note
sh=(7*q)/4#gives break at end of half note
de=(3/2)*(q/2)#dotted half-note
ei=(q/2) #eigth note
s=q/4 #sixteenth note
sq=q-(q/3)#stacado quater
rsq=q/3 #rest for stacado quater
se=s #stacado eigth
ss= s/2 # stacado sixteenth
i=1 #rep counter

#establish notes
def A(l):
    beep(l, 1567.98)
def G(l):
    beep(l,1396.91)
def F(l):
    beep(l,1244.51)
def E(l):
    beep(l,1174.66)
def D(l):
    beep(l,1046.50)
def Cs(l):
    beep(l,987.77)
def C(l):
    beep(l,932.33)
def B(l):
    beep(l,880.00)
def Bb(l):
    beep(l,830.61)
def a(l):
    beep(l,783.99)
def g(l):
    beep(l,698.46)
def fs(l):#f sharp
    beep(1,659.25)
def f(l):
    beep(1,622.25)
def e(l):
    beep(l,587.33)
def r(l): #rest
    beep(l,0)



def whiteAndGold(i):
#White and Gold starts here
#Intro
    g(h)
    a(h)
    B(w)
#Phrase 1
    C(ei)
    B(q)
    C(ei)
    a(ei)
    g(ei)
    e(q)
    C(ei)
    B(q)
    C(ei)
    a(ei)
    g(ei)
    e(q)
    C(q)
    g(q)
    a(q)
    C(q)
    B(se)
    r(se)
    B(q)
    Bb(ei)
    B(ei)
    Bb(ei)
    B(q)
#Phrase 2
    D(ei)
    Cs(q)
    D(ei)
    B(ei)
    a(ei)
    g(q)
    a(q)
    B(q)
    a(sh)
    r(s)
    a(q)
    B(q)
    C(q)
    a(q)
    B(se)
    r(se)
    B(q)
    C(ei)
    D(ei)
    G(se)
    r(se)
    G(s)
    F(s)
    E(s)
    D(s)
    C(se)
    r(se)
    C(se)
    r(se)
    C(s)
    D(s)
    E(s)
    F(s)
    G(se)
    r(se)
    G(se)
    r(se)
    G(ei)
    E(ei)
    G(q)
    A(q)
    G(h)
#Phrase 3
    C(sq)
    r(rsq)
    C(q)
    D(q)
    E(q)
    D(ei)
    C(q)
    a(ei)
    C(sq)
    r(rsq)
    C(ei)
    D(ei)
    E(ei)
    D(q)
    C(ei)
    a(de)
    g(ss)
    r(ss)
    g(ei)
    e(ei)
    g(ei)
    a(q)
    e(ei)
    g(q)
    fs(ei)
    g(ei)
    a(ei)
    C(se)
    r(se)
    C(ei)
    a(ei)
    C(q)
    D(q)
    #Ending
    C(h)
    r(q)
    C(ei)


whiteAndGold(1)