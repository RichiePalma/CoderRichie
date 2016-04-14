print("Now it is turn to make a sum of numbers!")
print ("Give me the range, in intergers, please.")
x = int(input("From:"))
y = int(input("To:"))
#But what if the user makes a mistake and submits "x" bigger or equal than "y"?

if (x>y):
	print("Remember that 'From' needs to be smaller than 'To'")	
elif (x==y):
	print("Your result is:", operation(x , y))
else:
		incl = 0
		for n in range(x,y+1):
			incl= incl + n
			
		print ("Your result is:", incl)
