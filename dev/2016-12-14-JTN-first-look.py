
# coding: utf-8

# In[20]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set();


# In[2]:

print pd.__version__
print sns.__version__


# In[3]:

df = pd.read_excel("../data/coalpublic2013.xls", header=2, index_col='MSHA ID')
df.head()


# In[4]:

df['Company Type'].unique()


# In[5]:

df['Company Type'].replace(to_replace='Indepedent Producer Operator', 
                           value='Independent Producer Operator',
                          inplace=True)


# In[6]:

df['Company Type'].unique()


# In[7]:

df.rename(columns=lambda x: x.replace(" ","_"), inplace=True)


# In[8]:

df.head()


# In[9]:

len(df)


# In[10]:

plt.scatter(df.Average_Employees,df.Labor_Hours)
plt.xlabel('Total Employees')
plt.ylabel('Total Working Hours')


# In[11]:

sns.regplot(df.Average_Employees,df.Labor_Hours)
plt.savefig("../figures/2016-12-14" + "-employees_vs_hrs.png")


# In[12]:

for column in df.columns:
    print column


# In[13]:

plt.scatter(df.Labor_Hours, df['Production_(short_tons)'])
plt.xlabel('Total Working Hours')
plt.ylabel('Production (short tons)')


# In[14]:

df['Production_(short_tons)'].hist()


# In[15]:

#keep only non zero production
df = df[df['Production_(short_tons)'] > 0]


# In[16]:

df.head()


# In[18]:

len(df)


# In[19]:

#try again - still not good
df['Production_(short_tons)'].hist()


# In[23]:

#add new column
df['log_production'] = np.log(df['Production_(short_tons)'])


# In[24]:

#try hist again
df.log_production.hist()


# In[25]:

df.to_csv('../data/cleaned_coalpublic2013.csv')


# In[ ]:



