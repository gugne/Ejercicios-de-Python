from math import sqrt

def funciónCuadrática(a,b,c):
    d=(b**2)-(4*a*c)
    
    if (b*b)<(4*a*c):
        print ("La ecuación no tiene soluciones reales")
    
    elif d>0:
        solution1=(-b+ sqrt(d))/(2*a)
        solution2=(-b- sqrt(d))/(2*a)
        print (solution1)
        print (solution2)
    else:
        solution1=(-b+ sqrt(d))/(2*a)
        solution2=(-b- sqrt(d))/(2*a)
        print (solution2)
        #print ("La ecuación no tiene soluciones reales")
            
    #elif (b*b)<(4*a*c):
        
    #elif (b*b)==(4*a*c):     
        #print (solution1)
        #print (solution2)
    #elif (b*b)>(4*a*c):
        #print (solution1)
        #print (solution2)
   
a= int(input("Valor de a:"))
b= int(input("Valor de b:"))
c= int(input("Valor de c:"))

funciónCuadrática(a,b,c)


