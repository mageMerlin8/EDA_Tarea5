from buttons import *
from treePhoto import *

class myWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Arboles Binarios de Busqueda")
        self.geometry('500x500')
        self.bind("<Button-1>", self.mousePressed)
        self.miarbol = bst.ArbolB()

        self.buttonsFrame = ButtonsFrame(self, self.miarbol)
        self.treeFrame = TreeFrame(self, self.miarbol)

        self.buttonsFrame.pack()
        self.treeFrame.pack()

    def mousePressed(self, event):
        if (event.widget is butonsFrame.btnFind or
            event.widget is buttonsFrame.btnClear or
                event.widget is buttonsFrame.btnInsert or
                    event.widget is buttonsFrame.btnDelete):
                    self.treeFrame.resizeClicked()
