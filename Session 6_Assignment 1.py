#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement 1:
# Write a function so that the columns of the output matrix are powers of the input
# vector.
# The order of the powers is determined by the increasing boolean argument. Specifically,
# when increasing is False, the i-th output column is the input vector raised element-wise
# to the power of N - i - 1.
# 
# HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
# Theophile Vandermonde.

# In[1]:


import numpy as np

x = np.array([1, 2, 3, 4, 5])
N = 4
np.column_stack([x**(N-1-i) for i in range(N)])

#Vandermonde matrix: If increasing is False, the first column is x**(N-1), the second x**(N-2) and so forth


# In[7]:


#By calling vander function
x = np.array([1, 2, 3, 5])
np.vander(x)


# In[ ]:




