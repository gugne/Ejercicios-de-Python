#Hacer un programa en PYTHON que permita al usuario elegir calcular: 
# suma, resta, multiplicación y división entre dos números. 

def suma(x,y):
    z=x+y
    return z

def resta(x,y):
    z=x-y
    return z
def mult(x,y):
    z=x*y
    return z

def div(x,y):
    z=x/y
    return z

flag=True
while flag:
    print ("""
Bienvenido a nuestra calculadora.
Menú:
        1. Suma.
        2. Resta.
        3. Multiplicación.
        4. División.
        
        
        5. SALIR.
           """)

    menu=int(input("Digite el numero de extensión: "))
    if menu==1:
        print("1. Suma.")
        val1=int(input("Valor uno:"))
        val2=int(input("Valor dos:"))
        operación=suma(val1,val2)
        print(f"El resultado de la suma de {val1} y {val2}, es: {operación}")
        break
    elif menu==2:
        val1=int(input("Valor uno:"))
        val2=int(input("Valor dos:"))
        operación=resta(val1,val2)
        print(f"El resultado de la resta de {val1} y {val2}, es: {operación}")
        print("2. Resta.")
        break
    elif menu==3:
        print("3. Multiplicación.")
        val1=int(input("Valor uno:"))
        val2=int(input("Valor dos:"))
        operación=mult(val1,val2)
        print(f"El resultado de la multiplicación entre {val1} y {val2}, es: {operación}")
        break
    elif menu==4:
        print("4. División.")
        val1=int(input("Valor uno:"))
        val2=int(input("Valor dos:"))
        operación=div(val1,val2)
        print(f"El resultado de la división entre {val1} y {val2}, es: {operación}")
        break
    
    elif menu==5:
        print("Hasta luego")
        break
    else:
        print("Comando no válido, vuelva a intentar de nuevo con un número del 1-4 o ")
        continue
    
    


