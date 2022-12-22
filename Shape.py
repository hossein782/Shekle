# Auto detect text files and perform LF normalization
* text=auto
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 02:28:03 2022

@author: Hossein782
"""

import math
from point import Point
class Shape:
    def __init__ (self,x,y,r,c=Point(0,0),color):
        self.__x=x
        self.__y=y
        self.__r=r
        self.__a=a
        self.__b=b
        self.__color=color
#تعیین دایره یا مربع بودن
        if(r>0):
            self.type='circle'
        else:
            self.type='square'  
#محاسبه مساحت
    def area (self):
        if self.type== 'circle':
            return(3.14*self.__r*self.__r)
        else:
            return(self.__x*self.__y)
        
#محاسبه محیط
    def perimeter (self):
        if self.type=='circle':
            return(2*3.14*self.__r)
        elif (self.__x) != (self.__y):
            
#فاصله شکل تا مرکز
    def distance (self):
        return math.sqrt((self.__x)^2+(self.__y)^2)
    
#فاصله شکل با شکل دیگر
    def distancefrom (self,point.__x,point.__y):
        return math.sqrt((self.__x-point.__x)^2+(self.__y-point.__y)^2)

#داخل بودن شکل با شکل دیگر
    def isinside (self,point.__x,point.__y,p.r):
        if self.type=='circle':
            self.plus=(self.__r)+(p.r)
            self.dplus = math.sqrt((self.__x-point.__x)^2+(self.__y-point.__y)^2)
            if (self.plus - self.dplus) <= 0:
                return True
            else:
                return False
        else:
            return "Goodbye for now!!!"