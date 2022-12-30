#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
init_printing()

#Defining the symbols used in the code
x,y,z=symbols('x,y,z')
a,b,c=symbols('a,b,c')
phi=symbols('phi')
xprime,yprime,zprime=symbols('xprime,yprime,zprime')

"""        Origin of frame A wrt to frame A'   x_A,y_A,z_A  """
x_A,y_A,z_A=symbols('x_A,y_A,z_A')

"""     Transformation of A with respect of A' 
        pre multiplying this matrix by points of A will give points of A wrt to A'

"""
# any point wrt A frame
p_A=Matrix([[x],[y],[z],[1]])

# Any point wrt A_prime frame
p_Aprime=Matrix([[xprime],[yprime],[zprime],[1]])

#Tansfromation matrix from Aprime to A
T_Aprime_wrt_A=Matrix([[cos(phi),-sin(phi),0,x_A],[sin(phi),cos(phi),0,y_A],[0,0,1,z_A],[0,0,0,1]])


#Therefore pA= T_Aprime_wrt_A*p_Aprime
Product=simplify(T_Aprime_wrt_A*p_Aprime)
pprint(Product)



# In[3]:


# origin of Aprime with respect to A
o_Aprime=solve([Product-p_A],[x_A,y_A,z_A])

#Final Matrix with the origin values put in
T_Aprime_wrt_A=Matrix([[cos(phi),-sin(phi),0,o_Aprime[x_A]],[sin(phi),cos(phi),0,o_Aprime[y_A]],[0,0,1,o_Aprime[z_A]],[0,0,0,1]])
pprint(T_Aprime_wrt_A)




# In[4]:


#But we have been given the question to find T_A_wrt_Aprime
#For that I have done the following computations explained int he PDF report.
R_Aprime_wrt_A=Matrix([[cos(phi),-sin(phi),0],[sin(phi),cos(phi),0],[0,0,1]])
Origin=Matrix([[o_Aprime[x_A]],[o_Aprime[y_A]],[o_Aprime[z_A]]])

R_A_wrt_Aprime=R_Aprime_wrt_A.T
Origin_new=-(R_A_wrt_Aprime*Origin)


#This the final matrix required.
T_Aprime_wrt_A=Matrix([[R_A_wrt_Aprime[0,0],R_A_wrt_Aprime[0,1],R_A_wrt_Aprime[0,2],Origin_new[0]],
                        [R_A_wrt_Aprime[1,0],R_A_wrt_Aprime[1,1],R_A_wrt_Aprime[1,2],Origin_new[0]],
                        [R_A_wrt_Aprime[2,0],R_A_wrt_Aprime[2,1],R_A_wrt_Aprime[2,2],Origin_new[0]],
                        [0,0,0,1]])

pprint(T_Aprime_wrt_A)


# In[ ]:




