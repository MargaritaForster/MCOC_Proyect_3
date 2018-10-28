#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 16:18:16 2018

@author: fernandaordonez
"""

yc = 1.5 #metros
B = 3.5 #metros
ss = 0.0014 #metros
n = 0.012 #concreto
g = 9.80665 #metros/s**2 

yc = 1.5
yc2 = 0
tol = abs(yc2-yc)

while (tol > (1/10**6)):
    
    A = B*yc + ss*(yc**2)
    P = B + 2*yc*(ss**2 + 1)**(0.5)
    R = A/P
    V = (1/n)*R**(2/3)*ss**(0.5)
    Q = V*A
    E = yc + (Q**2)/(2*A**(2)*g)
    
    Tc = B + 2*ss*yc
    dTc = 2*ss
    dE = 1 - (Q**2)*Tc/(g*A**(3))
    
    f = A**3/Tc - (Q**2)/g
    df = 3*A**(2) - A**(3)*2*ss/(Tc**2)
    
    yc2 = yc - f/df
    
    tol = abs(yc2-yc)
    yc = yc2
    
    