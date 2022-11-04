n= int(input("Digite un número: "))
c=0 #contador
while n>0: #cuando el número sea meyor al cero hará:
  c+=1 #suma 1 al contador ej: 100>0 c=0 +1 =1
  n=n//10 #divide el núero en 10 ej: 100/10=10
  #n(10)>0 -entonces-> c=(1)+1=2 --> n= [10/10] =1
  #continua el ciclo c=(2)+1=3 n= (1)/10 = 0,1

  #retorna al while y compara otra vez int(0,1)= Como tenemos el int en el input lo trae a 0.0 y 0 no es MAYOR QUE CERO entonces para el ciclo 
if c==4:#en el ejemplo c para este momento será 3==4: false, se salta el if.
    print("su número es 4")
else: #tres es diferente de 4 entonces va a imprimir el else
    print("El número de dígitos es:",c)


t= (1, 2,"hola",3.3,"hello",5,4.3)
int_=[]
float_=[]
str_=[]

while flag:
  print("Bienvenido al menú:")
  print("""
       
       1.Consignar
       2.Retirar.
       3.Ver saldo
       4.Abonar Intereses.
       5.Salir
       """)
  flag=int(input("Ingresa un número para el menú al que deseas entrar [1/5]:"))
  if flag ==1:
    print ("Algo ha salido mal, lo sentimos")
    print ("... ")
    print ("... ")
    print ("... ")
    print ("Regrasando al menú inicial...")
    print ("... ")
    print ("... ")
    print ("... ")
  elif flag==2:
    print ("Algo ha salido mal, lo sentimos")
    print ("... ")
    print ("... ")
    print ("... ")
    print ("Regrasando al menú inicial...")
    print ("... ")
    print ("... ")
    print ("... ")
  elif flag==3:
    print ("Algo ha salido mal, lo sentimos")
    print ("... ")
    print ("... ")
    print ("... ")
    print ("Regrasando al menú inicial...")
    print ("... ")
    print ("... ")
    print ("... ")
  elif flag==4:
    print ("Algo ha salido mal, lo sentimos")
    print ("... ")
    print ("... ")
    print ("... ")
    print ("Regrasando al menú inicial...")
    print ("... ")
    print ("... ")
    print ("... ")
  elif flag==5:
    print ("Abandonando la aplicación")
    break
  else:
    print("Opción no válida.")
    print ("... ")
    print ("... ")
    print ("... ")
    print ("Regrasando al menú inicial...")
    print ("... ")
    print ("... ")
    print ("... ")

