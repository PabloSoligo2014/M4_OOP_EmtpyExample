'''
Created on 22 ago. 2019

@author: pabli
'''
from math import sin, cos, sqrt, atan2, radians
class Geoposicion(object):
    #public #protected #private
    def __init__(self, lat=0.0, lon=0.0):
        if lat<-90 or lat>90:
            raise Exception("invalid...")
        
        
        if lon<-180 or lon>180:
            raise Exception("invalid...")
            
        self.__lat = lat
        self.__lon = lon
    
    
    def set_lat(self, value):
        if value<-90 or value>90:
            raise Exception("invalid...")
        self.__lat = value
        
    def set_lon(self, value):
        if value<-180 or value>180:
            raise Exception("invalid")
        self.__lon = value
        
        
    def get_lat(self):
        return self.__lat
    
    def get_lon(self):
        return self.__lon
    
    def __sub__(self, other):
        return self.distance(other)
        
    def __repr__(self):
        return str(self.__lat)+", "+str(self.__lon)
    
    def distance(self, other):
        #Distancia entre dos puntos 
        R = 6373.0

        lat1 = radians( self.__lat )
        lon1 = radians( self.__lon )
        
        lat2 = radians( other.get_lat() )
        lon2 = radians( other.get_lon() )

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = R * c
        
        return distance
    
    
    def render(self, canvas):
        x0 = int(((self.__lon+180)*canvas.w)/360.0)
        y0 = canvas.h - int(((self.__lat+90)*canvas.h)/180.0)
        midsize = 5
        self._ele = canvas.create_oval(x0-midsize, y0-midsize, x0+midsize, y0+midsize, fill='red')
        return self._ele
        
    
    
        
        