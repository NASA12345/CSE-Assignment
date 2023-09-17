def Multiplication(x,y):
    i = 0
    prod = 0
    while i < y:
        prod += x
        i += 1
    return prod

a = int(input("Enter the number to be multiplied: "))
b = int(input("Enter the multiplier: "))
print(Multiplication(a,b))
