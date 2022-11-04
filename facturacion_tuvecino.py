#1. Cantidad de productos a procesar (N)
#2. Cada pruducto: 
#                   a. Código.
#                   b. Nombre del producto. 
#                   c. Cantidad comprada. 
#                   d. Velor unitario. 
#                   e. Tipo de IVA: [1. Excento de iva, 2. Bienes (5%), 3. General (19%)]





products={
    1: ["Manzana",1500,5],
    2: ["Manzana Verde",1800,5],
    3: ["Arroz Diana 500g",2000,0],
    4: ["Jabón Rey", 1000, 19],
    5: ["Maiz Pira 1KG", 1500, 19],
    6: ["Quezo Mozarella 500gr", 7500, 0],
    7: ["Jamon Zenu", 8000, 0],
    8: ["Chunky cachorros 1KG", 5000, 5]
}

flag=True
while flag:
    print("""
Bienvenido al sistema de facturación
Menú:
    1. Panel de administración.
    2. Facturación.
    3. Salir.
          """)
    menu=(input("Ingrese el índice de menú al que desea acceder: "))
    if menu== "3":
        print ("Se ha cerrado el programa exitosamente")
        break
    elif menu== "1":
        while flag: #[PANEL DE ADMINISTRACIÓN: AGREGAR, BORRAR O BUSCAR PRODUCTO.]
            print ("""
-----     [Panel de administración]     -----

    1. Agregar producto.
    2. Borrar producto.
    3. Buscar producto. 
    4. Salir.
        """)
            submenu=(input("Ingrese el índice de menú al que desea acceder: "))
            if submenu=="4":
                print ("Volviendo al menú principal. Espere un momento")
                break
            elif submenu== "1": #Agrega producto, si ya existe, ofrece posibilidad de remplazarlo en el mismo código asignado.
                print (">> Agregar producto.")
                code= len(products)
                code=code+1
                #code=int(input("Ingrese el código del producto:"))
                name=input("Ingrese el nombre del producto: ").strip().title()
                price=float(input("Ingrese el precio unitario del producto:"))
                tax= float(input("Ingrese el valor del IVA para este producto (0, 5 o 19): "))
                for key,value in products.items():
                    #print(i)
                    if value[0]==name:
                        print(f"Ya existe una entrada asignada con el nombre {name}")
                        print("CÓDIGO     ", "   NOMBRE  ")
                        print(key, "            ", value[0])
                        rewrite=input(f"Desea sobre-escribir la entrada para '{name}' [s/n]: ").strip().lower()
                        if rewrite=="s":
                            products[key]= [name,price,tax]
                            break
                        else:
                            break                             
                else:
                    products[code]=[name,price,tax]  
                print(products)
                
            elif submenu== "2":
                print (">> Borrar un producto.")
                print ("Al borrar un producto no podrá volver a usar el código asignado anteriormente.")
                dyknow=input("¿Conoce el código del producto que desea borrar? (s/n): ").strip().lower()
                if dyknow=="s":
                    delete=int(input("Ingrese el código asignado al producto:"))
                    if delete in products.keys():
                        for key in products.keys():
                            if delete==key:
                                products[key]= ["Deleted"]
                                break
                    else:
                        print("\n El código ingresado aún no ha sido asignado")
                            
            elif submenu== "3":
                print (">> Buscar producto.")
                buscar=input("Ingrese palabra clave: ").strip().title()
                print("CÓDIGO     ", "   NOMBRE  ")
                matches=0
                for key,value in products.items():
                    if buscar in value[0]:
                        print(key, "            ", value[0])
                        matches+=1
                else:
                    print(f"Se han encontrado {matches} coincidencias")
            else:
                print("El indice ingresado no existe. Intente nuevamente")
    
    #[/PANEL DE ADMINISTRACIÓN: AGREGAR, BORRAR O BUSCAR PRODUCTO.]


    elif menu== "2": #[FACTURACIÓN: TOTAL DE PRODUCTOS ]
        codigo=[]
        nombre=[]
        cantidad=[]
        valor=[]
        tipo_iva=[]
        factura=[]                       
        print ("> Facturación.")
        n=int(input("Cantidad de productos diferentes a procesar: "))
        for i in range (n):
            product=int(input("Inserte el código del producto:"))
            while product not in products.keys():
                print("Este código no ha sido asignado a ningún producto, intente nuevamente.")
                product=int(input("Inserte el código del producto: "))   
            quantity=int(input(f"¿Cuántas unidades de Unidades de '{products[product][0]}' desea llevar el cliente: "))
            #3. Almacenar en listas, una lista por cada elemento de entrada: [Codigo, nombre, cantidad, valor, tipo de iva]
            codigo.append(product)
            nombre.append(products[product][0])
            cantidad.append(quantity)
            valor.append(products[product][1])
            tipo_iva.append(products[product][2])
#5. Calcular para cada producto: 
#           a. Valor del producto (Cantidad x Valor unitario).
#           b. Valor del IVA por producto (a*+Iva). 
#           c. Valor total de la compra (suma de lo N productos con el IVA) 
#           d. Valor total del IVA (suma del IVA de todos los productos.) 
#           e. Información calculada para cada producto: [Valor producto, valor iva, valor final.] -Almacenar un una lista-
            valor_unitario=products[product][1]
            valor_producto=valor_unitario*quantity
            valor_iva=valor_producto*((products[product][2])/100)
            valor_final=valor_producto+valor_iva
            factura.append([products[product][0],valor_unitario,quantity,valor_producto,valor_iva,valor_final])
                      
        else:
            #4. Elemento de control: Imprimir longitud de la listas: [Código], [nombre], [cantidad], [valor], [tipo de iva]
            print(f"La lista código tiene: {len(codigo)} Elementos")
            print(f"La lista nombre tiene: {len(nombre)} Elementos")
            print(f"La lista cantidad tiene: {len(cantidad)} Elementos")
            print(f"La lista valor tiene: {len(valor)} Elementos")
            print(f"La lista tipo de Iva tiene: {len(tipo_iva)} Elementos")
            
            #IMPRESIÓN DE LA FACTURA EN PANTALLA:
                    
            print("FACTURA ELECTRÓNICA")
            print ("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format('PRODUCTO','PRECIO UNITARIO','CANTIDAD','SUBTOTAL SIN IVA', "IVA", "SUBTOTAL CON IVA"))
            for i in factura:
                for j in i:
                    print ("{:<21}".format(j), end="")
                print()
                    #print(j,end="           ")
                #print()
            #print(factura)
            
            
    else:
        print("El indice ingresado no existe. Intente nuevamente")



