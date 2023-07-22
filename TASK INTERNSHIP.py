#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# # Read the dataset

# In[3]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.head()


# # Display all the columns of the dataset where datatypes,column name,count and overall memory

# In[4]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.info()


# # Find the total no of people based on their count age,income,gender

# In[5]:


dv["age"]=dv["age"]*70


# In[6]:


dv


# In[7]:


dv["income"]=dv["income"]*15000
dv


# In[8]:


dv["gender"].value_counts()


# # Find the value count of different data types

# In[9]:


dv["age"].value_counts()


# In[10]:


dv["visits"].value_counts()


# In[11]:


dv["illness"].value_counts()


# # Describing the info of the datatypes

# In[12]:


import pandas as pd


# In[13]:


dv.describe()


# In[14]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.dropna(axis = 0)


# In[15]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.fillna("20")


# In[67]:


dv.ffill(axis = 0)


# In[66]:


dv.bfill(axis = 0)


# In[28]:


dv.drop_duplicates()


# In[29]:


dv.drop_duplicates(subset=['private'])


# In[30]:


dv.drop_duplicates(subset=['freerepat','illness'])


# In[31]:


dv.shape


# In[32]:


dv.columns


# In[33]:


dv.isna().sum()


# # Analyzing the variables

# In[34]:


import pandas as pd
dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.visits.unique()


# In[35]:


dv.gender.unique()


# In[36]:


dv.freerepat.unique()


# In[37]:


dv.private.unique()


# In[38]:


dv.nchronic.unique()


# In[39]:


dv.age.unique()


# In[40]:


dv.income.unique()


# In[41]:


dv.nunique()


# # Exploring and Plotting the data

# In[42]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[43]:


dv=pd.read_excel("DoctorVisits (2).xlsx")
dv.head()


# In[44]:


sns.histplot(dv['age'], bins=60)


# In[46]:


sns.histplot(dv['age'], bins=65)
plt.xlabel('Age')
plt.ylabel('visit')
plt.title('Distribution of Patients Ages')
plt.show


# In[47]:


gender_counts = dv['gender'].value_counts()
sns.barplot(x=gender_counts.index,y=gender_counts.values)
plt.xlabel('gender')
plt.ylabel('visit')
plt.title('Distribution of Patient Gender')
plt.show()


# In[48]:


sns.histplot(dv['visits'], bins=35)
plt.xlabel('visits')
plt.ylabel('income')
plt.title('visit analysis')
plt.show


# # Observations

# In[51]:


labels=['visits','illness','reduced','health']
sizes=[25,20,13,5]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[52]:


x = [16,14,12,18,20] 
y = [10,12,14,9,7]
plt.plot(x,y)
plt.xlabel('nchronic')
plt.ylabel('Ichronic')
plt.title('Disease analysis')
plt.show()


# In[53]:


labels=['freerepat','freepoor']
sizes=[30,40]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('patient health insurance analysis')
plt.show()


# In[54]:


labels=['visits','illness']
sizes=[70,60]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[55]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[56]:


labels=['visits','illness','reduced','health']
sizes=[40,25,20,10]
plt.pie(sizes,labels=labels,autopct = '%1.1f%%')
plt.title('overall analysis of patients')
plt.show()


# In[57]:


x = [20,50,66,99,10] 
y = [30,30,46,80,55]
plt.scatter(x,y)
plt.xlabel('freepoor')
plt.ylabel('private')
plt.title('insurance analysis')
plt.show()


# In[58]:


dv=pd.read_excel("DoctorVisits (2).xlsx")


# In[61]:


dv.hist(figsize=(20,25))


# In[62]:


x= (dv[['health']]==1).sum()
y= (dv[['health']]==0).sum()
percent= ((x*y)/(x+y))*100
percent


# # Conclusion

# a) We analyzed the dataset which is about the visiting of patients to doctor.
# 

# b) We analyzed all the variables of the dataset

# c) Female gender is more in number comparable to male gender

# d) Income doesn't create any kind of difference in the dataset it made it's consistency path asusally

# e) Coming to the factor of age condition and health condition those are some what creating some kind of difference in the analytics.

# f) NO,Any patient doesn't belongs to freepoor as they didn't get any help from the government due to their low income.
# 

# g) Private doesn't play much role in the dataset
