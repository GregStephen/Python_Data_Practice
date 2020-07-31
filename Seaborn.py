#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


tips = sns.load_dataset('tips')


# In[4]:


tips.head()


# In[10]:


sns.distplot(tips['total_bill'], kde=False, bins=40)


# In[14]:


sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')


# In[16]:


sns.pairplot(tips, hue='sex')


# In[17]:


sns.rugplot(tips['total_bill'])


# In[ ]:




