#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
init_printing()


phi,y,theta,psi=symbols('phi, y, theta, psi')

"""
R_phi,T_y,R_theta,R_psi=symbols('R_phi,T_y,R_theta,R_psi')
"""

R_phi=Matrix(
    [[1,0,0,0],
    [0,cos(phi),-sin(phi),0],
    [0,sin(theta),cos(theta),0],
    [0,0,0,1]])


T_y=Matrix([[1,0,0,0],
            [0,1,0,y],
            [0,0,1,0],
            [0,0,0,1]])



R_theta=Matrix(
    [[cos(theta),-sin(theta),0,0],
    [sin(theta),cos(theta),0,0],
    [0,0,1,0],
    [0,0,0,1]])



R_psi=Matrix(
    [[1,0,0,0],
    [0,cos(psi),-sin(psi),0],
    [0,sin(psi),cos(psi),0],
    [0,0,0,1]])


#This is the final MAtrix Required
expr=simplify(R_theta*R_phi*T_y*R_psi)
pprint(expr)

