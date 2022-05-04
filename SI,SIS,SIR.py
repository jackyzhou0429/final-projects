# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:10:46 2022

@author: 10949
"""
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt


def dySIS(y,t,lamda,mu):
    dy_dt = lamda*y*(1-y) -mu*y
    return dy_dt
def dySIR(y,t,lamda,mu):
    i,s = y
    di_dt = lamda*s*i - mu*i
    ds_dt = -lamda*s*i
    return np.array([di_dt,ds_dt])


#Setting model parameters
number = 1e6 #total population
lamda  = 0.2 #transmission rate  
sigma  = 2.5 #susceptible persons effectively exposed
mu     = lamda/sigma #Daily cure rate
tEND   = 200 #Predicted date length
t      = np.arange(0.0,tEND,1)
i0     = 1e-5 #Initial value of patient ratio
s0     = 1-i0 #Initial value of the vulnerability ratio
y0     = (i0,s0) #Initial values of differential equations

print("lamda={}\tmu={}\tsigma={}".format(lamda,mu,sigma))
      
ySI  = odeint(dySIS, i0, t,args=(lamda,0))
ySIS = odeint(dySIS, i0, t,args=(lamda,mu))
ySIR = odeint(dySIR, y0, t,args=(lamda,mu))
plt.title("Comparing the data models of SI, SIR and SIS")
plt.xlabel('t/days')
plt.axis([0,tEND,-0.1,1.1])
plt.axhline(y=0,ls="--",c='c')
plt.plot(t,ySI,':g', label='i(t)-SI')
plt.plot(t,ySIS, '--g', label='i(t)-SIS')
plt.plot(t,ySIS[:,0],'-r', label='i(t)-SIR')
plt.plot(t,ySIR[:,1],'-b', label='s(t)-SIR')
plt.plot(t,1-ySIR[:,0]-ySIR[:,1], 'm', label='r(t)-SIR')
plt.legend(loc='best')
plt.show()

