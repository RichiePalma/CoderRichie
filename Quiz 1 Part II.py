print("Lets do some math!")
x = input("Give me the first number:")
y = input("Give me the second number:")
def operation (x,y):
	return("Multiplicacion", int(x) * int(y))
print (operation (x , y))
def operation2 (x,y):
	return("Division", int(int(x) / int(y)))
print (operation2 (x,y))
def operation3 (x,y):
	return("Sobrante", int(x) % int(y))
print (operation3 (x , y))
