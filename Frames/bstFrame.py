import trees.bst as bst
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from resizeimage import resizeimage
import random as rd

class BSTFrame(Frame):
    def __init__(self, window):
        Frame.__init__(self, window)

        #initialize
        self.cosasFrame = Frame(self, width = 150)
        self.miarbol = bst.ArbolB()

        #create widgets
        #Buttons: insert, find, delete, clear
        self.buttonsFrame = Frame(self.cosasFrame)

        self.btnInsert = Button(self.buttonsFrame, text = 'insertar', command = self.insertClicked)
        self.btnDelete = Button(self.buttonsFrame, text = 'eliminar', command = self.deleteClicked)
        self.btnFind = Button(self.buttonsFrame, text = 'encontrar', command = self.findClicked)
        self.btnClear = Button(self.buttonsFrame, text = 'clear', command = self.clearClicked)

        self.btnInsert.pack(side = TOP)
        self.btnDelete.pack()
        self.btnFind.pack()
        self.btnClear.pack()

        self.buttonsFrame.pack()

        #txtFields: input
        self.inputFrame = Frame(self.cosasFrame)

        self.inputLabel = Label(self.inputFrame, text = 'Dato: ')
        self.inputField = Entry(self.inputFrame, width = 10)

        self.inputLabel.pack(side = LEFT)
        self.inputField.pack(side = RIGHT)

        self.inputFrame.pack(side = TOP)

        #tree
        self.treeFrame = Frame(self)
        self.treeFrame.bind("<Configure>", self.resizeClicked)
        self.treeLabel = Label(self.treeFrame, image = None)

        self.treeLabel.pack()

        #organize
        self.treeFrame.pack(side = RIGHT,fill=BOTH , expand=1)
        self.cosasFrame.pack(side = LEFT)

    def pintaArbol(self):
        self.miarbol.outputTreeImage('currentTree.jpg')
        self.resizeClicked()

    def insertClicked(self):
        if(self.miarbol.insert(int(self.inputField.get()))):
            if( self.miarbol.root.right is not None or self.miarbol.root.left is not None):
                self.pintaArbol()
        else:
            messagebox.showwarning('Nodo Repetido', 'Se intentó insertar un nodo que ya existía')

    def deleteClicked(self):
        if(self.miarbol.delete(int(self.inputField.get()))):
            self.pintaArbol()
        else:
            messagebox.showwarning('Nodo Repetido', 'Se intentó eliminar un nodo que no existe')

    def findClicked(self):
        if(self.miarbol.find(int(self.inputField.get()))):
            messagebox.showinfo('Nodo Encontrado','Se encontró el nodo que buscabas!')
        else:
            messagebox.showwarning('Nodo no Encontrado', 'No se encontró el nodo que buscabas!')

    def clearClicked(self):
        self.miarbol.clear()
        self.pintaArbol()

    def resizeClicked(self, event = None):
        height = self.treeFrame.winfo_height()
        width = self.treeFrame.winfo_width() - self.cosasFrame.winfo_width()
        treeImage = Image.open('currentTree.jpg')
        treeImage = resizeimage.resize_contain(treeImage, [width, height])
        treePhoto = ImageTk.PhotoImage(treeImage)
        self.treeLabel.config(image = treePhoto)
        self.treeLabel.image = treePhoto

        self.treeLabel.pack()
