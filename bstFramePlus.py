from bstFrame import *

class BSTFramePlus(BSTFrame):
    def __init__(self, window):
        BSTFrame.__init__(self, window)


        self.randTreeFrame = Frame(self.cosasFrame, width = 50)
        #NEW
        self.randLabel = Label(self.randTreeFrame, text = 'Generar un arbol binario:')
        self.intSpinBox = Spinbox(self.randTreeFrame, from_ = 2, to = 100)
        self.btnAltArbol = Button(self.randTreeFrame, text = 'Genera!', command = self.creaArbolClicked)

        self.randLabel.pack(side = TOP)
        self.intSpinBox.pack(side = LEFT)
        self.btnAltArbol.pack()

        self.randTreeFrame.pack(side = BOTTOM)

    ##NEW
    def creaArbolClicked(self):
        self.miarbol.clear()
        num = int(self.intSpinBox.get())
        nums = rd.sample(range(1, 99), num)
        for i in nums:
            self.miarbol.insert(int(i))

        self.pintaArbol()
