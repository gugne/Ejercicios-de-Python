
#Escriba un programa que para un grupo de n (el valor que usted desee mayor a 4) estudiantes, 
# almacene la nota y el código del estudiante en una matriz. 
# Código      Nota
# Estudiante 1      410            3.0
# Estudiante 2      350            2.5
# … ...
# … ...
# … ...
# Estudiante n      357          4.8

# Se requiere elaborar un programa que imprima las siguientes consideraciones:
# 1. Obtener la mayor nota y la menor nota (imprimir la nota y el código del estudiante que sacó la nota) 
# 2. Imprimir la nota promedio del curso

# ❖ Muy bien [ 4.0 ­ 5.0]
# ❖ Bien [ 3.0 ­ 4.0 )
# ❖ Suficiente [ 2.0 ­ 3.0 )
# ❖ Insuficiente [ 0,5 ­ 2.0 )






num= int(input("Inserte el número de estudiantes en la tabla:"))
table=[]
for i in range(num):
    print(f"Al estudiante le será asignado el código [{i+1}]")
    name= (input(f"Nombre del estudiante {i+1}:")).strip().title()
    #code= int (input(f"Inserte el código del estudiante {i+1}:"))
    flag=True
    while flag:
        grade= float (input(f"Nota del estudiante {i+1}:"))
        if grade<=5 and grade>=0.5:
            break
        else:
            print("La nota mínima es '0.5' y la nota máxima es '5.0'. El valor ingresado no es válido")
    new_list=[name,i+1,grade]
    table.append(new_list)
    print(new_list, "Será añadido a la lista")
print(table)

#mejor y peor nota:
best_grade=0
worst_grade=5

for i in range(num):
    for j,k,l in table:
        if best_grade<l:
            best_grade=l
            best_student=k
        if worst_grade>l:
            worst_grade=l
            worst_student=k
else:
    print(f"La mejor nota del ciclo fue {best_grade} del estudiante {best_student} y la peor nota del ciclo fue {worst_grade} del estudiante {worst_student} ")

acum=0
for i in range(num):
     acum+=table[i][2]
else:
    promedio=acum/num
    print(f"El acumulado del curso fue {promedio}") 

# 3. Teniendo en cuenta la definitiva, imprima el código y un mensaje de acuerdo con la nota:
good_job=[] #4-5
good_enough=[] #3-4
just_fine=[] #2-3
get_better=[] #0.5-2.0

for i in range(num):
    if table[i][2]>=4:
        good_job.append([table[i][1],table[i][2]])
    elif table[i][2]>=3 and table[i][2]<4:
        good_enough.append([table[i][1],table[i][2]])
    elif table[i][2]>=2 and table[i][2]<3:
        just_fine.append([table[i][1],table[i][2]])
    else:
        get_better.append([table[i][1],table[i][2]])
else:
# 7. Diga cuántos estudiantes quedaron en cada una de las categorías anteriores.
    if len(good_job)>0:         
        print ("Lo hicieron muy bien:")
        print (good_job)
        print (f"{len(good_job)} estudiantes lo hicieron MUY BIEN!!!")
    if len(good_enough)>0:
        print ("Lo hicieron bien:")
        print (good_enough)
        print (f"{len(good_enough)} estudiantes lo hicieron BIEN!!!")
    if len(just_fine)>0:
        print ("Lo lograron pero pueden hacerlo aún mejor:")
        print (just_fine)
        print (f"{len(just_fine)} estudiantes lo lograron pero pueden mejorar!!!")
    if len(get_better)>0:
        print ("Deben mejorar para aprobar: ")
        print (get_better)
        print (f"{len(get_better)} estudiantes deben mejorar para aprobar!!!")

# 4. Cuántos estudiantes aprobaron y cuántos reprobaron       
approved=[]
reprove=[]

for i in range(num):
    if table[i][2]>=2:
        approved.append([table[i][1],table[i][2]])
    else:
        reprove.append([table[i][1],table[i][2]])
else:
    print(f"El total de estudiante aprobados es: {len(approved)}")
    print(f"Reprobaron un total de: {len(reprove)}")
# 5. Cuál fue el porcentaje de estudiantes aprobados y reprobados.
    aprobados=(len(approved)*100)/num
    reprobados=(len(reprove)*100)/num
    print(f"El porcentaje de estudiante que aprobaron fue:{aprobados}%")
    print(f"El porcentaje de estudiante que reprobaron fue:{reprobados}%")


# 6. Estudiantes que aprobaron y reprobaron (imprimir los códigos)
print("Los estudiante que aprobaron organizados por código, fueron:")
for i in range(len(approved)):
    print("Estudiante", end=" ")
    print (approved[i][0])
    
print("Los estudiante que reprobaron organizados por código, fueron:")
for i in range(len(reprove)):
    print("Estudiante", end=" ")
    print (reprove[i][0])

