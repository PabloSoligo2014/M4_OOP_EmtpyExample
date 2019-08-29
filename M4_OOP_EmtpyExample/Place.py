'''
Created on 29 ago. 2019

@author: pabli
'''
from Geoposition import Geoposicion

class Place(Geoposicion):
    
    def __init__(self, lat, lon, desc):
        super(Place, self).__init__(lat, lon)
        self.__desc = desc
        
    def get_desc(self):
        return self.__desc
    
    def render(self, canvas):
        x0 = int(((self.get_lon()+180)*canvas.w)/360.0)
        y0 = canvas.h - int(((self.get_lat()+90)*canvas.h)/180.0)
        midsize = 5
        canvas.create_text(x0+midsize, y0+midsize, text=self.__desc)
        canvas.create_rectangle(x0-midsize, 
                                y0-midsize, 
                                x0+midsize, 
                                y0+midsize, 
                                fill='blue')
        return x0, y0