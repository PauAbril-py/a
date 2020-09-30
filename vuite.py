# vendes
cv = int(input("Vendes de cola:			"))
tv = int(input("Vendes de taronja:		"))
lv = int(input("Vendes de llimona:		"))

print()

# preu
cp = int(input("Preu de cola:			"))
tp = int(input("Preu de taronja:		"))
lp = int(input("Preu de llimona:		"))

print()

# total
# ct=int(input(""))
# tt=int(input(""))
# lt=int(input(""))

print()

# informe de ventes
print("---------------------------------------------------------------------")
print()
print("Producte		Vendes		Preu		Total")
print()
print("---------------------------------------------------------------------")
print()
print("Cola			", cv, "		", cp, "		", cv * cp)
print()
print("Taronja			", tv, "		", tp, "		", tv * tp)
print()
print("Llimona			", lv, "		", lp, "		", lv * lp)
print()
print("---------------------------------------------------------------------")
print()
print("Total:	", cv * cp + tv * tp + lv * lp)
