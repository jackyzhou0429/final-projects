# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 03:46:11 2022

@author: ALIENWARE
"""

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tkinter import *
from tkinter.ttk import *

days=100  
beta=1
sigma=1
gamma=0.1

'''
the inital value for the parameter:
    the number of days is 100
    beta is 1
    sigma is 1
    gamma is 0.1
'''

def seir_m(t, y, beta, sigma, gamma):   
    S, E, I, R= y
    dSdt=-beta*I*S
    dEdt=-sigma*E+beta*I*S
    dIdt=-gamma*I+sigma*E
    dRdt=gamma*I
    return dSdt, dEdt, dIdt, dRdt
''' 
this is the differential equation for seir model
this function will return the differential equation which will be solved later.

'''

# R0=beta*s0/gamma

import tkinter as tk # import tkinter model to create the interactive window
window = tk.Tk() # create a window
window.title('simulation for COVID-19')
window.geometry('1000x700') # basic setting of the window
label= tk.Label(text='simulated graph for COVID-19',font=('Arial',25),
                 width=33,height=1)
label.pack()
'''
create a label, set the width height and font and show it on the window
'''


class interface:
    '''
    this interface class will generate two frames: frame 1 and frame 2 on the window.
    In frame 1, the user can select the enter the parameter they want to enter : 
        the number of days 
        beta
        sigma
        gamma
    then they can apply the change of the 
    In frame 2, the user can choose which type of garph to show. 
    if the button is clicked, a new window will appear to show the graph. 
    '''
    def __init__(self, master):
        self.days=days   
        self.beta=beta
        self.sigma=sigma
        self.gamma=gamma
        
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
        
        label_size=tk.Label(master=frame_1, text="the number of days:",foreground="black",font=('Calibri',10))
        label_size.place(x=0,y=60)
        
        label_beta=tk.Label(master=frame_1, text="the value of beta:",foreground="black",font=('Calibri',10))
        label_beta.place(x=0,y=160)
        
        label_sigma=tk.Label(master=frame_1, text="the value of sigma:",foreground="black",font=('Calibri',10))
        label_sigma.place(x=0,y=260)
        
        label_gamma=tk.Label(master=frame_1, text="the value of gamma:",foreground="black",font=('Calibri',10))
        label_gamma.place(x=0,y=360)
        
        btn = tk.Button(master=frame_2,
             text ="Click to open the line graph",
             command = self.openNewWindow)
        btn.place(x=0,y=200)
        
        btn = tk.Button(master=frame_2,
             text ="Click to open the pie chart",
             command = self.openPieWindow)
        btn.place(x=0,y=300)
        
        b_plot=tk.Button(master=frame_2,text='show picture',width=15,height=2,command=self.graph)
        b_plot.place(x=0,y=0)
        
        
    def insert_size(self):
        var=self.e1.get()
        self.days=int(var)

    def insert_beta(self):
        var=self.e2.get()
        self.beta=float(var) 
        
    def insert_sigma(self):
        var=self.e3.get()
        self.sigma=float(var) 

    def insert_gamma(self):
        var=self.e4.get()
        self.gamma=float(var) 
    
    def graph(self):
        sol = solve_ivp(seir_m, [0,self.days], [0.99, 0.01, 0, 0], 
                    rtol=1e-6, args=(self.beta, self.sigma, self.gamma))
        
        fig = plt.figure(); ax = fig.gca()
        lines = ax.plot(sol.t, sol.y.T)
        ax.legend(lines, ['S', 'E', 'I', 'R']);
        ax.set_xlabel('days')
        ax.set_ylabel('proportion of all')
        return plt.gcf()
    
    def openNewWindow(self):
        global newWindow
        newWindow = tk.Toplevel(window)
        newWindow.title("Line graph for simulation")
        
        global frame_x
        frame_x =tk.Frame(newWindow)
        frame_x.pack(fill='both', side='left')
        
        sol = solve_ivp(seir_m, [0, self.days], [0.99, 0.01, 0, 0], 
                    rtol=1e-6, args=(self.beta, self.sigma, self.gamma))
        s, e, i, r = sol.y
        
        x=len(sol.t)
        
        fig= plt.Figure() 
        axes = fig.add_subplot(111)
        axes.set_ylim(0, 1.1)
        axes.set_xlim(0, self.days)
        line, =axes.plot(0, 0.99)
        line1, =axes.plot(0, 0.01)
        line2, =axes.plot(0, 0)
        line3, =axes.plot(0, 0)
        plt.style.use("ggplot")
        axes.legend(['S', 'E', 'I', 'R']);
        axes.set_xlabel('days')
        axes.set_ylabel('proportion of all')
        axes.set_title('Animation line graph for SEIR model')
        x1, y1, y2, y3, y4 = [], [], [], [], []
        
        def animate(a):
            x1.append((sol.t[a]))
            y1.append((s[a]))
            y2.append((e[a]))
            y3.append((i[a]))
            y4.append((r[a]))
            
            line.set_xdata(x1)
            line.set_ydata(y1)
            line1.set_xdata(x1)
            line1.set_ydata(y2)
            line2.set_xdata(x1)
            line2.set_ydata(y3)
            line3.set_xdata(x1)
            line3.set_ydata(y4)
            
            return line, line1, line2, line3, 
        canvas = FigureCanvasTkAgg(fig, master=frame_x)
        canvas.get_tk_widget().grid(column=0,row=1)
    
        anim = animation.FuncAnimation(fig, animate, np.arange(1, x), interval=25, repeat=False)
    
        newWindow.mainloop()
        
    def openPieWindow(self):
        '''
        This function helps to open a new window where it shows the SEIR percentage of total Suspectable cases with different sets of data.
        '''
        #Create a new window what shows the pie chart animation
        global piewindow 
        piewindow = tk.Toplevel(window)
        piewindow.title("Pie chart for stimulation")
        
        #Create a new frame on the window
        frame_1 =tk.Frame(piewindow)
        frame_1.pack(fill='both', side='left')
        
        #Solve the differenial equation with the given input by the user.
        sol = solve_ivp(seir_m, [0, self.size], [0.99, 0.01, 0, 0], 
                    rtol=1e-6, args=(self.beta, self.sigma, self.gamma))
        
        #Create fours lists for different types of results.
        s, e, i, r = sol.y
        
        #Plot the pie chart
        fig, ax = plt.subplots()
        
        #Find the index posistions of element '0' in order to clear them later on.
        def searchzero(list):
            '''
            Find the index(es) of number 0 in the list
            '''
            #Create a list where it contains all indexes of 0.
            zeroindex = []
            for i in range(len(list)):
                if list[i] == 0:
                    zeroindex.append(i)
            return zeroindex
            
        
        def changingpie(num):
            '''
            This function helps to show the SEIR percentage of total Suspectable cases with different sets of data.
            '''
            # make sure previous axis data were wiped so that the new pie chart won't be messed up.
            ax.clear() 
            
            #Create lists of all variables needed for the pie chart animation.
            nums = [s[num], e[num], i[num], r[num]]
            labels = ['S', 'E', 'I', 'R']
            colors = ['gold', 'green', 'violet', 'royalblue']
            zeroindex = []
            
            #Find 0 indexes
            for m in range(len(nums)):
                if nums[m] == 0:
                    zeroindex.append(m)
                    
            #Reverse the elements inside the list so that lists can remove elemnts from larger indexes to smaller indexes.
            zeroindex1 = zeroindex[::-1]
            
            #Remove all elements coresponded with 0 in nums.
            for k in zeroindex1:
                labels.pop(k)
                colors.pop(k)
                nums.pop(k)
                
            #Create a pie chart with certain value.
            ax.pie(nums, labels=labels, colors=colors, autopct='%.2f%%', shadow = False, normalize = True)
            ax.set_title('SEIR proportion for a certain Suspectable group')
            
        #Create a canvas so that function annimation can be shown on it. 
        canvas = FigureCanvasTkAgg(fig, master=frame_1)
        canvas.get_tk_widget().pack()
        
        #Create animation
        ani = animation.FuncAnimation(fig, changingpie, frames=len(s), repeat=False) 
        
        #Repeat checking the input value changes
        piewindow.mainloop()
interface(window)

window.mainloop()