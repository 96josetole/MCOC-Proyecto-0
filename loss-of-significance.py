# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 18:56:36 2018

@author: 96josetole
"""

import numpy as np
from numpy import random
from matplotlib import pyplot as plt
for t in [9,10,11,12,13,14]:
    n = 2**t #Cantidad de datos que contiene la lista a
    print "N = " +str(n)
    a=np.zeros((1,n), dtype=np.float32) #se crea la lista an con largo N
    i = 0
    a[0, :n/2-1]=1#se determina que la primer mitad de la lista contiene valores 1.0
    a[0, n/2:]=0.1#se determina que la primer mitad de la lista contiene valores 0.1  
    b = np.std(a) #arreglo a con tipo de datos dtype=sp.float32 y usar np.std.
    c = np.std(a, dtype= np.float64) #arreglo a con tipo de datos dtype=sp.float32 y usar np.std con un acumulador interno de tipo np.float64.
    d = np.std(a, dtype= np.float16) #arreglo a con tipo de datos dtype=sp.float32 y usar np.std con un acumulador interno de tipo np.float16.
#Definicion de funcion propia de desviacion estandar con acumulador interno del tipo np.float64
    def stdev64(z,n):#se ingresan parametros (lista,N=largo lista)
        s = 0
        i = 0
        while i < n:
            s+=(z[0,i]-np.mean(z, dtype= np.float64))**2
            i+=1
        return np.sqrt(s/(n)) #retorna desviacion estandar de los datos
    e = stdev64(a,n)
#Definicion de funcion propia de desviacion estandar con acumulador interno del tipo np.float32
    def stdev32(z,n):#se ingresan parametros (lista,N=largo lista)
        s = 0
        i = 0
        while i < n:
            s+=(z[0,i]-np.mean(z))**2
            i+=1
        return np.sqrt(s/(n)) #retorna desviacion estandar de los datos
    f = stdev32(a,n)
    print "Standard_deviation_1 = "+str(b)+"       "+"ERROR = "+str((abs(b-c)/c)*100) + " %"
    print "Standard_deviation_2 = "+str(c)+" "+"ERROR = "+str((abs(c-c)/c)*100) + " %"
    print "Standard_deviation_3 = "+str(d)+"         "+"ERROR = "+str((abs(d-c)/c)*100) + " %"
    print "Standard_deviation_4 = "+str(e)+" "+"ERROR = "+str((abs(e-c)/c)*100) + " %"
    print "Standard_deviation_5 = "+str(f)+" "+"ERROR = "+str((abs(f-c)/c)*100) + " %"
#figura-loss-of-significance-plot2, no considera el caso 3
plt.plot([9,10,11,12,13,14],[1.61227765581e-06,1.84114747245e-06,5.44276374756e-06,8.92503144069e-06,6.11738039649e-06,1.39103310154e-06 ])
plt.plot([9,10,11,12,13,14],[0.0,0.0,0.0,0.0, 0.0 ,0.0 ])
plt.plot([9,10,11,12,13,14],[3.86746e-03,1.95239525039e-02,2.28445272818e-02,1.68627805871e-02,1.3860468879e-02,1.23564525481e-02 ])
plt.plot([9,10,11,12,13,14],[9.86398619732e-14,1.23328670158e-12,2.30652002558e-12,2.84940109253e-12,7.62330195976e-12,5.32899026658e-12])
plt.plot([9,10,11,12,13,14],[8.23470301698e-07,8.25652493288e-07,8.26746990468e-07,8.27296322042e-07,8.27558189726e-07,8.27717308651e-07])
plt.xlabel("N, donde a.size = 2^N")
plt.ylabel("Error Relativo")
plt.legend(["a.dtype=float32 y np.std(a)","a.dtype=float32 y np.std(a,dtype=np.float64)","a.dtype=float32 y np.std(a,dtype=np.float16)","a.dtype=float32 y stdev64(a,N)","a.dtype=float32 y stdev32(a,N)"])
plt.title("Perdida de significancia")
plt.show()
#figura-loss-of-significance-plot
plt.plot([9,10,11,12,13,14],[1.61227765581e-06,1.84114747245e-06,5.44276374756e-06,8.92503144069e-06,6.11738039649e-06,1.39103310154e-06 ])
plt.plot([9,10,11,12,13,14],[0.0,0.0,0.0,0.0, 0.0 ,0.0 ])
plt.plot([9,10,11,12,13,14],[9.86398619732e-14,1.23328670158e-12,2.30652002558e-12,2.84940109253e-12,7.62330195976e-12,5.32899026658e-12])
plt.plot([9,10,11,12,13,14],[8.23470301698e-07,8.25652493288e-07,8.26746990468e-07,8.27296322042e-07,8.27558189726e-07,8.27717308651e-07])
plt.xlabel("N, donde a.size = 2^N")
plt.ylabel("Error Relativo")
plt.legend(["a.dtype=float32 y np.std(a)","a.dtype=float32 y np.std(a,dtype=np.float64)","a.dtype=float32 y stdev64(a,N)","a.dtype=float32 y stdev32(a,N)"])
plt.title("Perdida de significancia")
plt.show()