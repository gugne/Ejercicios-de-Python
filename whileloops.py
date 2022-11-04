#Escriba un programa que pregunte una y otra vez si desea continuar con el programa, siempre que se conteste exactamente sí (en minúsculas y con tilde).

flag=True
while flag:
  run_p=input("¿Desea continuar ejecutando el programa?[sí/no]: ").lower()
  if run_p=="sí" or run_p=="si":
    continue
  else:
    print("Hasta luego :)")
    break
    
#Escriba un programa que pregunte una y otra vez si desea terminar el programa, salvo si se contesta exactamente SI (en mayúsculas y sin tilde).
flag=True
while flag:
  run_p=input("¿Desea terminar el programa?: ")
  if run_p=="SI":
    print("Hasta luego :)")
    break
  else:
    continue

#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan.

flag=True
while flag:
  passw=input("Ingrese su contraseña: ")
  passw_c=input("Repita su contraseña: ")
  if passw_c==passw:
    print("Su cuenta ha sido creada")
    break
  else:
    print("Las contraseñas no coinciden, intente nuevamente")
    continue
    
#Escriba un programa que simule una hucha. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa no comprobará que las cantidades sean positivas.

flag=True
w_save=int(input("¿Cuánto desea ahorrar?: "))
saved=0
while flag:
  money=int(input("¿Cuánto va a depositar ahora?"))
  saved+=money
  if w_save<=saved:
    print(f"""Haz ahorrado lo suficiente:
          
          Tu meta era: {w_save}
          Ahorraste: {saved}
         """)
    break
  else:
    continue
    #Tambien se puede cortar con -flag=False.

#Escriba un programa que mejore la simulación de la hucha del ejercicio anterior, no permitiendo que se escriban cantidades negativas.

flag=True
w_save=int(input("¿Cuánto desea ahorrar?: "))
saved=0
while flag:
  money=int(input("¿Cuánto va a depositar ahora?"))
  saved+=money
  if money<0:
    print("No se pueden ingresar números negativos")
    saved-=money
  elif w_save<=saved:
    print(f"""Haz ahorrado lo suficiente:
          
          Tu meta era: {w_save}
          Ahorraste: {saved}
         """)
    break
  else:
    continue

#VERSIÓN 2

flag=True
saved=0
piggy=int(input("Cuánto deseas ahorrar?: "))
while flag:
  if piggy>saved:
    save=int(input("Cuánto deseas ingresar ahora?: "))
    if save<0:
      print("Sólo se pueden ingresar valores positivos")
    else:
      saved+=save
  else:
    print(f"Haz ahorrado {saved}")
    flag=False

#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.

count=0
passw=input("Ingrese su contraseña:")
print("Tiene 3 intentos de confirmación antes de que su cuenta sea bloqueada")
while count<3:
  passw_c=input("Confirme su contraseña: ")
  if passw!=passw_c:
    count+=1
    print(f"Ups... las contraseñas no coinciden, intentos restantes: {3-count} ")
    if count==3:
      print(">>>Se ha bloqueado su cuenta tras 3 intentos fallidos<<<")
      break
  else:
    print("Felicidades cuenta creada")
    break
    

#Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres peticiones.

count=0
passw=input("Ingrese su contraseña:")
print("Tiene 3 intentos de confirmación antes de que su cuenta sea bloqueada")
while count<3:
  passw_c=input("Confirme su contraseña: ")
  if passw!=passw_c:
    count+=1
    print(f"Ups... las contraseñas no coinciden, intentos restantes: {3-count} ")
    if count==3:
      print(">>>Se ha bloqueado su cuenta tras 3 intentos fallidos<<<")
      break
  else:
    print("Felicidades cuenta creada")
    break