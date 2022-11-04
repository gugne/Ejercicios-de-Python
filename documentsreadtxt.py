def tabla_n (x):
    read_it=open("tabla_"+str(x)+".txt", "r")
    if read_it.mode == "r":
        content= read_it.read()
        print (content)

flag=True
while flag:
    num=int(input("Inserte su número:"))
    if num>10:
        print(f"El número debe ser un número entre 1 y 10. Tu número es {num}")
    else:
        tabla_n (num)
        print("Contenido del archivo leído exitosamente")