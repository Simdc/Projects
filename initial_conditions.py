#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


class initial_condition():
    def __init__(self):
        pass
    
    def matrix_initialization(NX, NY, zero_initialization = True, intial_value = 0):
        
        if zero_initialization == True:
            
            m_prev = np.zeros([NX,NY], dtype = np.float64)
           
            
        else:
            m_prev = np.full([NX,NY],  intial_value,dtype = np.float64)
            
        m_tent = np.zeros([NX,NY], dtype = np.float64)
        m_next = np.zeros([NX,NY], dtype = np.float64)
           
            
            
        
        return [m_prev, m_tent, m_next]


# In[ ]:




