from scipy.special import expn
import numpy as np

## http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html
## http://docs.scipy.org/doc/scipy/reference/generated/scipy.special.expn.html
## Siempre el primer arg es 1, el segundo valor va a ser lo que se ponga en Matlab
res=expn(1,1.0)

print "valor: ", res
