a=int(input("Cuantitat:		 "))
b=int(input("Preu:			 "))
c=int(input("IVA:			 "))


preu=a*b
iva=c/100*preu


print()
print("IVA (21%):		",iva,"€")
print()
print("Total=			",preu+iva,"€")