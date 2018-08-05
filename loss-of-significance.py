# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 18:56:36 2018

@author: 96josetole
"""

import numpy as np
from numpy import random
from matplotlib import pyplot as plt

t = 9
n = 2**t
print "N: " +str(n)
a=np.zeros((1,n), dtype=np.float32)
i = 0
a[0, :n/2-1]=1
a[0, n/2:]=0.1  
b = np.std(a)
c = np.std(a, dtype= np.float64) 
d = np.std(a, dtype= np.float16)
def stdev64(z,n):
    s = 0
    i = 0
    while i < n:
        s+=(z[0,i]-np.mean(z, dtype= np.float64))**2
        i+=1
    return np.sqrt(s/(n))
e = stdev64(a,n)

def stdev32(z,n):
    s = 0
    i = 0
    while i < n:
        s+=(z[0,i]-np.mean(z))**2
        i+=1
    return np.sqrt(s/(n))
f = stdev32(a,n)
print str(b)+" "+str((abs(b-c)/c)*100) + " %"
print str(c)+" "+str((abs(c-c)/c)*100) + " %"
print str(d)+" "+str((abs(d-c)/c)*100) + " %"
print str(e)+" "+str((abs(e-c)/c)*100) + " %"
print str(f)+" "+str((abs(f-c)/c)*100) + " %"

#plt.plot([9,10,11,12,13,14],[1.61227765581e-06,1.84114747245e-06,5.44276374756e-06,8.92503144069e-06,6.11738039649e-06,1.39103310154e-06 ])
#plt.plot([9,10,11,12,13,14],[0.0,0.0,0.0,0.0, 0.0 ,0.0 ])
#plt.plot([9,10,11,12,13,14],[0.00386746398162,0.0195239525039,0.0228445272818,0.0168627805871,0.013860468879,0.0123564525481 ])
#plt.plot([9,10,11,12,13,14],[9.86398619732e-14,1.23328670158e-12,2.30652002558e-12,2.84940109253e-12,7.62330195976e-12,5.32899026658e-12])
#plt.plot([9,10,11,12,13,14],[8.23470301698e-07,8.25652493288e-07,8.26746990468e-07,8.27296322042e-07,8.27558189726e-07,8.27717308651e-07])