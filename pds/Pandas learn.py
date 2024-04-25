#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


obje=pd.Series([1, "Ali", 3.5, "Hey"])
obje


# In[3]:


obje[2]


# In[4]:


obje.values


# In[7]:


obje=pd.Series([1, "Ali", 3.5, "Hey"],index=["a","b","c","d"])
obje


# In[9]:


obje["b"]


# In[10]:


obje.index


# In[11]:


puan={"Ali":90, "Can":80, "Efe":75, "Berra":95}
nt=pd.Series(puan)
nt


# In[12]:


nt["Can"]


# In[13]:


nt[nt>85]


# In[14]:


nt<85


# In[15]:


nt["Can"]=60


# In[16]:


nt


# In[17]:


nt[nt<80]=83


# In[18]:


nt


# In[19]:


"Efe" in nt


# In[20]:


"Ahmet" in nt


# In[21]:


nt/10


# In[22]:


nt**2


# In[23]:


nt.isnull() //eksik veri yok


# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


import pandas as pd
ufo = pd.read_csv('https://raw.githubusercontent.com/erkansirin78/datasets/master/uforeports.csv')
print(ufo)


# In[ ]:





# In[ ]:





# In[41]:


import pandas as pd
dm = pd.read_csv(r'C:\Users\Ceren\Documents\tercih.csv', encoding='ISO-8859-1')
print(dm)


# In[42]:


df.dtypes


# In[39]:


df = pd.read_excel(r'C:\Users\Ceren\Desktop\tercih.xlsx')
print(df)


# In[44]:


df.head()


# In[49]:


df.Müşteriler.unique()


# In[50]:


df.Müşteriler.nunique()//kaç tane tür


# In[51]:


get_ipython().run_line_magic('matplotlib', 'inline')
df.Müşteriler.Year.plot(kind="hist") //yıllara göre histogramı


# In[ ]:





# In[56]:


mk = pd.read_excel(r'C:\Users\Ceren\Desktop\makeup.xlsx')
print(mk)


# In[62]:


get_ipython().run_line_magic('matplotlib', 'inline')
mk.Günlüksatışsayısı.Year.plot(kind="hist") 


# In[63]:


import matplotlib.pyplot as plt
import pandas as pd

# Örnek bir DataFrame oluşturalım
veri = {'Year': [2018, 2018, 2019, 2019, 2020, 2020],
        'Günlüksatışsayısı': [100, 120, 150, 130, 200, 180]}
mk = pd.DataFrame(veri)

# Histogramı çizelim
mk['Günlüksatışsayısı'].plot(kind='hist')
plt.show()


# In[3]:


import matplotlib.pyplot as plt
import pandas as pd

# Veri tablosu oluşturalım
veri = {'Ürünler': ['Maskara', 'Ruj', 'Gloss', 'Krem', 'Parfüm', 'Maske', 'Deodorant', 'Saçkremi', 'Kapatıcı', 'Pudra', 'Allık', 'Fondöten', 'Highliter', 'Güneşkremi', 'Dudakyağı', 'Farpaleti'],
        'Günlüksatışsayısı': [100, 180, 200, 50, 20, 68, 46, 12, 24, 10, 65, 30, 16, 14, 8, 10],
        'Year': [2010, 2011, 2011, 2011, 2012, 2012, 2012, 2012, 2022, 2022, 2022, 2022, 2023, 2023, 2023, 2024]}

# DataFrame oluşturalım
mk = pd.DataFrame(veri)

# Histogramı çizelim
mk['Günlüksatışsayısı'].plot(kind='hist')
plt.show()


# In[5]:


veri={"isim": ["Ali","Can","Ayşe","Buse","Alp","Nur"],
     "puan":[90,80,85,75,95,60],
     "spor":["Futbol","Kayak","Yüzme","Tenis","Karate","Sörf"],
     "cinsiyet":["E","E","K","K","E","K"]}
df=pd.DataFrame(veri)
df


# In[7]:


df.head() 


# In[8]:


df.tail()


# In[9]:


df.tail(2)


# In[10]:


df.head(3)


# In[11]:


df=pd.DataFrame(veri,columns=["isim","spor","cinsiyet","puan"])
df


# In[13]:


df=pd.DataFrame(veri,columns=["isim","spor","cinsiyet","puan"],
               index=["bir","iki","üç","dört","beş","altı"])
df


# In[14]:


df["spor"]


# In[15]:


sutunlarım=["isim","spor"]
df[sutunlarım]


# In[18]:


df.loc[["bir","üç"]]


# In[19]:


df


# In[21]:


df["geçti"]=df.puan>80
df


# In[23]:


notlar={"Matematik":{"Ali":85,"Efe":90,"Nur":95},
       "Fizik":{"Ali":90,"Efe":80,"Nur":75}}
puan=pd.DataFrame(notlar)
puan


# In[24]:


puan.T


# In[25]:


puan.index.name="isim"
puan.columns.name="ders"
puan


# In[26]:


puan.values


# In[ ]:




