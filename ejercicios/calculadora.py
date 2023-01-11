#!/usr/bin/env python
# coding: utf-8

# In[1]:


inicio = input('para empezar escribe "inicio"')
while (inicio == inicio):
    accion = int(input("""elige cualquiera de estas opciones por su numero
    1 - realizar una suma
    2 - realizar multiplicacion
    3 - realizar division
    4 - realizar potencia
    5 - realizar resta
    0 - salir de la aplicacion"""))
    if accion == 1:
        num1 = float(input("ingresa el primer numero a sumar "))
        num2 = float(input("ingresa el segundo numero a sumar "))
        print("El resultado de tu suma es ",num1+num2)
    elif accion == 2: 
        num1 = float(input("ingresa el primer numero a multiplicar "))
        num2 = float(input("ingresa el segundo numero a multiplicar "))
        print("El resultado de tu multiplicacion es ",num1*num2)
    elif accion == 3:
        num1 = float(input("ingresa el dividendo "))
        num2 = float(input("ingresa el divisor "))
        print("el resultado de tu division es ",num1/num2," el resto de tu division es ",num1%num2)
    elif accion == 4:
        num1 = float(input("ingresa el numero base "))
        num2 = float(input("ingresa el exponente "))
        print("el resultado de tu potencia es ",num1**num2) 
    elif accion == 5:
        num1 = float(input("ingresa el primer numero a restar "))
        num2 = float(input("ingresa el segundo numero a restar "))
        print("el resultado de tu resta es ",num1-num2)
    elif accion == 0:
        print("gracias por usar la calculadroga")
        break
    
    
    
    


# In[ ]:




