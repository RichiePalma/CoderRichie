Maximo = int(input("¿Cuantal es el maximo de T's?: "))

def PrimeraMitad(Maximo):
    for i in range (0, Maximo,1):
        for k in range (0,i+1,1):
            print("T", end="")
        print("")
    return""

def SegundaMitad(Maximo):
    for i in range (Maximo-1,0, -1):
        for k in range (0,i,1):
            print("T", end="")
        print("")
    return""

print(PrimeraMitad(Maximo), end="")
print(SegundaMitad(Maximo))
#print(printoperation, end="")
    #end="" es para que se impriman en el mismo renglon
