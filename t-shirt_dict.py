
ventas={
    "Cartagena": ["M", "S", "L", "L", "L", "L", "L", "XL", "XXL", "S", "S", "L", "M", "M", "M", "S", "S", "M", "M"],

    "Barranquilla": ["S", "S", "L", "M", "XL", "S", "L", "M", "M", "M", "S", "S", "M", "M", "XL", "S", "M", "S", "XXL", "XL", "L"],

    "Medellín": ["L", "L", "XL", "XXL", "S", "S", "S", "S", "L", "L", "L", "XL", "XL", "XL", "XL", "XL", "L", "L", "L", "L", "L", "L", "L", "L", "L", "M", "M", "S", "S", "S", "S", "XL", "L"],

    "Bogotá": ["M", "S", "S", "M", "M", "XL", "S", "M", "S", "S", "S", "L", "S", "S", "S", "M", "M","M", "M", "M", "M", "M", "M", "L", "L", "XL", "XL", "XL", "XL", "XL", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "L", "L", "XL", "XL", "XL", "XL", "XL" ]
}

#print(ventas)
#Diseña un programa que lea el diccionario e indique el total de ventas,
# las tallas más vendidas y el total de tallas por ciudad.


for ciudad,venta in ventas.items():
 
    if ciudad=="Cartagena":
        print ("Cartagena:",end=" ")
        Cartagena_S=venta.count("S")
        Cartagena_M=venta.count("M")
        Cartagena_L=venta.count("L")
        Cartagena_XL=venta.count("XL")
        Cartagena_XXL=venta.count("XXL")
        total_cartagena=len(venta)
        print (f"[S:{Cartagena_S}], [M:{Cartagena_M}], [L:{Cartagena_L}], [XL:{Cartagena_XL}], [XXL:{Cartagena_XXL}] TOTAL: {total_cartagena}")
    elif ciudad=="Barranquilla":
        print ("Barranquilla:",end=" ")
        Barranquilla_S=venta.count("S")
        Barranquilla_M=venta.count("M")
        Barranquilla_L=venta.count("L")
        Barranquilla_XL=venta.count("XL")
        Barranquilla_XXL=venta.count("XXL")
        total_barranquilla=len(venta)
        print (f"[S:{Barranquilla_S}], [M:{Barranquilla_M}], [L:{Barranquilla_L}], [XL:{Barranquilla_XL}], [XXL:{Barranquilla_XXL}] TOTAL: {total_barranquilla}")
    elif ciudad=="Medellín":
        print ("Medellín:",end=" ")
        Medellin_S=venta.count("S")
        Medellin_M=venta.count("M")
        Medellin_L=venta.count("L")
        Medellin_XL=venta.count("XL")
        Medellin_XXL=venta.count("XXL")
        total_medellin=len(venta)
        print (f"[S:{Medellin_S}], [M:{Medellin_M}], [L:{Medellin_L}], [XL:{Medellin_XL}], [XXL:{Medellin_XXL}] TOTAL: {total_medellin}")
    elif ciudad=="Bogotá":
        print ("Bogotá:",end=" ")
        Bogota_S=venta.count("S")
        Bogota_M=venta.count("M")
        Bogota_L=venta.count("L")
        Bogota_XL=venta.count("XL")
        Bogota_XXL=venta.count("XXL")
        total_bogota=len(venta)
        print (f"[S:{Bogota_S}], [M:{Bogota_M}], [L:{Bogota_L}], [XL:{Bogota_XL}], [XXL:{Bogota_XXL}] TOTAL: {total_bogota} Camisetas")

total_S=Cartagena_S+Barranquilla_S+Medellin_S+Bogota_S
total_M=Cartagena_M+Barranquilla_M+Medellin_M+Bogota_M
total_L=Cartagena_L+Barranquilla_L+Medellin_L+Bogota_L
total_XL=Cartagena_XL+Barranquilla_XL+Medellin_XL+Bogota_XL
total_XXL=Cartagena_XXL+Barranquilla_XXL+Medellin_XXL+Bogota_XXL
valor_total= (total_S*2500)+(total_M*3400)+(total_L*5200)+(total_XL*6000)+(total_XXL*9000)
TOTAL= total_cartagena+total_barranquilla+total_medellin+total_bogota
print()
print (F"Total de camisetas vendidas: {TOTAL}")
print(f"""
Discriminadas de la siguiente forma:

      *Talla S: {total_S}
      *Talla M: {total_M}
      *Talla L: {total_L}
      *Talla XL: {total_XL}
      *Talla XXL: {total_XXL}
      """)
print (f"Ventas totales: ${valor_total}")
total_talla=[["Talla S",total_S],["Talla M",total_M],["Talla L",total_L],["Talla XL",total_XL],["Talla XXL",total_XXL]]


mas_vendido=0
menos_vendido=100

for i,k in total_talla:
    if k>mas_vendido:
        mas_vendido=k
        talla_mv=i
    if k<menos_vendido:
        menos_vendido=k
        talla_menos=i
else:
    print (f"La talla más vendida fue: {talla_mv} y la menos vendida fue: {talla_menos}")