from Frames.bstFrameRotaciones import *

window = Tk()
window.geometry('500x500')
bstFrame = BSTFrameRotaciones(window)
bstFrame.pack(fill=BOTH , expand=1)
window.mainloop()