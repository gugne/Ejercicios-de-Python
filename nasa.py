dic={
    "Hernandez": [2.3, 4.3, 9],

    "Andrade": [8.7, 7.6, 10],

    "Castro": [9.2, 8.6, 9.7],

    "Contreras": [1.2, 3.2, 5.6],

    "Diaz": [9.8, 8.8, 8.2],

    "Benitez": [1.2, 9.8, 10],

    "Mendoza": [7.6, 7.9, 7.6]

}
expelled=[]
final=[]
approved=[]
for key in dic:
    sum=0
    print(key)
    for values in dic[key]:
        sum+=values
        print(sum)
    else:
        prom=sum/len(dic[key])
        print (f"el promedio de {key}, es: {prom}")
        if prom<5:
            expelled.append(key)
        elif prom>5 and prom<=7:
            final.append(key)
        else:
            approved.append(key)

print("Han sido descalificado los siguientes participantes:")
print(expelled)
print("Han pasado para la última prueba los siguientes participantes:")
print(final)
print("Debido a su buen puntaje, han sido admitidos directamente los siguientes participantes:")
print(approved)
            
            
            
            
