#Link to pdf: http://kenscourses.com/tc101winter2016/wp-content/uploads/2016/04/TC101_FinalExamQuestions.pdf
#Not finished yet
#I left them as comments so it doesn't affect the current excersice that is trying to run.
'''#9. Count words
namefile = input("Name of the file: ")
word = input("What word are you counting?: ").lower()

def Searcher(namefile, word):
    counter = 0
    with open(namefile) as openfile:
        for line in openfile:
            line = line.lower()
            counter += line.count(word)
        return counter

print(Searcher(namefile,word))'''
#------------------------------------------------------------------------------
'''#8. Square root PENDING
S = int(input("What is the number?: "))
X0 = 600.000

def SquareRoot(S,X0):
    x1 = (X0 + (S/X0))*0.5
    NextX =  '''
#------------------------------------------------------------------------------
'''#7.Suma de cuadrados en una lista
Cardinality = int(input("How many elements are in the list? "))
List = []

for i in range (Cardinality):
    Elements = float(input("Number: "))
    List.append(Elements)

def sum_squares(List):
    Squared_List = []
    for i in range (Cardinality):
        Squares = List[i]**2
        Squared_List.append(Squares)
    Squared_Sum = sum(Squared_List)
    return Squared_Sum

print (sum_squares(List))'''
#-------------------------------------------------------------------------------
'''#6.Fibonacci
Cardinality = int(input("What Cardinality of the Fibonacci series would you like to see?: "))
Fibonacci=[0,1]

def Fibo(Fibonacci):
    for i in range (Cardinality):
        Fibonacci.append(Fibonacci[-1]+Fibonacci[-2])
    return (Fibonacci[Cardinality])
#[-1] = Ultimo // [-2] Penultimo
#Sumar el ultimo con el penultimo de la lista y agregarlo a la lista
#Esto se repide hasta 'Cardinality' de veces
print(Fibo(Fibonacci))'''
#------------------------------------------------------------------------------
'''#5. Minimo de una lista
Lista = []

for i in range(4):
    contenido = float(input("Numero: "))
    Lista.append(contenido)

def Minimo(Lista):
    maspequeño = min(Lista)
    return maspequeño

print("El más pequeño de la lista es: ", Minimo(Lista))'''
#------------------------------------------------------------------------------
'''#4. Promedio de una lista
import math

Lista = []
Cardinalidad = int(input("¿Cuantos elementos contiene la lista?: "))

for i in range(Cardinalidad):
    Elementos = float(input("Numero: "))
    Lista.append(Elementos)

def Promedio(Lista):
    promedio = (sum(Lista)) / Cardinalidad
    return promedio

print("El promedio es: ", Promedio(Lista))'''
#------------------------------------------------------------------------------
'''#3. Factorial
Numero = int(input("What would be the factorial number? "))

def Factorial(Numero):
    Resultado = 1
    for i in range (1,Numero+1,1):
        Resultado *= i
    return Resultado

print(Factorial(Numero))'''
#------------------------------------------------------------------------------
'''#2. T's trangulo
T = int(input("¿Cual es el maximo de 'T'?: "))

def PrimeraMitad(T):
    for i in range (0,T,1):
        for k in range (0,i+1,1):
            print("T", end="")
        print("")
    return ""

def SegundaMitad(T):
    for i in range(T-1,0,-1):
        for k in range(0,i,1):
            print("T", end="")
        print("")
    return ""

print(PrimeraMitad(T), end="")
print(SegundaMitad(T))'''
#------------------------------------------------------------------------------
'''#1. Distancia
import math
units = str(input("What are the units: " ))
x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

def Hypotenuse(x1,y2):
    Distance = math.hypot(x1-x2,y1-y2)
    return Distance

#print("x = "+str(x)+"y = "+str(y))
print("Distance = "+ str(Hypotenuse(x1,y2)) + str(units))
'''
