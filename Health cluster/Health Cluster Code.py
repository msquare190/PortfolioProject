#!/usr/bin/env python
# coding: utf-8

# ## Libraries

# In[1]:


# Import all neccesary librarie

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
from matplotlib.colors import Normalize, ListedColormap
from sklearn.preprocessing import StandardScaler


from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


# ## DataFrame

# In[15]:


# These helps us to put and view our dataset in a dataframe in python

df = pd.read_csv('country_data.csv')
df


# ## Data Exploration

# In[5]:


# shape gives a description of the total number of columns and rows the dataset has

df.shape


# In[6]:


# Check if there is null values

df.isnull().sum()


# In[7]:


#check for duplicate rows

duplicate_rows = df.duplicated().sum()
duplicate_rows


# In[8]:


df.info()


# In[9]:


#Summary of the data

df.describe()


# ## Feature Engineering

# In[10]:


# Calculate the correlation matrix for only numeric features
correlation_matrix = df.drop(columns = ['country']).corr()

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Feature Correlation Matrix")
plt.show()


# Interpreting Feature Pairs:
# 
# For each non-diagonal cell, a correlation value close to 1 implies a strong positive relationship, meaning as one feature increases, the other also tends to increase.
# A value close to -1 implies a strong negative relationship, where as one feature increases, the other tends to decrease.
# Values near 0 suggest a weak or no linear relationship, indicating that the features are relatively independent.

# ## Model Building

# In[41]:


# There is no target in clustering so, y variable is not needed

x = df.iloc[:,[1,3,7]]


# ## K-means

# In[42]:


kmeans = KMeans(n_clusters = 3, n_init = 'auto', random_state = 42)
kmeans.fit(x)


# In[43]:


centers = kmeans.cluster_centers_
print('centroids: \n', centers)


# ## To view Countries and the Clusters they Belong To

# In[44]:


df['cluster'] = kmeans.labels_

# Extract countries in each cluster
cluster_0_countries = df[df['cluster'] == 0]['country'].tolist()
cluster_1_countries = df[df['cluster'] == 1]['country'].tolist()
cluster_2_countries = df[df['cluster'] == 2]['country'].tolist()

df


# ## Visualization

# In[18]:


#Visualise the result
fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection = '3d')

# store the normalisation of the color encodings
nm = Normalize(vmin = 0, vmax = len(centers)-1)

# plot the clustered data
scatter1  = ax.scatter(x['child_mort'], x['health'], x['life_expec'], c = kmeans.predict(x), s = 50, cmap = 'plasma', norm = nm)

# plot the centroids using a for loop
for i in range(centers.shape[0]): ax.text(centers[i, 0], centers[i, 1], centers[i, 2], str(i), c = 'black',
                                          bbox=dict(boxstyle="round", facecolor='white', edgecolor='black'))
    
    
ax.azim = -60
ax.dist = 10
ax.elev = 10
# column names here!!!
ax.set_xlabel(df.columns[1])
ax.set_ylabel(df.columns[3])
ax.set_zlabel(df.columns[7])

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter1.legend_elements(),
loc="upper right", title="Clusters")
ax.add_artist(legend1)
fig.savefig('cluster_plot.png')

# produce a legend with the unique colors from the scatter
legend1 = ax.legend(*scatter1.legend_elements(), loc="center left", title="Clusters")
ax.add_artist(legend1)
fig.tight_layout(pad = 2.0)


# ## Using all the features

# In[24]:


x = df.drop('country', axis = 1)

kmeans = KMeans(n_clusters = 3, n_init = 'auto', random_state = 42)
kmeans.fit(x)

centers = kmeans.cluster_centers_
print('centroids: \n', centers)


# In[38]:


# Viewing Countries who are in cluster 2 

df[df['cluster'] == 2]


# In[ ]:




