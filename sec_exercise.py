users=["Alice","Juan","Miguel","Fernando","Sara","Bernardo","Guillermo"]
print(len(users))

flag=True
while flag:
    print(f"Hola, mi nombre es Sharky, soy un robot")
    nombre=input("¿Cuál es su nombre?: ").strip().capitalize()
    if nombre in users:
        print(f"Bienvenido a la interfaz de usuario {nombre}")
        delete=input("¿Desea eliminar su cuenta?[s/n]: ").strip().lower()
        if delete=="s":
            users.remove(nombre)
            print(f"El usuario {nombre}, ha sido eliminado de forma exitosa")
        #flag=False
        else:
            print("Hasta luego.")
            break
    else:
        print(f"{nombre}, no es un usuario autorizado")
        add=input("¿Desea agregar esta cuenta de usuario a la base de datos?[s/n]: ").strip().lower()
        if add=="s":
            users.append(nombre)
            print(f"El usuario {nombre}, ha sido agregado de forma exitosa")
        else:
            print("Hasta luego.")
            break
        
    