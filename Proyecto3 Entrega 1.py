# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:21:07 2018

@author: Chopita Castro
"""

yn = 1.5 #metros
B = 3.5 #metros
ss = 0.0014 #metros
n = 0.012 #concreto

yn = 1.5
yn2 = 0
tol = abs(yn2-yn)

while (tol > (1/10**6)):
    
    A = B*yn + ss*(yn**2)
    P = B + 2*yn*(ss**2 + 1)**(0.5)
    R = A/P
    V = (1/n)*R**(2/3)*ss**(0.5)
    Q = V*A
    
    dA = B + 2*ss*yn  
    dP = 2*(ss**2 + 1)**(0.5)
    
    f = A**(5/3)*P**(-2/3) - (n*Q)/ss**(0.5)
    df = (5/3)*P**(-2/3)*A**(2/3)*dA - (2/3)*A**(5/3)*P**(-5/3)*dP
    
    yn2 = yn - f/df
    
    tol = abs(yn2-yn)
    yn = yn2
    

    







