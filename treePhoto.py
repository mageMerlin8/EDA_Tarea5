from PIL import Image, ImageTk
from resizeimage import resizeimage

from tkinter import *

class TreeFrame(Frame):
    def __init__(self, window, arbol):
        Frame.__init__(window)
        Frame.bind("<Configure>", self.resizeClicked)
        self.treeLabel = Label(self, image = None)
        self.miarbol = arbol
        self.treeLabel.pack()

    def pintaArbol(self):
        resizeClicked()

    def resizeClicked(seld, event = None):
        height = self.winfo_height()
        width = self.winfo_width() - 150
        treeImage = Image.open('currentTree.jpg')
        treeImage = resizeimage.resize_contain(treeImage, [width, height])
        treePhoto = ImageTk.PhotoImage(treeImage)
        self.treeLabel.config(image = treePhoto)
        self.treeLabel.image = treePhoto

        self.treeLabel.pack()
