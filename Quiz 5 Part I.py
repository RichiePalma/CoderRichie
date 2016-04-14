print("Want to known if a word is a palindrome?")

def ignorespaces(s):
	words = s.replace(" ", "") #To ignor spaces becuase there are palindrome with spaces
	return words

s = str(ignorespaces(input("What is the word?: ")))

s1 = s[::-1] #[] Means position for example s = racecar then print(s[3]) it is going to prin the letter e or you can also do range [0:4] to print 'race'
#print(s[0: : 2]) it will print each two letters than means r c c r
#print(s[-1]) prints the last letter, -2 for the 'penultima'

print("The word reversed is: ", s1)
#.join
if s.lower() == s1.lower(): #.lower() to ignor capital letters
	print ("Yes, it is a palindrome")
else:
	print ("No, it is not a palindrome.")
