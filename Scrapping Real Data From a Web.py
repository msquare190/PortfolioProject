#!/usr/bin/env python
# coding: utf-8

# In[11]:


#This are libraries

from bs4 import BeautifulSoup
import requests


# In[12]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[13]:


print(soup)


# In[21]:


#Since we have more than one table in the website we use index to call the table we need which is table [1]

soup.find_all('table')[1] 


# In[23]:


table = soup.find_all('table')[1]


# In[24]:


print(table)


# In[27]:


world_titles = table.find_all('th') #Getting the titles of the table using "th" tags


# In[28]:


world_titles


# In[31]:


#Looping through to take only the texts from the "th" tags

world_table_titles = [title.text.strip() for title in world_titles] #The ".strip()" function is use to remove backslash


# In[32]:


print(world_table_titles)


# In[33]:


#Creating DataFrame


# In[34]:


import pandas as pd


# In[35]:


df = pd.DataFrame(columns = world_table_titles) #Putting the titles into columns


# In[36]:


df


# In[40]:


table.find_all('tr') #the tag "tr" is the rows in the table


# In[38]:


column_data = table.find_all('tr')


# In[39]:


for row in column_data[1:]:
    row_data = row.find_all('td') #"td" tag is the individual row data in the table
    individual_row_data = [data.text.strip() for data in row_data]
    
    length = len(df)
    df.loc[length] = individual_row_data


# In[41]:


df


# In[42]:


#Exporting the dataframe into a csv file

df.to_csv(r'C:\Users\msqua\OneDrive\Desktop\Google Data Analysts\Full Data Analyst Bootcamp\companies.csv', index = False)


# In[ ]:




