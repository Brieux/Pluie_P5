speedFall = 3
posGoutteY = 0
nbrGoutte = 10000
listG = []
i = 0
l = 0

def setup():
    fullScreen()
    clear()
    createList()
    frameRate(30)
    
def draw():
    global listG,nbrGoutte,i, l
    clear()    
    #drawGoutte()
    listG.append(Goutte())
    while l <= i :
        listG[l].fall()
        listG[l].getOnScreen()
        l = l+1
    i = i+1
    l = 0
    print("une goutte")
    

# def drawGoutte():
#     global speedFall,posGoutteY
#     if posGoutteY > height+50:
#         print("Goutte trop basse")
#     else:    
#         fill(0,125,255)
#         rect(280,posGoutteY,10,50)
#         posGoutteY += speedFall
    
def createList():
    global nbrGoutte
    global listG
    for i in range(nbrGoutte):
        listG.append(Goutte())
            
class Goutte():
    def __init__(self):
        self.xSize = random(5,12)
        self.ySize = self.xSize * 8
        self.xPos = random(0+self.xSize, width-self.xSize)
        self.yPos = random(-100,-10)
        self.fallSpeed = self.xSize * 2.5
        
    def define(self):
        print('xSize  =',self.xSize, 'ySize  =',self.ySize, 'xPos  =',self.xPos, 'yPos  =',self.yPos)
    
    def fall(self):
        self.yPos += self.fallSpeed
            
    def getOnScreen(self):
        fill(110,3,177)
        rect(self.xPos,self.yPos,self.xSize,self.ySize)
