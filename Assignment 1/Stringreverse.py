def stringReverse(a):
    rev = ""
    for x in range(len(a)-1,-1,-1):
        rev += a[x]
    return rev

print(stringReverse(input("Enter a sentence: ")))