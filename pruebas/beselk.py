from scipy.special import *
import numpy as np

z = np.linspace(0,1,6);
print z
##besselk(1,z) 
res=kn(1,z)

print "valor: ", res
