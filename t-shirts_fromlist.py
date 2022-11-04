#Una empresa de camisetas ha tenido muchos problemas últimamente 
# con sus últimas ventas para las ciudades de Cartagena, Barranquilla, 
# Medellín y Bogotá. Luego de culminar la temporada no han contado 
# adecuadamente las unidades vendidas y están muy preocupados porque 
# no saben cuál es el total vendido hasta la fecha. El gerente nacional
# se ha puesto en contacto contigo para discutir como seria el programa
# que necesitan y te ha enviado la siguiente tabla:

#Talla      Precio

#"S"          $2500

#"M"        $3400

#"L"           $5200

#"XL"        $6000

#"XXL"     $9000

#“Estos serían los precios de cada camiseta” te dijo en la reunión, además de esto 
# te envía un diccionario indicando cada una de las unidades en la ciudad correspondiente:

ventas={
    "Cartagena": ["M", "S", "L", "L", "L", "L", "L", "XL", "XXL", "S", "S", "L", "M", "M", "M", "S", "S", "M", "M"],

    "Barranquilla": ["S", "S", "L", "M", "XL", "S", "L", "M", "M", "M", "S", "S", "M", "M", "XL", "S", "M", "S", "XXL", "XL", "L"],

    "Medellín": ["L", "L", "XL", "XXL", "S", "S", "S", "S", "L", "L", "L", "XL", "XL", "XL", "XL", "XL", "L", "L", "L", "L", "L", "L", "L", "L", "L", "M", "M", "S", "S", "S", "S", "XL", "L"],

    "Bogotá": ["M", "S", "S", "M", "M", "XL", "S", "M", "S", "S", "S", "L", "S", "S", "S", "M", "M","M", "M", "M", "M", "M", "M", "L", "L", "XL", "XL", "XL", "XL", "XL", "M", "M", "M", "M", "M", "M", "M", "M", "M", "M", "L", "L", "XL", "XL", "XL", "XL", "XL" ]
}

print(ventas)
#Diseña un programa que lea el diccionario e indique el total de ventas,
# las tallas más vendidas y el total de tallas por ciudad.

ventaslista=list(ventas.values())
tallas_ciudad=[]
cont_T_S=0
cont_T_M=0
cont_T_L=0
cont_T_XL=0
cont_T_XXL=0

#contador camisetas por ciudad, 
for ciudad in ventaslista:
    cont_S=0
    cont_M=0
    cont_L=0
    cont_XL=0
    cont_XXL=0
    for venta in ciudad:
        if venta =="S":
            cont_S+=1
        elif venta =="M":
            cont_M+=1
        elif venta =="L":
            cont_L+=1
        elif venta =="XL":
            cont_XL+=1    
        elif venta =="XXL":
            cont_XXL+=1
    #Else fuera del ciclo, crea una nueva lista para cada ciudad con la cantidad de camisas x talla
    else:    
         lista_previa=[]
         lista_previa.append(cont_S)
         lista_previa.append(cont_M)
         lista_previa.append(cont_L)
         lista_previa.append(cont_XL)
         lista_previa.append(cont_XXL)
         tallas_ciudad.append(lista_previa)
         cont_T_S+=cont_S
         cont_T_M+=cont_M
         cont_T_L+=cont_L
         cont_T_XL+=cont_XL
         cont_T_XXL+=cont_XXL

total_camisetas= cont_T_S+cont_T_M+cont_T_L+cont_T_XL+cont_T_XXL
print(f"En total se vendieron: {total_camisetas} camisetas")
tota_ventas= (cont_T_S*2500)+(cont_T_M*3400)+(cont_T_L*5200)+(cont_T_XL*6000)+(cont_T_XXL*9000)
print(f"El total en ventas fue: ${tota_ventas}")

for i in range(len(tallas_ciudad)):
    if i==0:
        print("Cartagena:",end=" ")
        for j in range(len(tallas_ciudad[0])):
            if j==0:
                print (f"[S:{tallas_ciudad[0][j]}],",end=" ")
            elif j==1:
                print (f"[M:{tallas_ciudad[0][j]}],",end=" ")
            elif j==2:
                print (f"[L:{tallas_ciudad[0][j]}],",end=" ")
            elif j==3:
                print (f"[XL:{tallas_ciudad[0][j]}],",end=" ")
            elif j==4:
                print (f"[XXL:{tallas_ciudad[0][j]}]",end=" ")
        print()
    elif i==1:
        print("Baranquilla:",end=" ")
        for j in range(len(tallas_ciudad[1])):
            if j==0:
                print (f"[S:{tallas_ciudad[1][j]}],",end=" ")
            elif j==1:
                print (f"[M:{tallas_ciudad[1][j]}],",end=" ")
            elif j==2:
                print (f"[L:{tallas_ciudad[1][j]}],",end=" ")
            elif j==3:
                print (f"[XL:{tallas_ciudad[1][j]}],",end=" ")
            elif j==4:
                print (f"[XXL:{tallas_ciudad[0][j]}]",end=" ")
        print()
    elif i==2:
        print("Medellín:",end=" ")
        for j in range(len(tallas_ciudad[2])):
            if j==0:
                print (f"[S:{tallas_ciudad[2][j]}],",end=" ")
            elif j==1:
                print (f"[M:{tallas_ciudad[2][j]}],",end=" ")
            elif j==2:
                print (f"[L:{tallas_ciudad[2][j]}],",end=" ")
            elif j==3:
                print (f"[XL:{tallas_ciudad[2][j]}],",end=" ")
            elif j==4:
                print (f"[XXL:{tallas_ciudad[2][j]}]",end=" ")
        print()
    elif i==3:
        print("Bogotá:",end=" ")
        for j in range(len(tallas_ciudad[3])):
            if j==0:
                print (f"[S:{tallas_ciudad[3][j]}],",end=" ")
            elif j==1:
                print (f"[M:{tallas_ciudad[3][j]}],",end=" ")
            elif j==2:
                print (f"[L:{tallas_ciudad[3][j]}],",end=" ")
            elif j==3:
                print (f"[XL:{tallas_ciudad[3][j]}],",end=" ")
            elif j==4:
                print (f"[XXL:{tallas_ciudad[3][j]}]",end=" ")
        
        print()


print (f"Talla S: {cont_T_S}")
print (f"Talla M: {cont_T_M}")
print (f"Talla L: {cont_T_L}")
print (f"Talla XL: {cont_T_XL}")
print (f"Talla XXL: {cont_T_XXL}")
#ventas_s=(cont_S*2500)
#ventas_m=(cont_M*3400)
#ventas_l=(cont_L*5200)
#ventas_xl=(cont_XL*6000)
#venta_xxl=(cont_XXL*9000)
#print (f"""


#copiaaaaa
####
######
#################################
#########################################################


for ciudad,venta in ventas.items():
    cont_S=0
    cont_M=0
    cont_L=0
    cont_XL=0
    cont_XXL=0
 #   print (ciudad)
    if ciudad=="Cartagena":
        print ("Cartagena:",end=" ")
        for i in range(len(venta)):
            if ventas[ciudad][i]=="S":
                cont_S+=1
            elif ventas[ciudad][i]=="M":
                cont_M+=1
            elif ventas[ciudad][i]=="L":
                cont_L+=1
            elif ventas[ciudad][i]=="XL":
                cont_XL+=1
            elif ventas[ciudad][i]=="XXL":
                cont_XXL+=1
        print (f"[S:{cont_S}], [M:{cont_M}], [L:{cont_L}], [XL:{cont_XL}], [XXL:{cont_XXL}]")
    elif ciudad=="Barranquilla":
        print ("Barranquilla:",end=" ")
        for i in range(len(venta)):
            if ventas[ciudad][i]=="S":
                cont_S+=1
            elif ventas[ciudad][i]=="M":
                cont_M+=1
            elif ventas[ciudad][i]=="L":
                cont_L+=1
            elif ventas[ciudad][i]=="XL":
                cont_XL+=1
            elif ventas[ciudad][i]=="XXL":
                cont_XXL+=1
        print (f"[S:{cont_S}], [M:{cont_M}], [L:{cont_L}], [XL:{cont_XL}], [XXL:{cont_XXL}]")
    elif ciudad=="Medellín":
        print ("Medellín:",end=" ")
        for i in range(len(venta)):
            if ventas[ciudad][i]=="S":
                cont_S+=1
            elif ventas[ciudad][i]=="M":
                cont_M+=1
            elif ventas[ciudad][i]=="L":
                cont_L+=1
            elif ventas[ciudad][i]=="XL":
                cont_XL+=1
            elif ventas[ciudad][i]=="XXL":
                cont_XXL+=1
        print (f"[S:{cont_S}], [M:{cont_M}], [L:{cont_L}], [XL:{cont_XL}], [XXL:{cont_XXL}]")
    elif ciudad=="Bogotá":
        print ("Bogotá:",end=" ")
        for i in range(len(venta)):
            if ventas[ciudad][i]=="S":
                cont_S+=1
            elif ventas[ciudad][i]=="M":
                cont_M+=1
            elif ventas[ciudad][i]=="L":
                cont_L+=1
            elif ventas[ciudad][i]=="XL":
                cont_XL+=1
            elif ventas[ciudad][i]=="XXL":
                cont_XXL+=1
        print (f"[S:{cont_S}], [M:{cont_M}], [L:{cont_L}], [XL:{cont_XL}], [XXL:{cont_XXL}]")
    
            
            
