from bstFramePlus import *

class BSTFrameRotaciones(BSTFramePlus):
    def __init__(self, window):
        BSTFramePlus.__init__(self, window)

        self.frameRotaciones = Frame(self.cosasFrame)
        self.btnRotLL = Button(self.frameRotaciones, text = 'rota LL', command = self.rotaLLClicked)
        self.btnRotRR = Button(self.frameRotaciones, text = 'rota RR', command = self.rotaRRClicked)

        self.btnRotLL.pack()
        self.btnRotRR.pack()
        self.frameRotaciones.pack()

    def rotaLLClicked(self):
        self.miarbol.rotaLL()
        self.pintaArbol()

    def rotaRRClicked(self):
        self.miarbol.rotaRR()
        self.pintaArbol()
