#Find if it is a perfect number
def findDivisors(num):
    divisior=list()
    for i in range(1,num):
        if num%i==0:
            divisior.append(i)
        else:
            continue
    return divisior

def isItPerfectNumber(num):
    list=findDivisors(num)
    total=0
    for i in range(0,len(list)):
        total +=list[i]
    
    if(total==num):
        print("{} is a perfect number".format(num))
    else:
        print("{} is not a perfect number".format(num))
        

isItPerfectNumber(6)
isItPerfectNumber(7)