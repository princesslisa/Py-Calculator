# Question

# Open “main.py”, and complete the function “find_anagrams”.
# It should accept two strings, and determine if they are anagrams.
# Your function should return True  if they are anagrams, else  False.

def find_anagrams(w1, w2):
    # Clear formatting and put all letters in lower case for easy comparison
    specialchars = "!#$%^&*(),.-/ ?:"
    for specialchar in specialchars:
        w1 = w1.replace(specialchar, '')
        w2 = w2.replace(specialchar, '')
    w1 = list(w1.lower())
    w2 = list(w2.lower())

    # Create an empty list
    a = []

    # Compare the length of the first word and second word
    if len(w1) == len(w2):
        for letter in w1:
            if letter in w2:
                b = list(w2.pop(w2.index(letter))) # Creating a list of the popped out letter of w2
                a.append(b) # Appending that letter to list a
            else:
                return False

        # Comparing length of the new list a to the list of the first word
        if len(a) == len(w1):
            return True

    else:
        return False

x = input('Enter first word: ')
y = input('Enter second word: ')

print(find_anagrams(x, y))