#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import scipy.stats


# In[3]:


import matplotlib
import matplotlib.pyplot as np
import pandas.plotting
from IPython import display
from ipywidgets import interact,widgets
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


colleges=pd.read_csv('insti.csv')


# In[5]:


colleges.info()


# In[6]:


colleges.head()


# In[7]:


pd.DataFrame(colleges.Autonomous.value_counts())


# In[8]:


pd.DataFrame(colleges.district.value_counts())


# In[10]:


combined=colleges.groupby("Autonomous").district.value_counts()
combined


# In[11]:


combined.unstack()


# In[13]:


colleges.Autonomous.value_counts().plot(kind='bar')


# In[14]:


colleges.district.value_counts().plot(kind='bar')


# In[15]:


combined.plot(kind='bar')


# In[17]:


k=combined.unstack()
k.plot(kind='bar')


# In[19]:


k.plot(kind='barh')


# In[ ]:




