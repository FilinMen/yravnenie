#y = ax^2 + bx + c
import matplotlib.pyplot as plt
import math
import matplotlib.patches as pat
import numpy as np

class Equation:

    def __init__(self,a,b,c):

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

        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        
        y = []
        x = []

        for i in range(-10,10):
            
            y1 = self.a * i**2 + self.b * i + self.c

            x.append(i)
            y.append(y1)

        ax.plot(x, y, label='парабола')
        plt.legend()
        plt.show()

    def __del__(self): #деструктор
        print("del done")

def main():

    a = input("коэф а")
    b = input("коэф б")
    c = input("коэф с")
    equation = Equation(a,b,c)
    equation.serch_root()
    equation.matplt()

main()




        



    