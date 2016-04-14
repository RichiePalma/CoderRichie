namefile = input("Please submit the document name: ")
word = input("What word are you looking for: ").lower()
# Inputs for the user
lower_case_word = word.lower()
#So lower or capital letters does not matter when searching the word.

def Counter(lower_case_word, namefile):
    counter = 0
    with open(namefile) as openfile: #open the file and keep it open
        for line in openfile:
            line = line.lower()
            counter += line.count(lower_case_word)
        return(counter)

print("The total amount of " + str(word) + " in text " + str(namefile) + " is: " + str(Counter(lower_case_word, namefile)))
