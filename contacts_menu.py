#Actividad 2:
# Escribir un programa que implemente una agenda. En la agenda se podrán
# guardar nombres y números de teléfono. El programa nos dará el 
# siguiente menú:
# Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en 
# la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo
# si no es correcto. Si el nombre no se encuentra, debe permitir ingresar 
# el teléfono correspondiente.
# Buscar: Nos pide una cadena de caracteres, # y nos muestras todos los 
# contactos cuyos nombres comiencen por dicha cadena.
# Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo 
# de la agenda.
# Listar: Nos muestra todos los contactos de la agenda.
# Implementar el programa con un diccionario.

contacts={
    "Mi número": 1113253232,
    "Bernardo Gomez": 3059203588,
    "Alexandra":3204155894,
    "Innovacion Digital":3004798801,
    "Angie Vitola":3006443301,
    "Pao":3007248438,
    "Andres": 3203444309,
    "Eloisa": 3203703531,
    "Mateo Vasquez": 3053404417,
    "Sara Acevedo": 11111111,
    "Sara Angostura": 2222222,
    "Sara Suarez": 333333333,
    
}
flag=True

print("""
Bienvenido a tu agenda interactiva
Menú:
    1.Añadir o Modificar contacto.
    2.Borrar un contacto.
    3.Buscar un contacto existente.
    4.Ver todos los contactos.
    
    Digite "s" para Salir.

""")

while flag:
    menu=input("Digite el indice del menú al que desea acceder[1-4]: ").strip()
    if menu=="s":
        break

#------AÑADIR CONTACTO----
    elif menu=="1":
        print(">Añadir o Modificar contacto.")
        contact_name=input("Ingrese el nombre de su nuevo contacto:").strip().title()
        phone_number=int(input(f"Ingrese el teléfono asignado para {contact_name}: "))
        if contact_name not in contacts:
            contacts[contact_name]= phone_number
        else:
            print(f"Ya existe una entrada con el nombre {contact_name}")
            for key,values in contacts.items():
                if contact_name in key:
                    print("  CONTACTO   ", "   TELÉFONO  ")
                    print(key,"    ",values)
            rewrite=input(f"Desea sobre-escribir el contacto '{contact_name}' [s/n]: ").strip().lower()
            if rewrite=="s":
                contacts[contact_name]= phone_number
            else:
                continue                             

#------BORRAR CONTACTO----    
    elif menu=="2":
        delete_contact=0
        print("Ingreses 'b'  para regresar al menú principal")
        while delete_contact !="B":
            print(">Borrar un contacto existente.")
            delete_contact=input("Ingrese el nombre de un contacto existente para borrarlo:").strip().title()
            if delete_contact=="B":
                print("""
Bienvenido a tu agenda interactiva
Menú:
    1.Añadir o Modificar contacto.
    2.Buscar un contacto existente.
    3.Borrar un contacto.
    4.Ver todos los contactos.
    
    Digite "s" para Salir.

                    """)    
                continue
            elif delete_contact in contacts:
                contacts.pop(delete_contact)
                print(f"La entrada {delete_contact}, ha sido eliminada exitosamente.")
                delete_contact="B"
            else:
                print(f"No se puede borrar la entrada '{delete_contact}' porque no existe")
                print("""
Intentelo nuevamente.
(...)
(...)
(...)               
                    """)
                print("Si no conoce la entrada que desea borrar, ingreses 'b'  para regresar al menú principal")

#---------BUSCADOR---------    
    elif menu=="3":
        print(">Buscar un contacto existente.")
        search_contact=input("Buscar:").strip().title()
        contador=0
        print("  CONTACTO   ", "   TELÉFONO  ")
        for key,values in contacts.items():
            if search_contact in key or search_contact in str(values):
                print(key,"    ",values)
                contador+=1
            else:
                continue 
        else:
            print(f"Se encontraron un total de '{contador}' coincidencias")
        if search_contact in contacts:
            print("holiii")

#------VER CONTACTOS----
    elif menu=="4":
        print(">Ver todos los contactos.")
        print("  CONTACTO   ", "   TELÉFONO  ")
        for key,values in contacts.items():
            print(key,"    ","--->", values)
