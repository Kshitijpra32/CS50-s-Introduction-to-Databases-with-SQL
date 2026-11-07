Amount_due = 50


while Amount_due > 0:
    Input = int(input("Insert coin:"))

    if Input in [5 , 10 ,25]:
        Amount_due -= Input
        print("Amount due:", Amount_due)

change = abs(Amount_due)
print("Change Owed:", change)
