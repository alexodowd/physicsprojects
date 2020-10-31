#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:14:12 2019

@author: Alex
"""
import math

def MyArcTan(x,N):
    arctan = 0
    if abs(x) <= 1:
        for n in range(0,N):
            y = 2*n+1 #abbreviation to make my life easier
            arctan += ((x**y)*(-1)**n/y)
        
    elif abs(x) > 1 and x > 0:
        
        arctan += ((math.pi)/2 - (MyArcTan(1/x, N)))
        
    elif abs(x) > 1 and x < 0:
        
        arctan += ((- math.pi)/2 - (MyArcTan(1/x, N)))
        
    return arctan
    
MyInput = '0'
while MyInput != 'q':
    MyInput = input('Enter a choice, "a", "b", "c" or "q" to quit: ') 
    print('You entered the choice: ',MyInput)
    
    if MyInput == 'a':
        print('You have chosen part (a)')
        Input_x = input('Enter a value for x (floating point number): ') 
        x = float(Input_x)
        Input_N = input('Enter a value for N (positive integer): ')
        N = int(Input_N)
        print('The answer is: ', MyArcTan(x,N))
        
    elif MyInput == 'b':
        print('You have chosen part (b)')
        Input_N = input('Enter a value for N (positive integer: ')
        N = int(Input_N)
        x = -2
        while (x <= 2):
            print(MyArcTan(x,N))
            print(math.atan(x))
            print(math.atan(x) - MyArcTan(x, N))
            x += 0.1 #increment
            
    elif MyInput != 'q':
        print('This is not a valid choice')
        print('You have chosen to finish - goodbye.')