x = [] #Vacio para que se llene la lista con el comando de abajo 
import statistics #Para poder usar los statistics.xxx

for i in range (10):
	num = float(input("Number: "))
	x.append(num) #append es para agregar a la lista de numeros

def suma(x):
	return(sum(x))

def promedio(x):
	return(suma(x) / float(len(x)))

def desviacionestandar(x): 
	return(statistics.stdev(x))
#WSQ10 did not requested this next ones but I just learned how to do this. So, duck it!
def populationstandar(x): 
	return(statistics.pstdev(x))
#Spanglish is the mejor language
def variance(x):
	return(statistics.variance(x))

def populationvariance(x):
	return(statistics.pvariance(x))
	
print ("The sum is:  ", suma(x))
print ("The average is: ", promedio(x))
print ("The standard deviation is: ", desviacionestandar(x))
print ("The popular standar deviation is: ", populationstandar(x))
print ("The variance is: ", variance(x))
print ("The population variance deviation is: ", populationvariance(x))
