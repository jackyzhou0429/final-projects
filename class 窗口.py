# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 03:46:11 2022

@author: ALIENWARE
"""

import argparse
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

parser = argparse.ArgumentParser(description='epidemic simulation parameter')
parser.add_argument('--size', type=int, default=100, help=" the size of the crowd you want to simulate.")
parser.add_argument('--beta',type=float, default=1, help="beta in SEIR model")
parser.add_argument('--sigma',type=float, default=1, help="sigma in SEIR model")
parser.add_argument('--gamma',type=float, default=0.1, help="gamma in SEIR model")
args = parser.parse_args()

if __name__ =='__main__':
    print(args.beta)

size=args.size   
beta=args.beta
sigma=args.sigma
gamma=args.gamma

def seir_m(t, y, beta, sigma, gamma):   
    S, E, I, R= y
    dSdt=-beta*I*S
    dEdt=-sigma*E+beta*I*S
    dIdt=-gamma*I+sigma*E
    dRdt=gamma*I
    return dSdt, dEdt, dIdt, dRdt


sol = solve_ivp(seir_m, [0,size], [0.99, 0.01, 0, 0], 
                rtol=1e-6, args=(beta, sigma, gamma))


fig = plt.figure(); ax = fig.gca()
lines = ax.plot(sol.t, sol.y.T)
ax.legend(lines, ['S', 'E', 'I', 'R']);
ax.set_xlabel('days')
ax.set_ylabel('proportion of all')
plt.show()
    
def graph():
    sol = solve_ivp(seir_m, [0,size], [0.99, 0.01, 0, 0], 
                rtol=1e-6, args=(beta, sigma, gamma))
    
    fig = plt.figure(); ax = fig.gca()
    lines = ax.plot(sol.t, sol.y.T)
    ax.legend(lines, ['S', 'E', 'I', 'R']);
    ax.set_xlabel('days')
    ax.set_ylabel('proportion of all')
    return plt.gcf()

# R0=beta*s0/gamma

import tkinter as tk
window = tk.Tk()
window.title('simulation for COVID-19')
window.geometry('1000x700')
label= tk.Label(text='simulated graph for COVID-19',font=('Arial',25),
                 width=33,height=1)
label.pack()

class interface:
    def __init__(self, master):
        frame_1 = tk.Frame(master, width=550, height=600)
        frame_1.pack(fill='both', side='left')

        frame_2 = tk.Frame(master, width=450, height=600)
        frame_2.pack(fill='both', side='right')

        label_tit=tk.Label(master=frame_1, text="select the parameter below:",foreground="black",font=('Calibri',20))
        label_tit.place(x=0,y=0)

        self.e1=tk.Entry(master=frame_1,show=None)
        self.e1.place(x=170,y=65)
        
        self.e2=tk.Entry(master=frame_1,show=None)
        self.e2.place(x=170,y=165)
        
        self.e3=tk.Entry(master=frame_1,show=None)
        self.e3.place(x=170,y=265)
        
        self.e4=tk.Entry(master=frame_1,show=None)
        self.e4.place(x=170,y=365)
        
        b_size=tk.Button(master=frame_1,text='apply',width=15,height=2,command=self.insert_size)
        b_size.place(x=360,y=50) 
        
        b_beta=tk.Button(master=frame_1,text='apply',width=15,height=2,command=self.insert_beta)
        b_beta.place(x=360,y=150)  
        
        b_sigma=tk.Button(master=frame_1,text='apply',width=15,height=2,command=self.insert_sigma)
        b_sigma.place(x=360,y=250)
        
           
        b_gamma=tk.Button(master=frame_1,text='apply',width=15,height=2,command=self.insert_gamma)
        b_gamma.place(x=360,y=350)
        
        label_size=tk.Label(master=frame_1, text="the size of crowd:",foreground="black",font=('Calibri',10))
        label_size.place(x=0,y=60)
        
        label_beta=tk.Label(master=frame_1, text="the value of beta:",foreground="black",font=('Calibri',10))
        label_beta.place(x=0,y=160)
        
        label_sigma=tk.Label(master=frame_1, text="the value of sigma:",foreground="black",font=('Calibri',10))
        label_sigma.place(x=0,y=260)
        
        label_gamma=tk.Label(master=frame_1, text="the value of gamma:",foreground="black",font=('Calibri',10))
        label_gamma.place(x=0,y=360)
        
        b_plot=tk.Button(master=frame_2,text='show picture',width=15,height=2,command=graph)
        b_plot.place(x=0,y=0)
        
        canvas=tk.Canvas(master=frame_2,width=500, height=500)
        canvas.place(x=0,y=100)
        
    def insert_size(self):
        global size
        var=self.e1.get()
        size=int(var)

    def insert_beta(self):
        global beta
        var=self.e2.get()
        beta=float(var) 
        
    def insert_sigma(self):
        global sigma
        var=self.e3.get()
        sigma=float(var) 

    def insert_gamma(self):
        global gamma
        var=self.e4.get()
        gamma=float(var) 

interface(window)

window.mainloop()