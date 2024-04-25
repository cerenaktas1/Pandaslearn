#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


obje=pd.Series(np.arange(5),index=["a","b","c","d","e"])
obje


# In[6]:


obje["c"]


# In[7]:


obje[2]


# In[8]:


obje[0:3]


# In[9]:


obje[[0,2]]


# In[10]:


obje[obje<2]


# In[11]:


obje["a":"c"]


# In[12]:


obje["b":"c"]=5


# In[13]:


obje


# In[5]:


veri=pd.DataFrame(np.arange(16).reshape(4,4),index=["Bursa","Ankara","Rize","Istanbul"],
                 columns=["bir","iki","uc","dort"])
veri


# In[15]:


veri["iki"]


# In[16]:


veri[["bir","iki"]]


# In[17]:


veri[:3]


# In[18]:


veri[veri["dort"]>5]


# In[19]:


veri[veri<5]=0


# In[20]:


veri


# In[21]:


veri.iloc[1]


# In[23]:


veri.iloc[1,[1,2,3]]


# In[24]:


veri.iloc[[1,3],[1,2,3]]


# In[25]:


veri.loc["Rize",["bir","iki"]]


# In[26]:


veri.loc[:"Rize","dort"]


# In[3]:


veri=pd.Series(np.arange(5))
veri


# In[28]:


veri[-1]


# In[6]:


import pandas as pd


# In[7]:


s=pd.Series([1,2,3,4],index=["a","b","c","d"])
s


# In[8]:


s["a"]


# In[9]:


s2=s.reindex(["b","d","a","c","e"])
s2


# In[10]:


s3=pd.Series(["mavi","sarı","mor"],index=[0,2,4])
s3


# In[11]:


s3.reindex(range(6),method="ffill")


# In[12]:


import numpy as np 


# In[13]:


df=pd.DataFrame(np.arange(9).reshape(3,3),index=["a","c","d"],
               columns=["ali","efe","can"])
df


# In[14]:


df2=df.reindex(["d","c","b","a"])
df2


# In[15]:


isim=["efe","nur","ali"]
df.reindex(columns=isim)


# In[16]:


df.loc[["c","d","a"]]


# In[17]:


s=pd.Series(np.arange(5.),index=["a","b","c","d","e"])
s


# In[18]:


yeni_s=s.drop("b")
yeni_s


# In[19]:


s.drop(["c","d"])


# In[20]:


veri=pd.DataFrame(np.arange(16).reshape(4,4),index=["ali","can","efe","nur"],
                columns=list("ABCD") )
veri


# In[21]:


veri.drop(["efe"])


# In[22]:


veri.drop("A",axis=1)


# In[23]:


veri.drop("ali",axis=0)


# In[24]:


veri.mean()


# In[25]:


veri.mean(axis=0)


# In[26]:


veri.mean(axis=1)


# In[27]:


veri.mean(axis="index")


# In[28]:


veri.mean(axis="columns")


# In[1]:


import pandas as pd ; import numpy as np


# In[2]:


s1=pd.Series(np.arange(4),index=["a","c","d","e"])
s2=pd.Series(np.arange(5),index=["a","c","e","f","g"])


# In[3]:


s1


# In[4]:


s2


# In[5]:


s1+s2


# In[6]:


df1=pd.DataFrame(np.arange(6).reshape(2,3),columns=list("ABC"),index=["ali","efe"])
df2=pd.DataFrame(np.arange(9).reshape(3,3),columns=list("ACD"),index=["ali","can","efe"])


# In[7]:


df1


# In[8]:


df2


# In[9]:


df1+df2


# In[10]:


df1.add(df2,fill_value=0)


# In[11]:


df1*3


# In[12]:


df1.mul(3)


# In[13]:


df2


# In[14]:


s=df2.iloc[1]
s


# In[15]:


df2-s


# In[16]:


s2=df2["A"]
s2


# In[17]:


df2.sub(s2,axis="index")


# In[18]:


vs=pd.DataFrame(np.random.randn(4,3),columns=list("ABC"),
               index=["ali","berk","can","efe"])
vs


# In[19]:


np.abs(vs)


# In[20]:


f=lambda x:x.max()-x.min()


# In[21]:


vs.apply(f)


# In[22]:


vs.apply(f,axis=1)


# In[23]:


def f(x):
    return x**2


# In[24]:


vs.apply(f)


# In[25]:


import pandas as pd ; import numpy as np


# In[26]:


s=pd.Series(range(5),index=["e","d","a","b","c"])
s


# In[27]:


s.sort_index()


# In[29]:


df=pd.DataFrame(np.arange(12).reshape(3,4),index=["iki","bir","üç"],
               columns=["d","a","b","c"])
df


# In[30]:


df.sort_index()


# In[32]:


df.sort_index(axis=1)


# In[34]:


df.sort_index(axis=1,ascending=False)


# In[35]:


s2=pd.Series([5,3,-1,9])
s2


# In[36]:


s2.sort_values()


# In[37]:


df2=pd.DataFrame({"a":[5,3,-1,9],"b":[1,-2,0,5]})
df2


# In[38]:


df2.sort_values(by="b")


# In[39]:


df2.sort_values(by=["b","a"])


# In[53]:


veri = pd.read_csv(r"C:\Users\Ceren\Desktop\tercihh.csv", encoding='ISO-8859-9')
veri.head()


# In[56]:


veri["Müşteriler;Tercih Edilen Ayakkabı Markaları"].sort_values()


# In[54]:


print(veri.columns)


# In[57]:


veri["Müşteriler;Tercih Edilen Ayakkabı Markaları"].sort_values(ascending=False)


# In[1]:


import pandas as pd ; import numpy as np


# In[4]:


df=pd.DataFrame([[2.4,np.nan],[6.3,-5.4],[np.nan,np.nan],[0.75,-1.3]],
               index=["a","b","c","d"],columns=["bir","iki"])
df


# In[5]:


df.sum()


# In[6]:


df.sum(axis=1) #satırların toplamı


# In[7]:


df.mean(axis=1) #satırların ortalaması


# In[8]:


df.mean(axis=1,skipna=False)  #eksik veri satırları hesaplanmadı


# In[10]:


df.idxmax() #her iki sütün için  max değere sahip olan index değeri


# In[11]:


df.idxmin() #satrıv e sutunlardakı mın değer


# In[12]:


df.cumsum()  #kümülatif dağılımı her bir sutün sırayla toplandı


# In[13]:


df.describe()


# In[15]:


s=pd.Series(["b","b","b","b","c","c","a","a","a"])
s


# In[16]:


s.unique()   #tek olarak görmek istersek


# In[17]:


s.value_counts()  #değerin sıklığınnı öğrenmek için


# In[19]:


x=s.isin(["b","c"])  #b ve c nin her bir satırda olup olmadığı
x


# In[20]:


s[x]    #değerlerin olduğu satırları görmek istersek


# In[ ]:




