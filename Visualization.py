#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import numpy as np


# In[2]:


class Visual():
    
    def __init__():
        pass
    
    def visualize_vector_plot(X, Y, u_next, v_next, streamplot):
        
        #------------------------------------------------#
        #plt.figure()
        plt.xlim((0, 1))
        plt.ylim((0, 0.5))
        #------------------------------------------------#
    
        if streamplot == True: 
            z1 = plt.streamplot(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], v_next[::2, ::2], color="black")
        else:
            z1 = plt.quiver(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], v_next[::2, ::2], color="black")
    
   
        #plt.show()
    
        return z1
    
    def visualize_contour_plot(X, Y, u_next, ticks):
    
        #------------------------------------------------#
        #plt.figure()
        plt.xlim((0, 1))
        plt.ylim((0, 0.5))
        #------------------------------------------------#
        plt.contourf(X[::2, ::2], Y[::2, ::2], u_next[::2, ::2], cmap="plasma")
        plt.colorbar(ticks=np.linspace(-50, 50, 20))
        #------------------------------------------------#
        
        return None
    
    def visualize_error_plot(Spin_up,N_ITERATIONS):
        
        Spin_up = np.array(Spin_up)
        np.shape(Spin_up)
        
        plt.ylabel('Error')
        plt.xlabel('Timesteps')
        plt.plot(np.linspace(0,1,N_ITERATIONS),Spin_up)
        plt.show()
        
        return None
    


# In[ ]:




