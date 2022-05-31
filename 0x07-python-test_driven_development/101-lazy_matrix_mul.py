#!/usr/bin/python3
"""
Write a function that multiplies 2 matrices by using the module NumPy

To install it: pip3 install numpy==1.15.0

    - Prototype: def lazy_matrix_mul(m_a, m_b):
    - Test cases should be the same as 100-matrix_mul but with new exception type/message

"""
from numpy import matmul

def lazy_matrix_mul(m_a, m_b):
    """Multiplies 2 matrices by using Numpy"""
    return(matmul(m_a, m_b))
