a = int(input("Please write an integer number: "))
b = int(input("Now the next integer number please: "))

def gcd(a,b):
    if b == 0:
        return a #0 is always divisible 
    else:
        return gcd(b, a%b) #It will keep repeating the process until b is 0 
		#They call this recursive functions #plottwist

print (("The greatest common denominator of ")+str(a)+(" and ")+str(b)+(" is: ")+str(gcd(a,b))) #This is new in my codes
#I will try to use it more often to remind the user which numbers he used and stuff. 
