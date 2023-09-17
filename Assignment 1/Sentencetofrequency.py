def sentencetofrequency(x):
    letters = sorted("".join((x.split())))
    cnt = dict.fromkeys(letters)
    for x in cnt.keys():
        count = 0
        for y in letters:
            if y == x:
                count +=1
            cnt[x] = count
    print(f"The count of each letter in the sentence is {cnt}.")

sentencetofrequency(input("Enter a sentence: "))