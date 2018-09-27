import bst
from tkinter import *
from tkinter import messagebox



class ButtonsFrame(Frame):
    def __init__(self, window, arbol = None, **options):
        Frame.__init__(self, window, **options)
        self.config(width = 150)
        self.buttonsFrame = Frame(self)
        self.miarbol = arbol

        self.btnInsert = Button(self.buttonsFrame, text = 'insertar', command = self.insertClicked)
        self.btnDelete = Button(self.buttonsFrame, text = 'eliminar', command = self.deleteClicked)
        self.btnFind = Button(self.buttonsFrame, text = 'encontrar', command = self.findClicked)
        self.btnClear = Button(self.buttonsFrame, text = 'clear', command = self.clearClicked)


        self.btnInsert.pack(side = TOP)
        self.btnDelete.pack()
        self.btnFind.pack()
        self.btnClear.pack()

        self.buttonsFrame.pack(side = BOTTOM)

        self.inputFrame = Frame(self)

        self.inputLabel = Label(self.inputFrame, text = 'Dato: ')
        self.inputField = Entry(self.inputFrame, width = 10)

        self.inputLabel.pack(side = LEFT)
        self.inputField.pack(side = RIGHT)
        self.inputFrame.pack()

    def setArbol(self, arbol):
        self.miarbol = arbol

    def insertClicked(self):
        if(self.miarbol.insert(int(self.inputField.get()))):
            if( self.miarbol.root.right is not None or self.miarbol.root.left is not None):
                miarbol.outputTreeImage()
        else:
            messagebox.showwarning('Nodo Repetido', 'Se intentó insertar un nodo que ya existía')


    def deleteClicked(self):
        if(self.miarbol.delete(int(self.inputField.get()))):
            miarbol.outputTreeImage()
        else:
            messagebox.showwarning('Nodo Repetido', 'Se intentó eliminar un nodo que no existe')


    def findClicked(self):
        if(self.miarbol.find(int(self.inputField.get()))):
            messagebox.showinfo('Nodo Encontrado','Se encontró el nodo que buscabas!')
        else:
            messagebox.showwarning('Nodo no Encontrado', 'No se encontró el nodo que buscabas!')


    def clearClicked(self):
        self.miarbol.clear()
        miarbol.outputTreeImage()
