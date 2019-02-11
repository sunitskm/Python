from pylab import *
import numpy as np
X = np.linspace(-pi, pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plot(S)
