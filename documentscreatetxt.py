#Actividad 1: Escribir una función que pida un número entero entre 1 y 10 y guarde
# en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
# donde n es el número introducido.

def tabla_n (x):
    create=open("tabla_"+str(x)+".txt", "w+")
    for i in range(11):
        resultado=x*i
        create.write (f"{x}*{i}= {resultado}")
        create.write("\n")
        

flag=True
while flag:
    num=int(input("Inserte su número:"))
    if num>10:
        print(f"El número debe ser un número entre 1 y 10. Tu número es {num}")
    else:
        tabla_n (num)
        print("El archivo ha sido creado exitosamente")
    