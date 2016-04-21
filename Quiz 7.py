Cardinality1 = int(input("How many numbers will the first list have?: "))
Cardinality2 = int(input("How many numbers will the second list have?: "))
List1 = [] #Usually as vector (x , y , z)
List2 = []
Vector = []
for i in range(Cardinality1):
    Set_Members1 = int(input("What is the number for the first list?: "))
    List1.append(Set_Members1)

for i in range(Cardinality2):
    Set_Members2 = int(input("What is the number for the second list?: "))
    List2.append(Set_Members2)

def dot_product(List1, List2):
    if Cardinality1 != Cardinality2:
        return float("NaN") #When it does not have the same number of elements
        #There is an element without a pair to multiply which gives 'Not a Number'
    else:
        for i in range(Cardinality1): #It can be either of the two Cardinalties
        #Since they are the same
            Vector.append(List1[i]*List2[i])
        print("The multiplication of such list members by order is: ", Vector)
        DotSum = sum(Vector)
        return DotSum
        print (DotSum)

print("Members of the first list: ", List1)
print("Members of the second list: ", List2)
print("The Sum of the numbers previously listed is: ", dot_product(List1, List2))
