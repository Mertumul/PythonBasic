
# Finding the roots of 2nd degree equations

#Equation = ax^2+bx+c

#Delta = b**2-4*a*c

# First Root = (-b-delta**0.5)/(2*a)
# Second Root = (+b-delta**0.5)/(2*a)


a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b**2 - 4*a*c

x1 = (-b - delta ** 0.5)/(2*a)
x2 = (-b + delta ** 0.5)/(2*a)

print("First Root:{}\t Second Root:{}".format(x1, x2))
