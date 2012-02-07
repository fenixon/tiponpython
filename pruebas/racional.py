from fractions import Fraction
from decimal import Decimal

>> from fractions import Fraction
>>> Fraction(8,9)
Fraction(8, 9)
>>> h=Fraction(8,9)
>>> h
Fraction(8, 9)
>>> h
Fraction(8, 9)
>>> h.n

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    h.n
AttributeError: 'Fraction' object has no attribute 'n'
>>> k=Fraction(Decimal(2.5))

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    k=Fraction(Decimal(2.5))
NameError: name 'Decimal' is not defined
>>> from decimal import Decimal
>>> k=Fraction(Decimal(2.5))
>>> k
Fraction(5, 2)
>>> k=Fraction(Decimal(1.5))
>>> k
Fraction(3, 2)
>>> k.denominator



k=Fraction(Decimal(0 - 2.0/3))

k=Fraction(0-2.00/3).limit_denominator(1000000)


##limitar la cantidad 
t=Fraction(-2).limit_denominator(1000000)

t.denominator
t.numerator	


Fraction(-3, 2)
>>> n=Fraction(-1.5).limit_denominator(1000000)
>>> n
Fraction(-3, 2)
>>> t=Fraction(-3.5).limit_denominator(1000000)