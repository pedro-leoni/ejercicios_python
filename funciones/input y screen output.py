#!/usr/bin/env python
# coding: utf-8

# # input

# In[1]:


ingreso = input("ingresa tu clase: ")


# In[2]:


listas = []


# In[6]:


print("Ingresa ya mismo 5 numeros")
for i in range(5):
    listas.append(input("ingresa un numero: "))
    


# In[7]:


listas


# In[8]:


# en este caso asignamos valores de input a una lista 


# # output (salida por pantalla)

# In[9]:


print("hola wacho")


# In[10]:


variable = 'pedro leoni'
otraVariable = 'genios estudiantes'


# In[13]:


forma = "el profesor {} y sus {} ".format(variable,otraVariable)


# In[14]:


forma


# In[15]:


#con .format formateo lo que vaya dentro de las {}, asignandole variables strings, el orden es importante 


# In[17]:



print(forma)


# In[18]:


forma = "el profesor {1} y sus {0} ".format(variable,otraVariable)


# In[19]:


forma


# In[20]:


#invertimos


# In[24]:


print('{:>50}'.format('perdro lenos'))


# In[25]:


#con {:>n} tabulamos n cantidad de espacios a a la derecha


# In[ ]:




