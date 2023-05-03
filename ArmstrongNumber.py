print("Lütfen bir sayi giriniz")

a=input("a:")
lena=len(a)
a=int(a)
step=0
result=0

temp=a

while temp>0:
    step=temp%10
    result+=step**lena
    temp //=10

if result==a:
    print("{} is a armstrong number".format(a))

else:
    print("{} is not a armstrong number".format(a))
