# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:03:02 

@author: ALIENWARE
"""
import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


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


sol = solve_ivp(seir_m, [0, args.size], [0.99, 0.01, 0, 0], 
                rtol=1e-6, args=(args.beta, args.sigma, args.gamma))

fig = plt.figure(); ax = fig.gca()
curves = ax.plot(sol.t, sol.y.T)
ax.legend(curves, ['S', 'E', 'I', 'R']);
ax.set_xlabel('days')
ax.set_ylabel('proportion of all')


#pie chart animation
from matplotlib.animation import FuncAnimation
s, e, i, r = sol.y   #Create lists for SEIR from solve_ivp solution above.
labels = ['S', 'E', 'I', 'R']
colors = ['gold', 'green', 'violet', 'royalblue']
fig, ax = plt.subplots()

def changingpie(num):
    '''
    This function helps to show the SEIR percentage of total Suspectable cases with different sets of data.
    '''
    ax.clear() # make sure previous axis data were wiped so that the new pie chart won't be messed up.
    nums = [s[num], e[num], i[num], r[num]]
    ax.pie(nums, labels=labels, colors=colors, autopct='%.2f%%', shadow = False)
    ax.set_title('SEIR proportion for a certain Suspectable group')

ani = FuncAnimation(fig, changingpie, frames=range(60), repeat=False) 
# Since there are 61 sets of data for each list of SEIR, we set range(60) to run the function 61 times.

plt.show()
#print(len(s))


