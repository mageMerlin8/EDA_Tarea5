import bst
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from resizeimage import resizeimage

def pintaArbol():
    miarbol.outputTreeImage()
    treeImage = resizeimage.resize_contain(Image.open('currentTree.jpg'), [1000, 1000])
    treePhoto = ImageTk.PhotoImage(treeImage)
    treeLabel.config(image = treePhoto)
    treeLabel.image = treePhoto

    treeLabel.pack()

def insertClicked():
    if(miarbol.insert(int(inputField.get()))):
        if( miarbol.root.right is not None or miarbol.root.left is not None):
            pintaArbol()
    else:
        messagebox.showwarning('Nodo Repetido', 'Se intentó insertar un nodo que ya existía')
    inputField.delete(0,-1)

def deleteClicked():
    if(miarbol.delete(int(inputField.get()))):
        pintaArbol()
    else:
        messagebox.showwarning('Nodo Repetido', 'Se intentó eliminar un nodo que no existe')
    inputField.delete(0,-1)

def findClicked():
    if(miarbol.find(int(inputField.get()))):
        messagebox.showinfo('Nodo Encontrado','Se encontró el nodo que buscabas!')
    else:
        messagebox.showwarning('Nodo no Encontrado', 'No se encontró el nodo que buscabas!')
    inputField.delete(0,-1)

def clearClicked():
    miarbol.clear()
    pintaArbol()
    inputField.delete(0,-1)

#initialize
window = Tk()
cosasFrame = Frame(window)
miarbol = bst.ArbolB()
#config
window.title("Hello")
window.geometry('500x500')

#frames


#create widgets
#Buttons: insert, find, delete, clear
buttonsFrame = Frame(cosasFrame)

btnInsert = Button(buttonsFrame, text = 'insertar', command = insertClicked)
btnDelete = Button(buttonsFrame, text = 'eliminar', command = deleteClicked)
btnFind = Button(buttonsFrame, text = 'encontrar', command = findClicked)
btnClear = Button(buttonsFrame, text = 'clear', command = clearClicked)

btnInsert.pack(side = TOP)
btnDelete.pack()
btnFind.pack()
btnClear.pack()
buttonsFrame.pack(side = BOTTOM)

#txtFields: input
inputFrame = Frame(cosasFrame)

inputLabel = Label(inputFrame, text = 'Dato: ')
inputField = Entry(inputFrame, width = 10)

inputLabel.pack(side = LEFT)
inputField.pack(side = RIGHT)
inputFrame.pack()

#tree
treeFrame = Frame(window, height = 100, width = 100)

treeLabel = Label(treeFrame, image = None)

treeLabel.pack()

#organize
treeFrame.pack(side = LEFT)
cosasFrame.pack(side = RIGHT)

#run
window.mainloop()
