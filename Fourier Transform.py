#Day 18 Homework
#Homework 1
#Fourier Transform

import numpy as np
import pylab as py

nts=1000

ti=-4.0
tf=4.0
t=np.linspace(ti,tf,nts)
dt=t[1]-t[0]

fi=-6.0
ff=6.0
f=np.linspace(fi,ff,nts)
df=f[1]-f[0]

####################################

def Function(T):
    return np.sin(6*np.pi*T)*np.exp(-T**2)

py.figure(1)
py.plot(t,Function(t),"-")
py.title("Function Plot")
py.xlabel("t", fontsize=16)
py.ylabel("f(t)", fontsize=16)
py.show()

####################################

def Fourier(T,F):
    return Function(T)*np.exp(-2*np.pi*1.j*F*T)

####################################

def midpoint(nts):
    y=np.zeros(nts,dtype=complex)
    for i in range(0,nts):
        for j in range(0,nts-1):
            y[i]+=Fourier(t[j]+dt/2,f[i])*dt
    return y 
    
#####################################

def trapezoid(nts):
    z=np.zeros(nts,dtype=complex)
    for k in range(0,nts):
        for l in range(0,nts-1):
            z[k]+=((Fourier(t[l],f[k])+Fourier(t[l]+dt,f[k]))/2)*dt
    return z
    
#####################################

def Simpson(nts):
    B=midpoint(nts)
    C=trapezoid(nts)

    Iv=(2./3.)*B+(1./3.)*C
    return Iv

py.figure(2)
py.plot(f,np.real(Simpson(nts)),"-")
py.title("Fourier Real Plot")
py.xlabel("f", fontsize=16)
py.ylabel("A(f)", fontsize=16)
py.show()

py.figure(3)
py.plot(f,np.imag(Simpson(nts)),"-")
py.title("Fourier Imaginary Plot")
py.xlabel("f", fontsize=16)
py.ylabel("A(f)", fontsize=16)
py.show()

py.figure(4)
py.plot(f,np.real(Simpson(nts))**2,"-")
py.title("Periodogram")
py.xlabel("f", fontsize=16)
py.ylabel("P(f)", fontsize=16)
py.show()

