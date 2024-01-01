import matplotlib.pyplot as plt
import numpy as np  
from scipy import optimize
import math

a = 1
b = 1

##### medodes estocastics#####
if(a == 1 and b == 1):
     r = 0.572915
     tf = 2.412
elif(a == 4 and b == 2):
     r = 1.0344
     tf = 3.508365
##############################

t = np.linspace(0, tf, 500)
x = r*(t-np.sin(t))
y = r*(1-np.cos(t))

def read_solution(document):
     with open(document, mode='r', encoding='utf-8') as file:
          lines = file.readlines()

     x = [float(eval(i)) for i in lines[0].split(',')]
     y = [float(eval(i)) for i in lines[1].split(',')]

     return x, y

x1, y1 = read_solution("mod1/solucio_1.txt")
x2, y2 = read_solution("mod2/solucio_2.txt")
x3, y3 = read_solution("mod3/solucio_3.txt")

plt.gca().invert_yaxis()
plt.axhline(color='grey')
plt.axvline(color='grey')
plt.plot(x1,y1,'g',label="model 1")
plt.plot(x2,y2,'r',label="model 2")
plt.plot(x3,y3,'b',label="model 3")
plt.plot(x,y,'y',label="cicloide")
plt.legend()
plt.show()