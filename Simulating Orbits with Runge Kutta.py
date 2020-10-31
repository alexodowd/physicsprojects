#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 10:37:05 2020

@author: Alex
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
from prettytable import PrettyTable


G = 6.674e-11
Me = 5.972e24  #mass of the Earth (kg)
rE = 6.371e6   #radius of earth (m)
Mm = 7.348e22  #mass of the Moon (kg)
Mr = 5e3 #mass of the rocket (kg)
rM = 1.737e6 #radius of the moon (m)
d = 3.844e8 # Distance between Earth and the Moon (m)


#dx/dt
def F1(vx):
    return vx

#dy/dt
def F2(vy):
    return vy

#dvx/dt
def F3(x,y):
    return -1 * (Me * x * G) / (((x**2)+(y**2))**(3/2))

#dvy/dt
def F4(x,y):
    return -1 * (Me * y * G) / (((x**2)+(y**2))**(3/2))

#dvx/dt including influence of the Moon

def F5(x,y):
    return (-1*(Mm * (x-d) * G) / ((((x-d)**2)+(y**2))**(3/2))) + (-1 * (Me * x * G) / (((x**2)+(y**2))**(3/2))) 

#dvy/dt including influence of the Moon

def F6(x,y):
    return (-1*(Mm * y * G) / ((((x-d)**2)+(y**2))**(3/2))) + (-1 * (Me * y * G) / (((x**2)+(y**2))**(3/2)))



def Exercise_4():
    
    t0 = 0
    t1 = 1.85e4
        
    print("""
          
    Welcome to Alex's Rocket Orbit Simulator!
    
          
    Please select which body you wish your rocket to orbit (enter 1 or 2):
        
        \n 1. Earth 
        \n 2. Moon""")
    choice = input()
    
    if choice == "1":
        

    # Starting Coordinates (x,y)

        print("""
        Please enter initial coordinates for your rocket (units are in m):
            (I reccommend starting with x = 7x10^6 and y = 0)""")
        
        x0 = input("x = ")
        y0 = input("y = ")
        
                   
        # Starting Velocities (x,y)
        
        print("""
        Please enter initial velocities along the x and y axis (units are in m/s)
        (If the previously reccommended altitude is set then start with x = 0, y = 7500)""")
        
        vx0 = input("Vx = ")
        vy0 = input("Vy = ")
        
        print('''
              Calculating orbit...
              ''')
        
        h = 1 

        N=int(t1-t0/h)
        
        
        x, y, vx, vy, t, Ek, Ep, Et = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)
        
        x[0] = x0
        y[0] = y0
        vx[0] = vx0
        vy[0] = vy0
        t[0] = 0
        
        r = np.hypot(x,y)           # x and y coordinates compounded in a single position variable 'r'
        v = np.hypot(vx,vy)         # Velocities in the x and y directions compounded in single variable 'v'
        r[0] = np.hypot(x[0],y[0])
        v[0] = np.hypot(vx[0],vy[0])
        
        #Energy
        Ek[0] = Mr*(v[0]**2)/2 #Kinetic energy (1/2MV**2)
        Ep[0] =  -Me*Mr*G/r[0] #Gravitational potential energy (-GMm/r)
        Et[0] = Ek[0]+Ep[0] #Total energy is the sum of these two
        

        # Part A RK4 Implementation
        for i in range (0, N-1):
            
            #1
            
            k1x = F1(vx[i])
            k1y = F2(vy[i])
            k1vx = F3(x[i],y[i])
            k1vy = F4(x[i],y[i])
            
            #2
            
            k2x = F1(vx[i] + h * 0.5 * k1vx)
            k2y = F2(vy[i] + h * 0.5 * k1vy)
            k2vx = F3(x[i] + h * k1x * 0.5, y[i] + h * k1y * 0.5)
            k2vy = F4(x[i] + h * k1x * 0.5, y[i] + h * k1y * 0.5)
            
            #3
            
            k3x = F1(vx[i] + h * 0.5 * k2vx)
            k3y = F2(vy[i] + h * 0.5 * k2vy)
            k3vx = F3(x[i] + h * k2x * 0.5, y[i] + h * k2y * 0.5)
            k3vy = F4(x[i] + h * k2x * 0.5, y[i] + h * k2y * 0.5)
            
            #4
            
            k4x = F1(vx[i] + h * k3vx)
            k4y = F2(vy[i] + h * k3vy)
            k4vx = F3(x[i] + h * k3x, y[i] + h * k3y)
            k4vy = F4(x[i] + h * k3x, y[i] + h * k3y)
            
            x[i+1] = x[i] + (h/6) * (k1x + 2 * k2x + 2 * k3x + k4x)
            y[i+1] = y[i] + (h/6) * (k1y + 2 * k2y + 2 * k3y + k4y)
            vx[i+1] = vx[i] + (h/6) * (k1vx + 2 * k2vx + 2 * k3vx +k4vx)
            vy[i+1] = vy[i] + (h/6) * (k1vy + 2 * k2vy + 2 * k3vy + k4vy) 
            t[i+1] =  t[i] + h
            r[i+1] = np.hypot(x[i+1],y[i+1])
            v[i+1] = np.hypot(vx[i+1],vy[i+1])
            
            
            #Energy
            
            Ek[i+1] = 0.5*Mr*(v[i+1]**2)    # Ek, Ep and total energy of the rocket for i+1 iterations
            Ep[i+1] = (-1*Mr*Me*G)/r[i+1]
            Et[i+1] = Ek[i+1] + Ep[i+1]
        
        if min(r) <= rE :
            print("""
                  "Your rocket has crashed!""")   # Crash Test
        else:
            print("""                    --------------------------
                       "Successful Flight!
                    --------------------------""")
        
        print("""
                    
                        DATA""")
        
        apsides = PrettyTable(['Min. Altitude (m)','Periapsis (m)','Apoapsis (m)'])
        apsides.add_row(['{:.3}'.format(min(r)-rE),'{:.3}'.format(min(r)),'{:.3}'.format(max(r))])
        print(apsides)
        
                #Plotting
        
        fig1,ax1 = plt.subplots()
        ax1.set_title('Rocket orbit of Earth') 
        ax1.set_xlabel('x position (m)')  
        ax1.set_ylabel('y position (m)')  
        ax1.plot(x,y, color = 'red')
        
        ax1.axis('equal')
        earth = plt.Circle([0,0], rE, color = 'teal')
        ax1.add_artist(earth)
        
        ax1.set_xlim([-2*rE,+2*rE])
        ax1.set_ylim([-2*rE,+2*rE])
        
        fig2,ax2 = plt.subplots()
        ax2.set_title('Energy analysis of a rocket orbiting Earth')
        ax2.set_xlabel('Time (s)')
        ax2.set_ylabel('Energy  (J)')
        ax2.plot(t,Ek, label = 'Kinetic Energy', color = 'lime')
        ax2.plot(t,Ep, label = 'Potential Energy', color = 'cyan')
        ax2.plot(t,Et, label = 'Total Energy', color = '#F700FF')
        ax2.legend()
        
        plt.show()
        
        Exercise_4()
           
    if choice == "2":
        
        h = 50
        N=int(t1-t0/h)
        
        x, y, vx, vy, Ek, Ep, Et, t = np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N), np.zeros(N)
        
        print("""
        Please enter initial coordinates for your rocket:""")
        
        x0 = input("x = ")
        y0 = input("y = ")
        
                   
        # Starting Velocities (x,y)
        
        print("""
        Please enter initial velocities along the x and y axis""")
        
        vx0 = input("Vx = ")
        vy0 = input("Vy = ")
        
        print('''
              Calculating orbit...
              ''')
        
        x[0] = x0
        y[0] = y0
        vx[0] = vx0
        vy[0] = vy0
        
        r = np.hypot(x,y)           # x and y coordinates compounded in a single position variable 'r'
        v = np.hypot(vx,vy)         # Velocities in the x and y directions compounded in single variable 'v'
        r[0] = np.hypot(x[0],y[0])
        v[0] = np.hypot(vx[0],vy[0])
        
        #Energy
        Ek[0] = Mr*(v[0]**2)/2 #Kinetic energy (1/2MV**2)
        Ep[0] =  -Mm*Mr*G/r[0] #Gravitational potential energy (-GMm/r)
        Et[0] = Ek[0]+Ep[0] #Total energy is the sum of these two
        
        # Part B RK4 Implementation 
        
        for i in range (0, N-1):
            
            #1
            
            k1x = F1(vx[i])
            k1y = F2(vy[i])
            k1vx = F5(x[i],y[i])
            k1vy = F6(x[i],y[i])
            
            #2
            
            k2x = F1(vx[i] + h * 0.5 * k1vx)
            k2y = F2(vy[i] + h * 0.5 * k1vy)
            k2vx = F5(x[i] + h * k1x * 0.5, y[i] + h * k1y * 0.5)
            k2vy = F6(x[i] + h * k1x * 0.5, y[i] + h * k1y * 0.5)
            
            #3
            
            k3x = F1(vx[i] + h * 0.5 * k2vx)
            k3y = F2(vy[i] + h * 0.5 * k2vy)
            k3vx = F5(x[i] + h * k2x * 0.5, y[i] + h * k2y * 0.5)
            k3vy = F6(x[i] + h * k2x * 0.5, y[i] + h * k2y * 0.5)
            
            #4
            
            k4x = F1(vx[i] + h * k3vx)
            k4y = F2(vy[i] + h * k3vy)
            k4vx = F5(x[i] + h * k3x, y[i] + h * k3y)
            k4vy = F6(x[i] + h * k3x, y[i] + h * k3y)
            
            x[i+1] = x[i] + (h/6) * (k1x + 2 * k2x + 2 * k3x + k4x)
            y[i+1] = y[i] + (h/6) * (k1y + 2 * k2y + 2 * k3y + k4y)
            vx[i+1] = vx[i] + (h/6) * (k1vx + 2 * k2vx + 2 * k3vx +k4vx)
            vy[i+1] = vy[i] + (h/6) * (k1vy + 2 * k2vy + 2 * k3vy + k4vy)
            t[i+1] =  t[i] + h
            r[i+1] = np.hypot(x[i+1],y[i+1])
            v[i+1] = np.hypot(vx[i+1],vy[i+1])
            #Energy
            
            Ek[i+1] = 0.5*Mr*(v[i+1]**2)    # Ek, Ep and total energy of the rocket for i+1 iterations
            Ep[i+1] = (-1*Mr*Me*G)/r[i+1]
            Et[i+1] = Ek[i+1] + Ep[i+1]
            
        param = PrettyTable(['Min. Altitude above Earth (m)','Min. Altitude above Moon (m)'])
        param.add_row(['{:.3}'.format(min(r)-rE),'{:.3}'.format(min(abs(d-r))),])
        print(param)
        
        
        fig3,ax3 = plt.subplots()
        ax3.set_title('Rocket Orbit of the Moon')
        ax3.set_xlabel('Horizontal displacement')
        ax3.set_ylabel('Vertical displacement')
        ax3.plot(x,y, color = 'red')
        ax3.set_xlim([-5*rE,+1.2*d])
        ax3.set_ylim([-0.5*d,+0.5*d])
        earth = plt.Circle([0,0], rE, color = 'teal')
        moon = plt.Circle([d,0], rM, color = 'white')
        ax3.add_artist(earth)
        ax3.add_artist(moon)
        
        fig4,ax4 = plt.subplots()
        ax4.set_title('Energy analysis of Rocket Orbit of the Moon')
        ax4.set_xlabel('Time (s)')
        ax4.set_ylabel('Energy (J)')
        ax4.plot(t,Ek, label = 'Kinetic Energy', color = 'lime')
        ax4.plot(t,Ep, label = 'Potential Energy', color = 'cyan')
        ax4.plot(t,Et, label = 'Total Energy', color = '#F700FF')
        ax4.legend()

        plt.show()
            
        Exercise_4()

Exercise_4()
