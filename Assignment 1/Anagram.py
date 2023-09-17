def anagram(x,y):

    str1 = sorted("".join(tuple(x.split())))
    str2 = sorted("".join(tuple(y.split())))
    
    if str1 == str2:
        return True
    else:
        return False

a = input("Enter a string: ")
b = input("Enter an anagram: ")

print(anagram(a,b))