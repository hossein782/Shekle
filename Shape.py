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
    def __init__ (self,x,y,r,c=Point(a,b),color):
        self.__x=x
        self.__y=y
        self.__r=r
        self.__a=a
        self.__b=b
        self.__color=color
 #تعیین مربع یا دایره بودن        
        if(r>0):
            self.type=circle
        else:
            self.type=square

    def getx (self):
        return self.__x
    def gety (self):
        return self.__y
    def getr (self):
        return self.__r
    def geta (self):
        return self.__a
    def getb (self):
        return self.__b
    def getcolor (self):
        return self.__color
    
#محاسبه مساحت
    def area (self):
        if self.type== circle:
            return(3.14*self.__r*self.__r)
        else:
            return(self.__x*self.__y)
#محاسبه محیط
    def perimeter (self):
        if self.type==circle:
            return(2*3.14*self.__r)
        elif (self.__x) != (self.__y):
#داخل بودن شکل با شکل دیگر
    def isinside (self,p.x,p.y,p.r):
        if self.type==circle:
            self.plus=(self.__r)+(p.r)
            self.dp = math.sqrt((self.__x-p.x)^2+(self.__y-p.y)^2)
            if (self.plus - self.dp) <= 0:
                return True
            else:
                return False
        else:
            return "Goodbye for now!!!"