#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:27:59 2019

@author: Alex
"""
#INVESTIGATING FREEFALL USING THE EULER METHOD

#-----------------------------------------------------------
#PART A
#-----------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

y0 = 1000
m = 70
k = 0.207
g = 9.8

NumPoints = 200

t0 = 0.0
t = 30

time = np.linspace(t0,t,NumPoints) 
height = np.zeros(NumPoints)

for i in range(NumPoints):
    
    height[i] = y0 - (m/k)*np.log(np.cosh((time[i])*(k*g/m)**(0.5)))
    
plt.title("Analytical prediction of height versus time")
plt.plot(time,height)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')

plt.show()

m = 70
k = 0.207
g = 9.8

NumPoints = 200

t0 = 0.0
t = 30

time = np.linspace(t0,t,NumPoints) 
vel = np.zeros(NumPoints)

for i in range(NumPoints):
    
    vel[i] = - ((m*g/k))**(0.5)*np.tanh((time[i])*(k*g/m)**(0.5)) #+ve(^)

plt.title("Analytical prediction of velocity versus time")
plt.plot(time,vel)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')

plt.show()

#-----------------------------------------------------------
#PART B
#-----------------------------------------------------------

y = 1000 #initialised variables
v = 0 
t = 0
dt = 1

# listed in height, velocity and time

height = [y]
velocity = [v]
time = [t] 

#algorithm, using a while loop to stop the simulation at y=0

while(y > 0):
    
    y = y + dt*v
    v = v - dt*(g+(k/m)*(abs(v)*v))
    t = t + dt
    
    height.append(y)
    velocity.append(v)
    time.append(t)
    
    #append function adds each iteration to the end of the lists height, velocity and time
    

plt.title("Height versus time using Euler Method (fixed drag)")
plt.plot(time, height)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()

plt.title("Velocity versus time using Euler Method (fixed drag)")
plt.plot(time, velocity)
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()

#-----------------------------------------------------------
#PART C
#-----------------------------------------------------------

y = 39045
v = 0
t = 0
dt = 1


def p(): #function definition for changing air density
    
    p0 = 1.2
    h = 7640
    
    return p0*np.exp(-y/h)

def k(): #funtion definition for the air resistance constant k
    
    Cd = 1.15
    A = 0.3
    
    return Cd*A*p()/2

height = [y]
velocity = [v]
time = [t] 


while(y > 0):
    
    y = y + dt*v
    v = v - dt*(g+(k()/m)*(abs(v)*v))
    t = t + dt
    
    height.append(y)
    velocity.append(v)
    time.append(t)

plt.title("Height with variable drag")
plt.plot(time, height)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()

plt.title("Velocity with variable drag")
plt.plot(time, velocity)
plt.plot([0, 350], [-343, -343])
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.show()
