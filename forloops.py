#1. Realice un programa que enumere los paises de la siguiente lista

countries= ['Canada', 'USA', 'Mexico', 'Australia']
size=len(countries)
print(size)
for i in range(len(countries)):
  print(i+1, countries[i])

#2. Crear un ciclo for que cuente de 0 a 100

for i in range(101):
  print(i)

#3. Haz una tabla de multiplicar utilizando el ciclo for
table_of=int(input("tabla del: "))
count=0
for i in range(11):
  result=i*table_of
  print(f"{table_of}*{i}={result}")

#4.Imprima los números del 1 a 10 al revés utilizando el ciclo for

for i in reversed(range(1,11,1)):
  print (i)

#5.Crear un bucle que cuente todos los números pares hasta el 100

for i in range(2,101,2):
  print(i)

#6.Cree un bucle que sume los números del 100 al 200

n=0
for i in range(100,201,1):
  n+=i
  print(n)

#7.Dado un número, cuente el número total de dígitos de un número Por ejemplo, el número es 75869, por lo que la salida debería ser 5.

c=0
num=(input("Digite un número:"))
size=len(num)
for i in range(size):
  c+=1
print(f"El número tiene: {c} dígitos")


#8.Mostrar series de Fibonacci hasta 10 términos - Fibonacci con Python

a=0
b=1
print(a)
for i in range(9):
  print(b)
  c=a+b
  a=b
  b=c

#las tablas de multiplicar desde las del 1 hasta la del 10

for i in range(0,11):
    print(f"Tabla del {i}")
    print()
    for j in range(0,11):
        mult=i*j
        print(f"""{i}*{j}= {mult}
              """)

#Use un bucle para mostrar elementos de una lista dada que estén presentes en posiciones pares

list=["a","b","c","d","e","f","g","h","i","j","k"]
size=len(list)
for i in range(size):
  if i%2==0:
    print(list[i])
  else:
    continue

#imprima el siguiente patrón en un ciclo for: 
#*
#**
#***
#****
#*****
#****
#***
#**
#*

c="*"
for i in range(6):
  print(c*i)
  if c*i=="*****":
    for j in reversed(range(5)):
      print (c*j)

#v2 con lo aprendido de end= en input (aunque lo hice más fácil con mi método que me salió de una)

rows=5
symbol="*"
for i in range(0,rows):
  for j in range(0,i+1):
    print(symbol, end="")
  print()
for i in range(rows,0,-1):
  for j in range(0,i-1):
    print(symbol, end="")
  print()

#imprima el siguiente patrón en un ciclo for: 54321,4321,321,21,1,****,***,**,*
#54321
#4321
#321
#1
for i in reversed(range(1,6)):
  print(i,i-1,i-2,i-3,i-4)
  for i in reversed(range(1,6)):
    print(i-1,i-2,i-3,i-4)
    for i in reversed(range(1,6)):
      print(i-2,i-3,i-4)
      for i in reversed(range(1,6)):
        a=0
        print(i-3,i-4)
        if a==0:
          print(i-4)
        break
      break
    break
  break

#v2 mirando como se hacía bien
rows=5
for i in range(0,rows):
  for j in range(rows-i,0,-1):
    print(j,end=" ")
  print()

#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5
rows=5
for i in range(1,rows+1):
  for j in range(1,i+1):
    print(j,end=" ")
  print()

#Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

number=int(input("Write a number: "))
a=0
for i in range(1,number+1,1):
  a+=i
  print(a)

#Write a program to display only those numbers from a list that satisfy the following conditions

#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop
#numbers = [12, 75, 150, 180, 145, 525, 50]

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
  if i>500:
    break  
  elif i>150:
    continue
  elif i%5==0:
    print (i)


#Display numbers from -10 to -1 using for loop

for i in range(-10,0,1):
  print(i)

#Use else block to display a message “Done” after successful execution of for loop
number= int(input("Inserte un número: "))
for i in range(1,number+1,1):
    print(i)
else:
    print("done")

#Write a program to display all prime numbers within a range

start=int(input("Inserte un número inicial: "))
end=int(input("Inserte un número final: "))
for num in range(start,end+1):
  if num>1:
    for i in range(2,num):
      if num%i==0:
        break
    else:#Este el esta en el for, no en el if
      print(num)

#Write a program to use the loop to find the factorial of a given number.

#The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.ej 5=5x4x3x2x1

n=int(input("Ingrese un número: "))
f=1
for i in range(1,n+1):
  f=f*i

print(f)

#Calculate the cube of all numbers from 1 to a given number
#Write a program to rint the cube of all numbers from 1 to a given number

n=int(input("Ingrese un número: "))
for i in range(1,n+1):
  print(f"número actual {i} y su potencia al cubo es {i*i*i}")

#Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

series = int(input("Ingrese un número de series: "))
num = int(input("Ingrese un número: "))
static=num
sum_seq = 0
for i in range(0, series):
  #print(num, end="+")#2+,22+,222+,+2222,+22222
  sum_seq += num #2,2+22=24,24+222=246,2468,24690,
  num = num * 10 + static#22,222,2222,22222

print()
print("La suma es", sum_seq)

#P
#Py
#Pyt
#Pyth
#Pytho
#Python

word="Python"
size=len(word)
for i in range(0,size):
  for j in range(0,i+1):
    print(word[j],end="")
  print()
for i in range(size, 0,-1):
  for j in range(0,i-1):
    print(word[j], end="")
  print()