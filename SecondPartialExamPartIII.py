x = int(input("base: "))
y = int(input("exponent: "))

def loop(x,y):
    answer = 1
    for i in range (y):
        answer *= x
    return answer

print(loop(x,y))
