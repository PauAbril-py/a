a=int(input("Cuantitat:		 "))
b=int(input("Preu:			 "))
c=a*b
iva=21/100*c
print()
print("IVA (21%):		",iva,"€")
print()
print("Total=			",c+iva,"€")