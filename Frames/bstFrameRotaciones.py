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

        self.btnInsert.config(command = self.insertClickedAvl)

    def calcFesClicked(self):
        self.miarbol.calculaFes(self.miarbol.root)
        self.pintaArbol()

    def insertClickedAvl(self):
        if(self.miarbol.insertAvl(int(self.inputField.get()))):
            if( self.miarbol.root.right is not None or self.miarbol.root.left is not None):
                self.pintaArbol()
        else:
            messagebox.showwarning('Nodo Repetido', 'Se intentó insertar un nodo que ya existía')

    def rotaLLClicked(self):
        self.miarbol.rotaLL()
        print(str(self.miarbol))
        self.pintaArbol()

    def rotaRRClicked(self):
        self.miarbol.rotaRR()
        self.pintaArbol()
