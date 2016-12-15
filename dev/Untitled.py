
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

print pd.__version__


# In[3]:

ls


# In[6]:

ls ..\data


# In[14]:

df1 = pd.read_excel("../data/coalpublic2013.xls", header=2, index_col='MSHA ID')
df1.head()


# In[ ]:



