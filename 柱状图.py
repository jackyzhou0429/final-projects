import argparse
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *
from tkinter.ttk import *

parser = argparse.ArgumentParser(description='epidemic simulation parameter')
parser.add_argument('--size', type=int, default=100, help=" the size of the crowd you want to simulate.")
parser.add_argument('--beta',type=float, default=1, help="beta in SEIR model")
parser.add_argument('--sigma',type=float, default=1, help="sigma in SEIR model")
parser.add_argument('--gamma',type=float, default=0.1, help="gamma in SEIR model")
args = parser.parse_args()

if __name__ =='__main__':
    print(args.beta)
    
    

def seir_m(t, y, beta, sigma, gamma):   
    S, E, I, R= y
    dSdt=-beta*I*S
    dEdt=-sigma*E+beta*I*S
    dIdt=-gamma*I+sigma*E
    dRdt=gamma*I
    return dSdt, dEdt, dIdt, dRdt

#line graph animation   #Create lists for SEIR from solve_ivp solution above.


    
sol = solve_ivp(seir_m, [0, args.size], [0.99, 0.01, 0, 0], 
         rtol=1e-6, args=(args.beta, args.sigma, args.gamma))
s, e, i, r = sol.y

#print(s)
plt.xticks(np.arange(0, 61, 10))

S = tuple(s)
E = tuple(e)
I = tuple(i)
R = tuple(r)

S = list(s)
E = list(e)
I = list(i)
R = list(r)

#print(S)

P1 = plt.bar(range(len(S)), S, lable = 'S', fc = 'b')
P2 = plt.bar(range(len(S)), E, bottom = S, lable = 'E', fc = 'g')
P3 = plt.bar(range(len(I)), I, bottom = E, lable = 'I', fc = 'y')
P4 = plt.bar(range(len(R)), R, bottom = R, lable = 'R', fc = 'r')

plt.legend((p1[0], p2[0], p3[0], p4[0]), ('S', 'E', 'I', 'R'), low = 4)

plt.legend()
plt.show()
















