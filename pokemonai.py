#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


df = pd.read_csv('pokemon.csv')


# In[3]:


df


# In[4]:


print(df.columns)


# In[5]:


print(df.info())


# In[7]:


print(df.isnull().sum())


# In[10]:


print(df[['height_m', 'percentage_male', 'type2', 'weight_kg']])


# In[11]:


df.describe().T


# In[12]:


df = df.fillna(0)


# In[13]:


df


# In[14]:


print(df.isnull().sum())


# In[15]:


df.to_csv('edited_data.csv', index=False)


# In[16]:


get_ipython().system('pip install squarify')


# In[17]:



import squarify
import matplotlib.pyplot as plt


# In[18]:


counts = df['type1'].value_counts()


# In[20]:


sizes = counts.values


# In[21]:


labels = counts.index


# In[22]:


some_colors = ['#6991F0',
        '#A8AA79',
        '#7AC852',
        '#A7B822',
        '#F85887',
        '#EF812E',
        '#B99F38',
        '#F6D030',
        '#A0429F',
        '#BCA23B',
        '#6D5947',
        '#C12F27',
        '#70589A',
        '#6B3EE3',
        '#B6B8D0',
        '#9AD7D9',
        '#FF65D5',
        '#A991F0',]


# In[23]:


squarify.plot(sizes=sizes, label=labels, color=some_colors)


# In[28]:


type_counts = df['type1'].value_counts()


# In[29]:


top_types = type_counts.head(5)


# In[30]:


plt.bar(top_types.index, top_types.values)
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Top 5 Types')
plt.show()


# In[31]:


counts = df['type1'].value_counts()

# sort the counts in ascending order and get the top 5 rarest types
rarest = counts.sort_values(ascending=True).head(5)

# create a histogram of the rarest types
plt.bar(rarest.index, rarest.values)

# set axis labels and title
plt.xlabel('Type')
plt.ylabel('Frequency')
plt.title('Histogram of Rarest Types')
plt.show()


# In[ ]:





# In[32]:


df


# In[33]:


data = df.sort_values('weight_kg', ascending=False).head(50)


# In[34]:


sns.scatterplot(x='height_m', y='weight_kg', data=data)


# In[35]:


data_sorted = data.sort_values('weight_kg', ascending=False)


# In[36]:


data_top10 = data_sorted.head(10)


# In[37]:


names = data_top10['name'].tolist()
weights = data_top10['weight_kg'].tolist()


# In[38]:


for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {weights[i]}")


# In[39]:


data_sorted = data.sort_values('height_m', ascending=False)
data_top10 = data_sorted.head(10)
names = data_top10['name'].tolist()
height = data_top10['height_m'].tolist()
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - {height[i]}")


# In[40]:


names = data_top10['name'].tolist()
weights = data_top10['weight_kg'].tolist()
heights = data_top10['height_m'].tolist()
for i in range(len(names)):
    print(f"{i+1}. {names[i]} - Height: {heights[i]}, Weight: {weights[i]}")


# In[41]:


plt.figure(figsize=(12,6))
ax = sns.countplot(x='generation',data=df,order=df['generation'].value_counts().index)
ax.set_title('Pokemons per Generation')
ax.set(xlabel='Generation',ylabel='Count')


# In[42]:


valc_type1 = df['type1'].value_counts()


# In[43]:


valc_type2 = df['type2'].value_counts()
types_df = pd.concat([valc_type1,valc_type2],axis=1)


# In[44]:


types_df.plot(kind='bar',stacked=True, color=['red', 'green'],figsize=(12,6))


# In[45]:


df.corr()


# In[46]:


df=df.drop(['abilities', 'against_bug', 'against_dark', 'against_dragon',
       'against_electric', 'against_fairy', 'against_fight', 'against_fire',
       'against_flying', 'against_ghost', 'against_grass', 'against_ground',
       'against_ice', 'against_normal', 'against_poison', 'against_psychic',
       'against_rock', 'against_steel', 'against_water'], axis=1 )


# In[47]:



plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);


# In[48]:


correlation = df['attack'].corr(df['base_total'])
print(correlation)


# In[49]:


import matplotlib.pyplot as plt

x = df['attack']
y = df['base_total']
plt.scatter(x, y)
plt.xlabel('attack')
plt.ylabel('base_total')
plt.title('Correlation between attack and base_total')
plt.show()


# In[50]:


x = df['attack']
y = df['defense']
plt.scatter(x, y)
plt.xlabel('attack')
plt.ylabel('base_total')
plt.title('Correlation between attack and base_total')
plt.show()


# In[ ]:





# In[ ]:




