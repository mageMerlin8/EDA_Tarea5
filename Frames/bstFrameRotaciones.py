from Frames.bstFramePlus import *
from trees import avl

class BSTFrameRotaciones(BSTFramePlus):
    def __init__(self, window):
        BSTFramePlus.__init__(self, window)

        self.miarbol = avl.ArbolAVL(self.miarbol.root)

        self.frameRotaciones = Frame(self.cosasFrame)
        self.btnRotLL = Button(self.frameRotaciones, text = 'rota LL', command = self.rotaLLClicked)
        self.btnRotRR = Button(self.frameRotaciones, text = 'rota RR', command = self.rotaRRClicked)

        self.btnCalcFes = Button(self.frameRotaciones, text = 'calcula fes', command = self.calcFesClicked)
        self.btnCalcFes.pack()

        self.btnRotLL.pack()
        self.btnRotRR.pack()
        self.frameRotaciones.pack()


    def calcFesClicked(self):
        self.miarbol.calculaFes(self.miarbol.root)
        self.pintaArbol()

    def rotaLLClicked(self):
        self.miarbol.rotaLL()
        print(str(self.miarbol))
        self.pintaArbol()

    def rotaRRClicked(self):
        self.miarbol.rotaRR()
        self.pintaArbol()
