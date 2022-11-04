

print("Super Tienda  tu Vecino")
print ("Factura   de  Venta")
print("codigo producto 1")
codigo1 = input()
print("primer producto")
precio1 = input()
print("cantidad comprada de ",precio1)
precio1_cantidad = int(input())
print("valor unitario de",precio1,"sin iva")
precio1_vu = int(input())

print("codigo producto 2")
codigo2 = input()
print("segundo producto ")
precio2=input()
print("cantidad comprada de ",precio2)
precio2_cantidad = int(input())
print("valor unitario de ",precio2,"sin iva" )
precio2_vu = int(input())


print("codigo producto 3")
codigo3 = input()
print("tercer producto ")
precio3=input()
print("cantidad comprada de ",precio3)
precio3_cantidad =int(input())
print("valor unitario de",precio3,"sin iva")
precio3_vu = int(input())



precio1_st = precio1_cantidad*precio1_vu
precio2_st = precio2_cantidad*precio2_vu
precio3_st = precio3_cantidad*precio3_vu

sub_total =precio1_st +precio2_st +precio3_st
IVA =sub_total * 0.19
Total = sub_total + IVA

print("El total de",precio1,"es:",precio1_st)
print("El total de",precio2,"es:",precio2_st)
print("El total de",precio3,"es:",precio3_st)

print("sub total es:",sub_total)
print("el iva es de ",IVA)
print("total a pagar con iva",Total)








