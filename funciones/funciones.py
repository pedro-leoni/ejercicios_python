#!/usr/bin/env python
# coding: utf-8

# # funciones

# In[1]:


def estudiantes():
    print("genios mis estudiantes")
estudiantes()


# In[2]:


estudiantes


# In[3]:


estudiantes()


# In[4]:


#con def creamos la funcion, le damos el nombre, cerramos con : y dentro de la tabulacion va la funion 


# In[7]:


def tabla_del_7():
    for x in range(10):
        print("7 * {} = {} ".format(x,x*7))


# In[8]:


tabla_del_7()


# In[12]:


#en las funciones las variablas tienen que estar declaradas previamente, la variable que se crea dentro de la funcion se queda
#dentro de la misma y al momento de usarla afuera nos va a causar problemas. Es un buen habito siempre "inicializarlas" afuera
#A MENOS QUE LO HAGAMOS DE FORMA GLOBAL COMO EL EJEMPLO DE ABAJO


# In[13]:


def advierto():
    variable = 'pedro'


# In[14]:


advierto()


# In[15]:


variable


# In[16]:


def advierto():
    global variable
    variable = 'pedro'
    print(variable)
advierto()

variable='leoni'
advierto()
print(variable)


# In[17]:


#con el global permitimos que fuera de la funcion se pueda utilizar una variable, pero no modificarla como vemos en el ejemplo
#de la linea 16


# In[ ]:




