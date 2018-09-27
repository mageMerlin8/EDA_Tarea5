import bst
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from resizeimage import resizeimage

treeImage = None

def pintaArbol():
    miarbol.outputTreeImage()
    resizeClicked()

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

def resizeClicked(event = None):
    height = treeFrame.winfo_height()
    width = treeFrame.winfo_width() - cosasFrame.winfo_width()
    treeImage = Image.open('currentTree.jpg')
    treeImage = resizeimage.resize_contain(treeImage, [width, height])
    treePhoto = ImageTk.PhotoImage(treeImage)
    treeLabel.config(image = treePhoto)
    treeLabel.image = treePhoto

    treeLabel.pack()


#initialize
window = Tk()
cosasFrame = Frame(window, width = 150)
miarbol = bst.ArbolB()
#config
window.title("Hello")
window.geometry('500x500')


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
treeFrame = Frame(window)
treeFrame.bind("<Configure>", resizeClicked)
treeLabel = Label(treeFrame, image = None)

treeLabel.pack()

#organize
treeFrame.pack(side = RIGHT,fill=BOTH, expand=1)
cosasFrame.pack(side = LEFT)

#run
window.mainloop()
