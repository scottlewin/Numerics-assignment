# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:06:08 2024

@author: sl8924
"""

import numpy as np
import matplotlib.pyplot as plt

#Set up the parameters of the shallow-water equations 
g = 10       # Gravitational acceleration (rounded to 10 for convenience of numbers)
H = 10       # Mean water depth

#Set up discretisation
nx = 200
x = np.linspace(0.0, 1.0, nx)
nt = 1000
dx = 1/nx
dt = 1/nt

#Make initial disturbance of water surface a Gaussian 
eta = 0.5*np.exp(- 100*((x - 1/2))**2)
#Store initial eta value 
eta_initial = eta 
#Initiliase veloctiy (zero everywhere)
u = np.zeros(nx)

#Create lists to store the new values of eta and u 
eta_new = np.zeros(nx)
u_new = np.zeros(nx)

for n in range(nt):
    
    #Calculate new value of eta 
    for j in range(nx-1):
        eta_new[j] = eta[j] - (H * dt / ( 2*dx)) * (u[j+1] - u[j -1])
    #Calculate new value of u 
    for j in range(nx-1):
        u_new[j] = u[j] - g*(dt/(2*dx)) *(eta[j+1]-eta[j-1])
    
    
    #Update eta and u to their new values 
    eta = eta_new
    u = u_new
    
    #Apply periodic boundary conditions
    eta_new[0] =  eta_new[-1]
    u_new[0] =  u_new[-1]
    
    
    #Visualise solution 
    if n % 10 == 0:
        
        plt.figure(figsize=(8, 4))
        plt.plot(x, eta, label='Wave Height')
        plt.plot(x,eta_initial)
        plt.ylim([-1, 1])
        #plt.xlim([0,0.2])
        plt.legend()
        plt.title(f"Time: {n*dt:.2f} s")
        plt.xlabel("x")
        plt.ylabel("Wave height")
        plt.grid()
        plt.show()
