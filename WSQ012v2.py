#There is no v1 becuase that one did not worked.
namefile = input("Please submit the document name: ") #Doc this case is test.txt
word = input("What word are you looking for: ")

file_object = open(namefile , 'r') #Open file as read
readfile = file_object.read() #To actually read the file

def Counter(word, namefile):
    wordcount = 0
    with open(namefile) as openfile:
        for line in openfile:
            for part in line.split():
                if word in part:
                    wordcount +=1
        return wordcount

print("This is the amount of times of such word: ", Counter(word, namefile))
print("This is what your document says: ", readfile) #Just to test that it is reading
#This finally opens!
