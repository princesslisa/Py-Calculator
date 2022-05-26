# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


# Question
# 2. Open “main.py”, and complete the function “read_file_content”.
# It should accept a filename as an argument and read the text contained in that file. It should return a string.
#
# 3.  Complete the function “count_words”. It uses “read_file_content” to read the text contained in “story.txt”.
# It should return a dictionary whose keys are unique words, and their values the count of those words in the text
# e.g {“as”:10, “would”:5}.

def read_file_content(filename):
    with open(filename) as file:
        content = file.read()
    return content


def count_words():
    text = read_file_content("./story.txt")

    # Cleaning text
    text = text.lower()
    specialchars = '.,?!()[]/'
    for specialChar in specialchars:
        text = text.replace(specialChar, "")
    text = text.replace('\n', '')

    # Create dictionary keys and find unique words
    keys = set(text.split(" "))
    mydict = {}
    for i in keys:
        mydict[i] = text.count(i)

    return mydict


print(count_words())
