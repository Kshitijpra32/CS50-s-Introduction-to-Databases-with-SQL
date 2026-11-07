camel = input("Enter a text :")
result = " "

for c in camel:
    if c.isupper():
        result += "_" + c.lower()
    else:
        result += c


print(result)
