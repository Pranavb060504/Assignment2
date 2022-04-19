import matplotlib.pyplot as plt
import numpy as np
def f(x,a,b):
    return a*x+b

xlist=np.linspace(0,10,num=1000)
ylist=(f(xlist,-1,10))
yl2=np.linspace(0,0,num=1000)
xl2=np.linspace(0,20,num=1000)
plt.grid()
plt.annotate("A",[0,10])
plt.annotate("B",[10,0])
plt.annotate("C",[0,0])
plt.annotate("D",[10,10])
plt.annotate("s",[5,5])
plt.annotate("h",[0,5])
plt.annotate("x",[5,0])
plt.plot(xlist,ylist,label="length of rod= s")
plt.plot(xl2,yl2)
plt.plot(yl2,xl2)
plt.xlabel("Distance of foot from wall/ x")
plt.ylabel("Distance of tip from ground/ h")
plt.show()
