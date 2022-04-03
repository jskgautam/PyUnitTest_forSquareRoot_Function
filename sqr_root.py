# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:23:50 2022

@author: Jay Gautam
"""
# print(round(2**(1/2), 3))

def sqr_root_num(number):
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError("The number should be either int or float")
    if number >= 0:
        return round(number**(1/2), 3)
    raise TypeError("The number must be positive")



# result = sqr_root_num(9.5)
# print(result)