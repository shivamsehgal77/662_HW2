#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First rotation matrix are written about each axis
#Then a transformation matrix is found out for the rotations
#Then equation of cone is written in matrix format wrt drone.
#Then the equation of the cone is converted to the origin frame.
#Then we substitute z=0 to find the intersection b/w the cone and the x-y plane.
#This gives equation of an elipse which is then solved for area using the hint given.



# Sympy is imported to make it possible to write equations
from sympy import *
import math
init_printing()
import shutilwhich


#symbols used in the code are defined as follows
x,y,z,d_x,d_y,d_z=symbols('x,y,z,d_x,d_y,d_z')
phi,theta,psi=symbols('phi,theta, psi')


#Rotation matrix are found out for each rotation.
R_psi=Matrix(
    [[1,0,0,0],
     [0,cos(psi),-sin(psi),0],
     [0,sin(psi),cos(psi),0],
     [0,0,0,1]])

R_theta=Matrix(
    [[cos(theta),0,sin(theta),0],
     [0,1,0,0],
     [-sin(theta),0,cos(theta),0],
     [0,0,0,1]])
R_phi=Matrix(
    [[cos(phi),-sin(phi),0,0],
     [sin(phi),cos(phi),0,0],
     [0,0,1,0],
     [0,0,0,1]])
T_D_wrt_origin=Matrix(
    [[1,0,0,d_x],
     [0,1,0,d_y],
     [0,0,1,d_z],
     [0,0,0,1]])

#Transformation of Drone wrt origin is given by the below equation.
Rotation_Dnew_wrt_origin=simplify(T_D_wrt_origin*R_phi*R_theta*R_psi)
pprint(Rotation_Dnew_wrt_origin)


# In[3]:


#any point wrt drone can be written as.
p_drone=Matrix([[x],[y],[z],[1]])

#S is a matrix to make the equation of the cone.
S=Matrix([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,0]])

#Therefore equation of cone wrt drone
Cone_eqn=p_drone.T*S*p_drone
Cone_eqn


# In[5]:


#Equation of the cone wrt the origin frame can be found using the below computation
#This is explaned in the pdf report also.
H=(Rotation_Dnew_wrt_origin.T)*S*(Rotation_Dnew_wrt_origin)
Equation_cone_wrt_origin=simplify(p_drone.T*H*p_drone)
Equation_cone_wrt_origin


# In[6]:


#To find the intersection with the x-y plane we substitute z=0
Intersection_cone_x_y_plane=Equation_cone_wrt_origin.subs({z:0})

#To convert this final cone equation to 
Ellipse_eqn=Intersection_cone_x_y_plane[0]
pprint(Ellipse_eqn)


# In[7]:


expr_1=Poly(Ellipse_eqn.evalf(),x,y,x*y,x**2,y**2)
preview(expr_1, viewer='file', filename='coeff_eqn')
pprint(expr_1)
list1=expr_1.coeffs()

a=list1[0]
b=list1[1]/2
c=list1[3]
d=list1[2]/2
e=list1[4]/2
f=list1[5]


# In[8]:


k=(-pi)/(sqrt(((a*c)-(b*b))**3))
A=Matrix([[a,b,d],[b,c,e],[d,e,f]])
Det_A=(det(A))

#This is the area of the ellipse 
area=(k*Det_A)
pprint(simplify(area))


# In[16]:


#For the following values of theta psi,phi i get the following result.

print((simplify(area.subs({psi:0,theta:0,phi:pi/4,d_x:1,d_y:2,d_z:3}))))

print(float(simplify(area.subs({psi:pi/6,theta:pi/6,phi:pi/4,d_x:1,d_y:2,d_z:3}))))


# In[ ]:




