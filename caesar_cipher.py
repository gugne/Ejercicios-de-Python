
ABC=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",]

code=int(input("Inserte un número de cifrado: "))
if code>=27:
    code=code-27
codeme= input("Escriba lo que desea codificar:").upper()
codelist= list(codeme)

for i in codelist:    
    if i not in ABC:
        print(i,end="")   
    else:
        index=ABC.index(i)
        new_index=index+code
        if new_index>26:
            giro=0+(new_index-27)
            print(ABC[giro],end="")
        else:
            index=ABC.index(i)
            print(ABC[new_index],end="")
print()
#decode=int(input("Inserte un número de cifrado: "))
#decodeme= input("Escriba lo que desea des-codificar:").upper()

decode=int(input("Inserte un número de de-cifrado: "))
if decode>=27:
    decode=decode-27
decodeme= input("Escriba lo que desea de-codificar:").upper()
decodelist= list(decodeme)

for i in decodelist:    
    if i not in ABC:
        print(i,end="")   
    else:
        index=ABC.index(i)
        new_index=index-decode
        if new_index<0:
            giro_neg=0+(new_index+27)
            print(ABC[giro_neg],end="")
        else:
            index=ABC.index(i)
            print(ABC[new_index],end="")
