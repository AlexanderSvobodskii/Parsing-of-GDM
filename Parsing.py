#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib as mpl
import re
import os


# In[14]:


path = 'C:\\Users\\Компьютер\\Desktop\\test_schedule.inc'

ident = os.path.exists(path)

if (ident == True):
    f = open(path, 'r')
    for line in f:
        print(line)
    f.close()
else :
    print('File does not exist in such directory')


# In[ ]:




