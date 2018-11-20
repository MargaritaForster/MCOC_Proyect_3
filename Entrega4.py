# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 11:08:49 2018

@author: joaco
"""
import scipy as sp
import numpy as np
from matplotlib import pyplot 

def ynormal(B, ss, n, s0, Q):
    yn = 1.5 #metros
    tol = 1
    
    while (tol > (1.e-6)):
        
        A = B*yn + ss*(yn**2)
        P = B + 2*yn*sp.sqrt(ss**2 + 1)
        R = A/P
        V = (1/n)*(R**(2./3.))*sp.sqrt(s0)
        
        
        dA = B + 2*ss*yn  
        dP = 2*sp.sqrt(ss**2 + 1)
        
        f = (A**(5./3.))*(P**(-2./3.)) - (n*Q)/sp.sqrt(s0)
        df = (5./3.)*(P**(-2./3.))*(A**(2./3.))*dA - (2./3.)*(A**(5./3.))*(P**(-5./3.))*dP
        
         
        yn2 = yn - f/df
        
        tol = abs(yn2-yn)
        yn = yn2
    return yn


def geom(y,B,ss): 
    
    A = B*y + (y**2)*s
    dAdy = B + 2*y*ss
    
    L = y*((ss**2+1)**0.5)
    P = B + 2*L
    dPdy = 2*((ss*2+1)**0.5)
    
    R = A/P
    dRdy = (P**-1)*dPdy - (A/P**2)*dPdy
    
    return A, dAdy, P, dPdy, R, dRdy

#Cacterísticas Canal

N=1000
L=150000
B=100
S=0.001
n=0.045
ss=0
Co=1.485
NC=1
Tfin=600
Tfins=Tfin*60
g=32.2
Q = 250


#Creamos NRalpha 
y1 = 1
beta = 3./5.
tol = 1000
i = 0

def NRalpha(Q,B,ss,n,Co,S): 
    
    while tol > 0.001: 
        i += 1
    
        x = geom(y1,B,ss)
        x[0] = A
        alfa = (n*(x[2]**(2./3.))/(Co*(S**0.5)))**beta
        
        f = A - alfa*(Q**beta)
        dfdy = x[1] - (2./5.)*((n*Q/Co*(S**0.5))**beta)*(x[2]**-beta)*x[3]
    
        y2 = y1 - f/dfdy 
    
        tol = abs(y2-y1)
        y1 = y2 
    return A, y2 




#seccion 2
dx=L/(N-1)
x=[]
for i in range(N):
    x.append(i*dx)
    
#Seccion 3
Q=sp.zeros((N,N))
q=sp.zeros(N)
Y=sp.zeros((N,N))
y=sp.zeros(N)
A=sp.zeros((N,N))
a=sp.zeros(N)
V=sp.zeros((N,N))
v=sp.zeros(N)
q[0:N]=250
y[0:N]=ynormal(B,ss,n,S,q[0])
Q[0]=q
Y[0]=y



a[0:N]=B*y[0]
v[0:N]=q[0]/a[0]
Q[0]=q
Y[0]=y
A[0]=a
V[0]=v 



#Seccion 3
t=0
k=0
while t<Tfin:
    k+=1
    dt=NC*dx/V[k]
    t+=dt
    if t<=150*60:
        Q[k+1,0]=250+750/(np.pi()*(1-np.cos(np.pi()*t/(60*75))))
    else:
        Q[k+1,0]=250
    
    y = NRalpha(Q[k+1,1],B,ss,n,Co,S)
    A[k+1,1] = y[0]
    Y[k+1,1] = y[1]
    V[k+1,1] = Q[k+1,1]/A[k+1,1]
    
    for i in range(N-1): 
        Q[k+1,i+1] = Q[k+1,i]- dt/dx*(A[k+1,i]-A[k,i])
        
        z = NRalpha(Q[k+1,i+1],B,ss,n,Co,S)
        A[k+1,i+1] = z[0]
        Y[k+1,i+1] = z[1]
        V[k+1,i+1] = Q[k+1,i+1]/A[k+1,i+1] 

#Seccion 4 
pyplot.subplot(2,1,1)
pyplot.plot(x,Y[k,:])
pyplot.xlabel('x (m)')
pyplot.ylabel('altura de agua(m)')
pyplot.axis([0, 150000, 0, 8])
pyplot.show()

pyplot.subplot(2,1,2)
pyplot.plot(x,Q[k,:])
pyplot.xlabel('x (m)')
pyplot.ylabel('Caudal (ft^3/s)')
pyplot.axis([0, 150000, 0, 1600])



    
    
    








    