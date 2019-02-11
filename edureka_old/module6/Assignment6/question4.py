from pylab import *
import numpy as np
n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
#X_0 = np.linspace()
Y = np.sin(2*X)
plot (X, Y+1, color='blue', alpha=1.00)
fill_between(X,1,Y+1,facecolor = 'b')
plot (X, Y-1, color='blue', alpha=1.00)
fill_between(X,-1,Y-1,where =Y>0,facecolor = 'b')
fill_between(X,-1,Y-1,where =Y<0,facecolor = 'r')
show()
'''x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2*np.pi*x)
y2 = 1.2*np.sin(4*np.pi*x)

fig = figure()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312, sharex=ax1)
ax3 = fig.add_subplot(313, sharex=ax1)

ax1.fill_between(x, 0, y1)
show()'''
