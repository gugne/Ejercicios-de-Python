mail=input("Ingrese su correo electrónico: ").strip()
user=mail[0:mail.index("@")]
domain=mail[mail.index("@")+1::1]
print (f"Su usuario es: {user}")
print (f"Su dominio es: {domain}")