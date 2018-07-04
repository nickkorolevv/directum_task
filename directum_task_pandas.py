
# coding: utf-8

# In[61]:


from pandas import read_csv as read
path = "company.csv"
data = read(path, delimiter=",")
empl_not_recommend_to_dismissal = data[(data.Education==1)&(data.Skills>90)&(data.NotFired)]
print(empl_not_recommend_to_dismissal)

