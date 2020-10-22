speedFall = 3
posGoutteY = 0
nbrGoutte = 10000
listG = []
i = 0

def setup():
    size(600,400)
    clear()
    createList()
    frameRate(30)
    
def draw():
    global listG,nbrGoutte,i
    clear()    
    #drawGoutte()
    listG.append(Goutte())
    while i > -1:
        listG[i].fall()
        listG[i].getOnScreen()
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
        self.xSize = 10
        self.ySize = 50
        self.xPos = random(0+self.xSize, width-self.xSize)
        self.yPos = random(-100,0)
        self.fallSpeed = random(5,10)
        
    def define(self):
        print('xSize  =',self.xSize, 'ySize  =',self.ySize, 'xPos  =',self.xPos, 'yPos  =',self.yPos)
    
    def fall(self):
        self.yPos += self.fallSpeed
            
    def getOnScreen(self):
        fill(0,125,255)
        rect(self.xPos,self.yPos,self.xSize,self.ySize)
