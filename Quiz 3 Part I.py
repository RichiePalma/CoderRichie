def abs(x,z):
	r = x - z
	return(r)

def abs(y,w):
	t = y - w
	return(t)

def operation3(a,b):
	d = (((a*a) + (b*b))**0.5)
	return(d)

print("Let's find the distance between two points")
x = int(input("'X1' Where in the x axis does it starts?"))
y = int(input("'Y1' Where in the y axis does it starts?"))
z = int(input("'X2' Where in the x axis did it moved?"))
w = int(input("'Y2' Where in the y axis did it moved?"))

a = z - x
b = w - y
#It would be the distance between (x,y) and (z,w)
if z > x:
		(a * -1) #Still do not know if this worked or if this is extra since I made it absolute in the def
if w > y:
		(b * -1)
print("Distance as a point: ", "(", abs(z,x),",", abs(w,y),")")
print ("Total distance between the two points: ", operation3(a,b))
