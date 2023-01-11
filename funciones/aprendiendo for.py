#!/usr/bin/env python
# coding: utf-8

# # for 
# ### sirve para recorrer listas, podemos hacer las cosas de una manera mas optima que con un while
# prestar principal atencion cuando se trata de estos bucles ASEGURARSE DE QUE TERMINEN, si quedan en un ciclo infinito capaz que hasta tenemos que borrar el notebook
# 

# In[1]:


lista = [1,2,3,4,5,6,7,8,9]
indice = 0
while indice < len(lista):
    print(lista[indice])
    indice+=1


# In[3]:


for recorrer in lista:
    print(recorrer)


# el for siempre necesita un in, declaramos la variable del for (recorrer), llamamos a la lista y la imprimimos, luego podemos toquetearla bastante a ese recorrido 

# In[1]:


lista = [1,2,3,4,5,6,7,8,9]
indice = 0

for recorrer in lista:
    lista[indice] *= 10 
    indice += 1
lista


# optimizando aun mas la funcion anterior

# In[2]:


for indice, recorrer in enumerate(lista):
    lista[indice] *= 10
lista


# esta con un 0 mas porque tomo los valores de lista asignados en la funcion anterior, si volviera a declarar la lista o si hubiera limpiado las variables se veria igual

# In[3]:


string = 'Pedro'
for caracteres in string:
    print(caracteres)


# In[4]:


for i in range(10):
    print(i)


# otro ejemplo de una variable declarada dentro del for (esta bien y se puede) y con range podemos hacer otro recorrido por

# In[5]:


for i in [1,2,3,4]:
    print(i)


# In[6]:


list(range(10))


# In[7]:


list(range(i))


# cuando listamos los valores de la lista i declarada anteriormetne vemos que nos devuelve 4 valores que vienen 1 abajo de los originales, esto es porque en realidad la lista nos devuelve las posiciones enumeradas y no el contenido de la variable otro ej

# In[ ]:




