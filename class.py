#y = ax^2 + bx + c
import matplotlib.pyplot as plt
import math
import matplotlib.patches as pat
import numpy as np

class Equation:

    def __init__(self, a, b, c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        

    def serch_root(self):
       
        D = self.b**2 - (4 * self.a * self.c)
        print(D)

        if D == 0:
            x = -1*((self.b)/(2*self.a))
            print("корень уравнения x =",x)
        elif D > 0:
            x1 = ((-1*(self.b))+D)/(2*self.a)
            x2 = ((-1*(self.b))-D)/(2*self.a)
            print(f"корни уравнения x1 = {x1} и x2 = {x2}")
        elif D < 0:
            print("нет корней")

    def matplt(self):

        fig, self.ax = plt.subplots()
        #self.ax.set_aspect('equal')
        
        y = []
        x = []

        for i in range(-10,10):
            
            y1 = self.a * i**2 + self.b * i + self.c

            x.append(i)
            y.append(y1)

        self.ax.plot(x, y, label='парабола')
        plt.legend()

    def matplt_fin(self):
        self.matplt()

        plt.grid()
        plt.legend()
        plt.show()


    def __del__(self): #деструктор
        print("del done")

class Derivative:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        

    def matplt(self):
        fig, self.ax = plt.subplots()
        #self.ax.set_aspect('equal')
        
        y = []
        x = []

        for i in range(0,10):
            
            y1 = 2 * self.a * i + self.b

            x.append(i)
            y.append(y1)

        self.ax.plot(x, y, label='линейная')
        
    
    def __del__(self): #деструктор
        print("del done")

class Integral:

    def __init__(self, a, b, c, d):
        super().__init__(a,b,c)
        self.d = int(d)

    def matplt(self):
        fig, self.ax = plt.subplots()
        #self.ax.set_aspect('equal')
        
        y = []
        x = []

        for i in range(0,10):
            
            y1 = ((self.a * (i**3))/3) + ((self.b * (i**2))/2) + self.c * i + self.d

            x.append(i)
            y.append(y1)

        self.ax.plot(x, y, label='линейная')

    
    def __del__(self): #деструктор
        print("del done")

class Funk(Integral, Derivative):
    def __init__(self, a, b, c, d):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
        self.d = int(d)
       

    def matplt1(self):
        Equation.matplt_fin(self)
        Derivative.matplt(self)
        Integral.matplt(self)
    



a = input("коэф а")
b = input("коэф б")
d = input("коэф d")
c = input("коэф с")
matp = Funk(a, b, c, d)
matp.matplt1()



    