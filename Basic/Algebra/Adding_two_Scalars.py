#!/usr/bin/env python
# coding=utf-8
##############################################################
 # File Name : Adding_two_Scalars.py
 # Purpose : Basic scalar operation
 # Creation Date : Sat 15 Apr 2017 08:35:34 PM CST
 # Last Modified : Sat 15 Apr 2017 08:44:07 PM CST
 # Created By : SL Chung
##############################################################
import numpy
import theano.tensor as T
from theano import function

# Variable object
# T.dscalar is the type we assign to
# 0-dimensional arrays (scalar) of doubles (d)
x = T.dscalar('x')
y = T.dscalar('y')

z = x + y

#  The output of the function f is a numpy.ndarray with zero dimensions.
f = function([x, y], z)
