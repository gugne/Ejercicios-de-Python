t=["hola",1,3,4,5,"hello",6,7,8]
str_=[]
int_=[]
float_=[]
for i in t:
  if isinstance(i, str):
    str_.append(i)  
  elif i%1==0:
    int_.append(i)
  else:
    float_.append(i)
    

print(int_)
print(float_)
print(str_)

#Escribe el código un ciclo para obtener el número de dígitos de un número ingresado por el usuario, pero saltarse si el digito es 4.

n=input("Ingrese un número para saber cuántos dígitos tiene: ")
counter=0

for i in n:
  if i=="4":
    continue
  else:
    counter+=1
print(f"el número tiene:{counter} digitos" )

#Diseñar un algoritmo quecalcule el promedio de notas del primer parcial de un curso de N estudiantes

stud= int(input("Ingrese el número de estudiantes:"))
cont=0
suma=0
notas=[]
for i in range(stud):
  nota=float(input(f"Inserte la nota del estudiante {i+1}:"))
  notas.append(nota)
  suma+=nota
  

print("Las notas fueron:", notas)
print("El promedio de notas es:")
print(suma//stud)

#Escribe el código usando break que reciba una palabra e imprima el número de letras que tiene y las letras hasta que, o bien termine la palabra o encuentre la letra a.

word= input("Ingrese una palabra: ")
size=len(word)
count=0
for i in range(size):
  if word[i]!="a":
    count+=1
    print(word[i])
  else:
    print(f"Letras totales: {size}")
    break

print(f"Letras hasta la a: {count}")

#fibonacci

  
a=0
b=1
print(a)
for i in range(15):
  print(b)
  z=a+b
  a=b
  b=z

#Escribe un algoritmo que lea 10 números e imprima cuantos son positivos, cuantos negativos y cuantos neutros(0).
neg=[]
pos=[]
cont_=0
cont_2=0
cont_0=0
print("Ingrese 10 números")
for i in range(5):
  n=int(input(f"Número {i+1} de 10: "))
  if n<0:
    neg.append(n)
    cont_+=1
  elif n==0:
    cont_0+=1    
  else:
    pos.append(n)
    cont_2+=1
  
print(f"los números negativos son: {neg}")
print (f"El total de negativos es: {cont_}")
print(f"los números positivos son: {pos}")
print (f"El total de positivos es: {cont_2}")

print (f"El total de ceros es: {cont_0}")

#pares de 1 a 10
evensto10=[]
for i in range(2,11,2):
  print(i)
  evensto10.append(i)
print(evensto10)

#sumar elementos de la lista  
Lista = [2, 3, 4, 21, 45, 76, 54, 12, 34, 67]
total=0
for i in Lista:
    total+=i
print (total)

#Escribamos un programa que le permita al usuario ingresar una lista de 6 números aleatorios entre 1 y 20 en Python, y determinar:
#El número mayor de una lista x
#Los # primos de la lista son
print("Ingrese 6 número del 1 al 20.")
flag=True
cont=1
list=[]
while flag:
  n=int(input(f"Ingrese su número{cont}: "))
  if cont==6:
    if n>=1 and n<=20:
      list.append(n)
      break
    else:
      print ("Uppps! sólo números del 1-20")  
  elif n<=20:
    list.append(n)
    cont+=1
  else:
    print ("Uppps! sólo números del 1-20")
    continue

print (list)
size=len(list)
mayor=0
a=0
primos=[]
for i in range (size):
  if mayor<list[i]:
    a=list[i]
    mayor=a
for i in range(size):
  if list[i]>1:
    for j in range(2,list[i]):
      if list[i]%j==0:
        break
      else:
        primos.append(list[i])
        break
  else:
    continue


  #for j in range(size):
print(f"Los número primos de tu lista son: {primos}")    
print(f"número mayor:{mayor}")

#Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en 
# una tupla y la muestre por pantalla el mensaje Yo estudio <asignatura>,
# donde <asignatura> es cada una de las asignaturas de la tupla.


course= ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
thistuple=tuple(course)
#size=len
for i in thistuple:
    print(f"Yo estudio {i}")


    
#Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una tupla, 
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la
# tupla las asignaturas aprobadas. Al final el programa debe mostrar por 
# pantalla las asignaturas que el usuario tiene que repetir.

thistuple=("Matemáticas", "Física", "Química", "Historia", "Lengua")
courses= list(thistuple)
contador=0
size= len(courses)
for i in range (size):
    print(i)
    grade=int(input(f"¿Cuál fue su calificación en {courses[i-contador]} [Notas 1/5]: "))
    if grade>=3:
        courses.remove(courses[i-contador])
        contador+=1
else:
    thistuple=tuple(courses)
    print("Debes repetir las siguientes asignaturas: ")
    print(thistuple)
    