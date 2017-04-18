#!/usr/bin/env python
# coding=utf-8
##############################################################
 # File Name : Adding_two_Scalars.py
 # Purpose : Basic scalar operation
 # Creation Date : Sat 15 Apr 2017 08:35:34 PM CST
 # Last Modified : 2017年04月18日 (週二) 13時37分55秒
 # Created By : SL Chung
##############################################################
import numpy as np
import theano.tensor as T
from theano import function
from theano import pp 

# Variable object
# T.dscalar is the type we assign to
# 0-dimensional arrays (scalar) of doubles (d)
# with the given name (string)
x = T.dscalar('x')
y = T.dscalar('y')

z = x + y

# show the function f, how z is calculated
print('z = ', pp(z))

#  The output of the function f is a numpy.ndarray with zero dimensions.
f = function([x, y], z)
print('f(x,y) = x + y')
print('f(2,3) is', f(2,3))
