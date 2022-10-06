# Finding the type of triangle quadrilateral
tqtype = input("Do you want to find the type of triangle or quadrilateral?")

if tqtype == '3':
    print("please enter the edge of triangle")
    a = int(input("please enter the first edge of triangle"))
    b = int(input("please enter the second edge of triangle"))
    c = int(input("please enter the third edge of triangle"))
    if (a > 0 and b > 0 and c > 0):
        if (a+b > c and a+c > b and b+c > a):
            if (a == b == c):
                print("this triangle is equilateral triangle")
            elif (a == b != c or a == c != b or b == c != a):
                print("isosceles triangle")
            else:
                print("scalene triangle")
        else:
            print("this is not triangle")
    else:
        print("you can't enter negative number or zero")


elif tqtype == '4':
    print("please enter the edge of quadrilateral")
    a = int(input("please enter the first edge of quadrilateral"))
    b = int(input("please enter the second edge of quadrilateral"))
    c = int(input("please enter the third edge of quadrilateral"))
    d = int(input("please enter the forth edge of quadrilateral"))

    if (a > 0 and b > 0 and c > 0 and d > 0):
        if (a == b == c == d):
            print("this is square")
        elif (a == c and b == d):
            print("this is rectangle")
        else:
            print("quadrilateral")
    else:
        print("you can't enter negative number or zero")


else:
    print("please make your choice right")
