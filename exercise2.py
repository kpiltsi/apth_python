year = int(input("Εισάγετε έτος: "))
disekto = False

if year % 400 == 0:
    disekto = True
if year % 4 == 0:
    if year % 100 != 0:
        disekto = True

print(disekto)
