def numToText(number):
    digit = {
        "0":'zero',
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":'six',
        "7":'seven',
        "8":'eight',
        "9":"nine"
    }
    show = ""
    for x in number:
        show += digit[x] + " "
    print(show)

y = input("Enter a number: ")
numToText(y)