#!/usr/bin/env python
# coding: utf-8

# In[3]:


"""
Sympy was used to define symbols
mpmath to convert from radians to degrees and vice versa
matplotlib to plot the graphs
math for inverse trignometric functions

First the final orientation is computed by the three rotations.
Then values are put in as given in the question.
Using these an angle axis represntation is computed explained below
Drone will be rotated at some angular velocity about the found axis to get the final orientation.
Using this and the constraints on angular velocity in the question we can find the angular velocity.
Then we can find w_x,w_y,w_z.
Then comparing the angle axis represntation with the Euler angle.
We find the plots of phi,theta,psi.

"""






from sympy import *
from mpmath import radians, degrees
import math
import matplotlib.pyplot as plt

x,y,z,d_x,d_y,d_z=symbols('x,y,z,d_x,d_y,d_z')
phi,theta,psi=symbols('phi,theta, psi')
w_x,w_y,w_z=symbols('w_x,w_y,w_z')
gammadot=symbols('gammadot')
gamma=symbols('gamma')

"""
R_phi,T_y,R_theta,R_psi=symbols('R_phi,T_y,R_theta,R_psi')
"""

R_psi=Matrix([[1,0,0],
     [0,cos(psi),-sin(psi)],
     [0,sin(psi),cos(psi)]])

R_theta=Matrix(
    [[cos(theta),0,sin(theta)],
     [0,1,0],
     [-sin(theta),0,cos(theta)]])
R_phi=Matrix(
    [[cos(phi),-sin(phi),0],
     [sin(phi),cos(phi),0],
     [0,0,1]])

#final orientation of the frame.
final_orientation=simplify(R_phi*R_theta*R_psi)

final_orientation


# In[4]:


# calcuating trace to calculate the angle for angle axis rotstion
trace=final_orientation[0,0]+final_orientation[1,1]+final_orientation[2,2]
trace=trace.subs({psi:radians(35),theta:radians(15),phi:radians(20)})

# Calculating the angle alpha for angle of angle axis
alpha=math.acos((trace-1)/2)


# calulation for the axis of rotation for psi,theta,phi 
val=1/(2*math.sin(alpha))
Axis=Matrix([
        [final_orientation[2,1]-final_orientation[1,2]],
        [final_orientation[0,2]-final_orientation[2,0]],
        [final_orientation[1,0]-final_orientation[0,1]]])

k=val*Axis


k=k.subs({psi:radians(35),theta:radians(15),phi:radians(20)})

#axis of rotation
k


# In[5]:


# rotation matrix for global frame about the n axis(gammadot is the angular velocity)
w_g=gammadot*k

#skew symetric matrix for the global frame 
w_g_skew=Matrix([[0,-w_g[2],w_g[1]],[w_g[2],0,-w_g[0]],[-w_g[1],w_g[0],0]])

w_g_skew


# In[6]:


#Rotation skew symetric matrix for drone local frame

w_drone=Matrix([[0,-w_z,w_y],[w_z,0,-w_x],[-w_y,w_x,0]])


# In[7]:


w_drone_1=(final_orientation.T)*w_g_skew*(final_orientation)

# finding thr values for w_x,w_y,w_z for given angles
solution=w_drone-w_drone_1
solution=solution.subs({psi:radians(35),theta:radians(15),phi:radians(20)})
solution


# In[8]:


solution[1,2]


# In[9]:


#we know that max of w is w=1deg/sec
#therefore the max angular velocity is of w_x=1 deg/sec
# we find the gammadot and hence can find the shortest time for rotation

print('\n')
w_z=(solve(solution[0,1],w_z))
w_y=(solve(solution[0,2],w_y))
w_x=(solve(solution[1,2],w_x))


w_x


# In[10]:


# solving for the angular velocity about the axis of rotation
gammadot_val=solve(w_x[0]-1,gammadot)


time_1=40.5/gammadot_val[0]
time_1
w_g_skew
gammadot_val[0]


# In[11]:


#computing the angular velocity and plotting against time.As required for the solution.
angular_x=[w_x[0].subs({gammadot:gammadot_val[0]})]*30

angular_y=[w_y[0].subs({gammadot:gammadot_val[0]})]*30

angular_z=[w_z[0].subs({gammadot:gammadot_val[0]})]*30

time_final=[x for x in range(0,30)]

plt.plot(time_final,angular_x,label='w_x')
plt.plot(time_final,angular_y,label='w_y')
plt.plot(time_final,angular_z,label='w_z')
plt.ylabel('Angular Velocity(w) deg/s')
plt.xlabel('Time(t) seconds')
leg = plt.legend(loc='upper center')


# In[12]:


#skew symetric matrix for the global frame 
w_g_skew=Matrix([[0,-w_g[2],w_g[1]],[w_g[2],0,-w_g[0]],[-w_g[1],w_g[0],0]])

k_skew_symetric=w_g_skew.subs({"gammadot":1})
k_skew_symetric


# In[16]:


#finding phi,psi,theta in terms of gamma.
Identity_MAtrix=Matrix([[1,0,0],[0,1,0],[0,0,1]])
z=sin(gamma)*k_skew_symetric
z


# In[31]:


w=(1-cos(gamma))*(k_skew_symetric)**2
w


# In[32]:


R_angle_axis=Identity_MAtrix+z+w

R_angle_axis


# In[39]:


theta_val=[]
for i in range(0,30):
    w=radians(i*1.274)#Gammadot=1.274
    theta_val.append(R_angle_axis[2,0].subs({gamma:w}))
    
#plot of theta wrt to time

theta_val=[degrees(-asin(x)) for x in theta_val]

time_final=[x for x in range(0,30)]

plt.plot(time_final,theta_val)
plt.xlabel("Time")
plt.ylabel("Angle with y(theta)")


# In[34]:


#computing tan(psi) by comparison of angle axis and euler angle
tan_psi=R_angle_axis[2,1]/R_angle_axis[2,2]
tan_psi


# In[40]:


#plot of psi wrt to time

psi_val=[]
for i in range(0,30):
    w_x_x=radians(i*1.274)
    psi_val.append(tan_psi.subs({gamma:w_x_x}))

psi_val=[degrees(atan(x)) for x in psi_val] 
psi_val

plt.plot(time_final,psi_val)
plt.xlabel("Time")
plt.ylabel("Angle with x(psi)")


# In[36]:


#computing tan(phi) by comparison of angle axis and euler angle
tan_phi=R_angle_axis[1,0]/R_angle_axis[0,0]
tan_phi


# In[48]:


#plot of phi wrt time
phi_val=[]
for i in range(0,30):
    w_z_z=radians(i*1.274)
    phi_val.append(tan_phi.subs({gamma:w_z_z}))
    

phi_val=[degrees(atan(x)) for x in phi_val]
phi_val

phi_val

plt.plot(time_final,phi_val)
plt.xlabel("Time")
plt.ylabel("Angle with z(phi)")


# In[43]:





# In[ ]:




