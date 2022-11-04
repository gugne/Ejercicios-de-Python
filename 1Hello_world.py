import math
#list1=[[1,2,3],[4,5,6],[7,8,9]]
#print(list1[2][1])
#print(list(str(1111)))
#list1=list1+list(str(1111))
#list1.append([2,2])
#print(list1)

#dic2=dict(zip("abcd",list((1,2,3,4,5))))
#print(dic2)


#Hacer un programa en PYTHON que permita al usuario elegir calcular el área 
# de figuras geométricas como: circulo, cuadrado, rectángulo, triángulo.

    

#a,b,c=1,2,3
#print(a)

#d,e,f=[4,5,6]

#print(type(e))

#g,h,i="oee"
#print(i)

#contacts={
    #"Mi número": 1113253232,
    #"Bernardo Gomez": 3059203588,
    #"Alexandra":3204155894,
    #"Innovacion Digital":3004798801,
    #"Angie Vitola":3006443301,
    #"Pao":3007248438,
    #"Andres": 3203444309,
    #"Eloisa": 3203703531,
    #"Mateo Vasquez": 3053404417,
    #"Sara Acevedo": 11111111,
    #"Sara Angostura": 2222222,
    #"Sara Suarez": 333333333,
#}

#mylist=list(contacts.values())
#print (mylist)



#for i in range (5):
    #for j,k in total_talla:
        #if k>mas_vendido:
            #mas_vendido=k
            #talla_mv=j
            #print(mas_vendido)
        #mas_vendido=total_talla[i][0]
        #print (mas_vendido)
    #if int(j)>=mas_vendido:
        #mas_vendido=i
    #if j<=menos_vendido:
        #menos_vendido=i

#Que tal este que imprima todas la tablas de multiplicar desde las del 1 hasta la del 10

def suma(*nums):
    total=0
    for num in nums:
        total+=num
    return total

print(suma(1,2,3,4,5,6,7,8,9,10))


for i in range(0,11):
    print(f"Tabla del {i}")
    print()
    for j in range(0,11):
        mult=i*j
        print(f"""{i}*{j}= {mult}
              """)
