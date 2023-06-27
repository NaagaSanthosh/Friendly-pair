a=int(input("Enter a first number: "))
b=int(input("Enter a second number: "))
suma=0
sumb=0
for i in range(1,a):
    if a%i==0:
        suma+=i
for j in range(1,b):
    if b%j==0:
        sumb+=j
if a==suma and b==sumb:
    print("{} and {} are a friendly pair".format(a,b))
else:
    print("{} and {} are not  friendly pair".format(a,b))
