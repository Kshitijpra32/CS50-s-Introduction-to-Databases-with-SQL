Input = input("Input:")
result = " "

for i in Input:
    if i.lower() not in ['a' , 'e' , 'i' , 'o' ,'u']:
        result += i

print(result)
