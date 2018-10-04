from Frames.bstFrame import *
from pruebas.helper import mkdir_p
from trees import avl
"""
Adds the functuionality to create new random trees
and for testing
"""
class BSTFramePlus(BSTFrame):
    def __init__(self, window):
        BSTFrame.__init__(self, window)


        self.randTreeFrame = Frame(self.cosasFrame, width = 50)
        #Random tree frame
        self.randLabel = Label(self.randTreeFrame, text = 'Generar un arbol binario:')
        self.intSpinBox = Spinbox(self.randTreeFrame, from_ = 2, to = 100)
        self.btnAltArbol = Button(self.randTreeFrame, text = 'Genera!',
                                  command = self.creaArbolClicked)
        #self.btnPrueba = Button(self.randTreeFrame, text = '<-TEST->',
        #                          command = self.TEST)

        self.checkPruebasVal = IntVar()
        self.checkPruebas = Checkbutton(self.randTreeFrame, text = 'Generar archivos de prueba',
                                        command = self.pruebasToggled, variable = self.checkPruebasVal)


        self.randLabel.pack(side = TOP)
        self.intSpinBox.pack(side = LEFT)
        self.btnAltArbol.pack()
        self.checkPruebas.pack(side = BOTTOM)
        #self.btnPrueba.pack(side = BOTTOM)
        #pack frames:
        self.randTreeFrame.pack(side = BOTTOM)

    ##NEW
    def creaArbolClicked(self):
        self.miarbol.clear()
        num = int(self.intSpinBox.get())
        nums = rd.sample(range(1, 99), num)
        for i in nums:
            self.miarbol.insert(int(i))
        self.pintaArbol()

    def creaArbolConPruebasClicked(self, arr = None):
            self.miarbol.clear()
            num = int(self.intSpinBox.get())
            if not arr:
                nums = rd.sample(range(1, 99), num)
            else:
                nums = arr
            #new directory
            curDir = 'pruebas/' + str(nums)
            mkdir_p(curDir)
            cont = 0
            for i in nums:
                self.miarbol.insert(int(i))
                if(self.miarbol.root.left or self.miarbol.root.right):
                    fileName = ('{}/' + str(cont) + '_' + str(i) + '.jpg').format(curDir)
                    self.miarbol.outputTreeImage(fileName)
                cont += 1
            self.pintaArbol()

    def pruebasToggled(self):
        if self.checkPruebasVal.get() == 1:
            self.btnAltArbol.config(command = self.creaArbolConPruebasClicked)
        else:
            self.btnAltArbol.config(command = self.creaArbolClicked)
## Pruebas
    def TEST(self):
        list = [10, 28, 96, 65, 95, 26, 23, 73, 12, 76, 80, 94, 77, 33, 50, 13, 32, 82, 22, 47, 20, 67, 62, 79, 8]
        self.creaArbolConPruebasClickedTEST(list)

    def creaArbolConPruebasClickedTEST(self, nums):
            self.miarbol.clear()
            cont = 0
            for i in nums:
                self.miarbol.insert(int(i))
            self.pintaArbol()

class AVLFramePlus(BSTFramePlus):
    def __init__(self, window):
        BSTFramePlus.__init__(self, window)
        self.miarbol = avl.ArbolAVL(self.miarbol.root)
