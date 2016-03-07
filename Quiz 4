def fact(x):
	r = 1
	for i in range (1,x+1): #Factorial 
		r = r*i
	return (r)
	
def calc_euler(prec): #prec is later defined by me at the end
	# calculate sum of 1/n! from 0 to infinity
	# stop when the difference between latest calc and previous is less than prec
	n = 0 
	prev = 100 #Big number either way it is going to become absolute at diff = 
	e = 0
	diff = abs(e - prev)
	print("diff is",diff)
	while (diff > prec):
		prev = e
		e = e + 1.0/fact(n) #The division and the addition to enter a loop.
		n = n + 1 #How many times it is going to be a factorial to meet the conditions. 
		diff = abs(e - prev)
		print("n is: ", n,"e is: ",e)
	return e
	
# Main program	
number = calc_euler(0.000000000000000000000000000000000000000000000000000001) #The value of the precision: when to stop. 
print(number) #Does not really matters that much the value of prec since it is going to get really close the values at some moment
