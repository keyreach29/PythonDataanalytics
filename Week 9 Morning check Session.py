#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


#Week 9 Morning check discussion
#Worked EXamples



# In[3]:


#Import the libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# In[4]:


#load the dataframe
data= pd.read_csv('D:\AZUBI-PYTHON-TRAINER\dm_office_sales.csv')
data


# In[5]:


#Potting the scatter plot

#showing the realtionship btw salary & sales
plt.scatter(data['salary'],data['sales'],s=100,c='g',marker='*')

plt.xlabel('Salary')
plt.ylabel('sales')
plt.title('Comparing Salaries with Sales')


# In[6]:


#Histogram
#Find the distribution for the salary
plt.hist(data['salary'],bins=15,edgecolor='green')
plt.xlabel('salary')
plt.ylabel('Count')
plt.title('Salary Distribution Chart')


# In[12]:


#Box plot
#Provides a summary of mean, median,minimum,maximum,Quartiles(1st,3rd),ourliers for work experience
plt.boxplot(data['work experience'])


# In[ ]:





# In[ ]:




