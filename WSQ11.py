x = int(input("What is the beggining of the range of numbers? : "))
y = int(input("What is the end of such range? : "))

def palindrome(n):
    return int(str(n)[::-1])
def Lychrel(x,y):
    candidate = list(range(x,y))
    palindr = 0
    nonlych = 0
    lych = 0
    count = 0
    for i in candidate:
        if i == palindrome(i):
            palindr += 1
        elif i == 0:
            palindr += 1
        else:
            q=i
            while q != palindrome(q) and count != 30:
                q = q+palindrome(q)
                if q == palindrome(q):
                    nonlych += 1
                count +=1
            if q!=palindrome(q) and count >= 30:
                lych+=1
    print(("Natural Palindromes: ")+str(palindr))
    print(("Non-Lychrels that become palindrome : ")+str(nonlych))
    print(("Lychrel candidates: ")+str(lych))


print("Calculating whether each value is one of: palindrome, non-lychrel or lychrel candidate")
print(("The results are from the range ")+str(x)+(" to ")+str(y))
print(Lychrel(x,y))
