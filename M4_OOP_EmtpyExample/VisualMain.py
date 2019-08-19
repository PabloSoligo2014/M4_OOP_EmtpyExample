'''
Created on 16 ago. 2019

@author: pabli
'''

import time

from tkinter import Tk, Canvas, Label, PhotoImage, Frame, NW, CENTER
from random import randrange
from _datetime import datetime
from tkinter.constants import ANCHOR


class Application(Frame):
    __canvas = None
    def __init__(self, master=None, elements=None):
        Frame.__init__(self, master)
        self.root = master
        self.root.resizable(width=False, height=False)
        self.root.title('Simulacion')
        background_image = PhotoImage(file="world3.png")
        
        w = background_image.width()
        h = background_image.height()
        self.__background_image = background_image        
        self.__canvas = Canvas(self.root, width=w, height=h)
        self.__canvas.h = h
        self.__canvas.w = w
        #self.__canvas.create_text((20, 20), text="Hola que tal", fill="black", anchor="nw")
        self.__canvas.create_image(0, 0, image=background_image, state="normal", anchor=NW)
        self.__canvas.pack()
        self._elements = elements
        self.createWidgets()

    def createWidgets(self):
        self.onUpdate()
        
    def onUpdate(self):
        # update displayed time
        #self.now.set(str(datetime.utcnow()))
        self.root.title(str(datetime.utcnow()))
        for ele in self._elements:
            ele.render(self.__canvas)
        # schedule timer to call myself after 1 second
        #car_image = PhotoImage(file="car.png")
        #self.__canvas.create_image(60, 60, image=car_image)
        
        self.after(1000, self.onUpdate)


if __name__ == '__main__':
    elements = []
    root = Tk()
    app = Application(master=root, elements=elements)
    root.mainloop()