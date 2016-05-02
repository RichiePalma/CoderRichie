text = str(input("Submit what you want to write: "))
#String to write on file
file = open("Test2.txt","w")
#Open file as write
file.write(text)
#Write over the file the value of text
file.close()
#Close file after that
