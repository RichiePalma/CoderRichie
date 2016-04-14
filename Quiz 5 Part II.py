def divisible(x):
	siloes = []
	for i in x:
		if i % 3 == 0:
			siloes.append(i)
	return (siloes)
	
def suma(x):
	return (sum(divisible(x)))
	
print("Time to sum a series of numbers divisible by 3!")
x = []

for i in range (8):
	num = input("Please submit an interger number: ")
	x.append(int(num)) #Int since Python 3 always consideres a regular input as string.
	
print ("The numbers divisible by 3 of your list of numbers are: ", divisible(x))
print ("The sum of those numbers is: ", suma(x))
