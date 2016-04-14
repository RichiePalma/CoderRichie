print("Let's do math again")
x = int(input("Please give me the first interger number: "))
y = int(input("Provide me the second interger number, please: "))
#This is basically WSQ03 but with fancier look
def operation(x,y):
	z = x + y
	return (z)
	#z as the result because, why not?
def operation2(x,y):
	z = x - y
	return (z)
def operation3(x,y):
	z = x * y
	return (z)
def operation4(x,y):
	z = x / y
	return (z)
def operation5(x,y):
	z = x % y
	return (z)
#The only difference is that we had to separate the operations from the printing of the actual results. 
#I do not now why neither do not worry. 
print("Suma: ", operation(x , y))
print ("Resta: ", operation2(x , y))
print ("Multiplicación: ", operation3(x , y))
print ("División: ", operation4(x , y))
print ("Sobrante: ", operation5(x , y))
