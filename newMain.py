from Frames.bstFramePlus import *

window = Tk()
window.geometry('1500x500')

bstFrame = AVLFramePlus(window)
bstFrame.pack(fill=BOTH , expand=1)

window.mainloop()
