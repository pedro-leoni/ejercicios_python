#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


listas = [5, 9, "pedro", -2, "estudiantes"]


# In[3]:


listas[0]


# # el numero entre [] con este formato lista[n] n sera el indice 

# In[4]:


listas[2]


# In[5]:


listas[2:]


# # puedo hacer las mismas cosas que con las cadenas de caracteres 

# In[6]:


primera_parte = [1, 2, 3, 4]
segunda_parte = [5, 6, 7]


# In[7]:


primera_parte + segunda_parte


# In[8]:


segunda_parte + [8, 9, 10]


# In[9]:


numeros = [1,2,3,4,9,6,7,8,9]


# In[10]:


numeros[4]=5 


# In[11]:


numeros


# # puedo cambiar el valor de 1 parte de esa lista, como mostre arriba

# In[13]:


numeros.append(10)


# In[14]:


numeros


# # con append agrego elementos al final de la lista

# In[15]:


numeros.append(10+1)


# In[16]:


numeros


# In[17]:


abecedario = ['A','B','C','D']


# In[18]:


abecedario[:2]


# In[19]:


abecedario[:2] = ['a', 'b']


# In[20]:


abecedario


# # anidar listas

# In[21]:


primero=[1,2,3]
segundo=[4,5,6]
tercero=[7,8,9]
cuarto=[10,11,12]
anidadas=[primero, segundo, tercero, cuarto]


# In[22]:


anidadas


# In[23]:


anidadas[0]


# In[24]:


anidadas[0][0]


# In[27]:


anidadas[2][1]


# # con el primer [] llamo a la lista y con el segundo [] a la posicion

# In[ ]:




