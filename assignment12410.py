#!/usr/bin/env python
# coding: utf-8

# # 1.importing data sets

# In[2]:


#importing data sets
import pandas as pd
ud=pd.read_csv("Uber_Drives_2016.csv")
ud.head() #to display the head data


# # 2.Display the number of rows and columns

# In[5]:


print(ud.shape)    #Display the number of rows and columns


# # 3.  unique values in CATEGORY column

# In[11]:


#  unique values in CATEGORY column
ud['CATEGORY*'].unique()


# # 4.Find how many null values are there in PURPOSE

# In[12]:


ud['PURPOSE*'].isnull().sum()  # no. of null values in PURPOSE


# # 5 Rename all columns in uppercase.

# In[14]:


ud=ud.rename(columns={'START_DATE*':'START_DATE','END_DATE*':'END_DATE','START*':'START','CATEGORY*':'CATEGORY','STOP*':'STOP','MILES*':'MILES','PURPOSE*':'PURPOSE'})
ud


# # 6. display rides where CATEGORY == 'Business'.

# In[16]:


ud.loc[ud['CATEGORY']=="Business"] 


# # 7. Show top 5 rides with the longest distance (MILES).

# In[17]:


ud.sort_values(by='MILES', ascending=False).head(5)


# # 8. Replace all missing PURPOSE values with "Not Specified".

# In[18]:


ud['PURPOSE'] = ud['PURPOSE'].fillna("Not Specified")
ud['PURPOSE'].isnull().sum()


# # 9. Create a new column TRIP_DURATION using END_DATE - START_DATE.

# In[27]:


# Calculate trip duration
ud['TRIP_DURATION'] = ud['END_DATE'] - ud['START_DATE']
# Display the result
print(ud[['START_DATE', 'END_DATE', 'TRIP_DURATION']])


# # 10.Sort trips by distance in descending order.

# In[25]:


ud.sort_values(by='MILES', ascending=False)


# #  11. Group by CATEGORY and find average miles per category.

# In[24]:


a_miles = ud.groupby('CATEGORY')['MILES'].mean()
a_miles    # average miles per category


# # 12 Find total trips for each PURPOSE.

# In[28]:


c= ud['PURPOSE'].value_counts()
c


# # 13 Identify top 3 start locations by number of rides.

# In[29]:


t_start_loc = ud['START'].value_counts().head(3)
t_start_loc


# In[ ]:




