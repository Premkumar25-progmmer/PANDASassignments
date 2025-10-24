#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT -2

# # 1.Load the dataset into a Pandas DataFrame

# In[26]:


#importing data sets
import pandas as pd
import numpy as n
ss=pd.read_csv("store_sales (1).csv")


# # 2.Display the first and last 5 rows

# In[15]:


ss.head              #to display the first and last 5 rows 


# # 3. Check shape, data types, and non-null counts.

# In[16]:


print(ss.shape)    #Display the number of rows and columns


# In[18]:


print(ss.dtypes)    #to show data types


# In[19]:


print(ss.info())            # info about the dataframe (column data types


# # 4. Print column names and summary statistics for all numeric columns.

# In[20]:


ss.columns


# In[28]:


ss.describe 


# # 5. Find the total and average sales for each month (Jan–Apr).

# In[30]:


# total + avg sales grouped by month (Jan to Apr included)
ss.groupby('Jan')['May'].agg(['sum', 'mean'])


# In[31]:


ss['May'].sum()


# # 6. Calculate total yearly sales for all stores combined

# In[33]:


total_sales= ss[['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']].sum().sum()
print(total_sales)


# # 7.Find total sales for each city in each month using groupby().

# In[41]:


# Reshape the data: convert month columns into rows
ss_melted = ss.melt(id_vars='city', 
                    value_vars=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec'],
                    var_name='Month', value_name='Sales')

# Group by city and month, then sum sales
sales_by_city_month = ss_melted.groupby(['city', 'Month'])['Sales'].sum()

# Display result
print(sales_by_city_month)


# # 8. Find the average monthly sales per city.

# In[43]:


avg = ss_melted.groupby(['city', 'Month'])['Sales'].mean()

# Display result
print(avg)


# In[46]:


# city with highest average sales
ss.groupby('Arizona')['Sales'].mean().idxmax()


# In[ ]:
# # 11.  Display the top 5 stores with the highest Total_Sales.

df['Total_Sales'] = df[['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']].sum(axis=1)
# Sort and display top 5 stores
top_5_stores = df[['store_id', 'Total_Sales']].sort_values(by='Total_Sales', ascending=False).head(5)
print(top_5_stores)



