w1 = "Hello World"
w2 = "hEllo orlDw"

# Clear formatting and put all letters in lower case
specialChars = "!#$%^&*(),.-/ ?:"
for specialChar in specialChars:
    w1 = w1.replace(specialChar, '')
    w2 = w2.replace(specialChar, '')
w1 = list(w1.lower())
w2 = list(w2.lower())

a = []

if len(w1) == len(w2):
    for letter1 in w1:
        if letter1 in w2:
            b = list(w2.pop(w2.index(letter1)))
            a.append(b)
        else:
            print("letter not in w2")
            break
    if len(a) == len(w1):
        print("letters complete")

else:
    print("word length not equal")