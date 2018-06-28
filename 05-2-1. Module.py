import sys
print(sys.path)
sys.path.append("/Users/songjaehyeok/Documents/Python/Jump To Python/mymod")
print(sys.path)

import mod1
print(mod1.sum(3,4))
print(mod1.safe_sum(1, 'a'))

from mod1 import sum
print(sum(3,4))

from mod1 import sum, safe_sum
print(mod1.safe_sum(1, 'a'))

from mod1 import *
print(mod1.safe_sum(1, 'a'))

import mod1
print(mod1.sum(3,4))

import mod2
print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.sum(mod2.PI, 4.4))

import modtest
print(mod2.sum(3,7))