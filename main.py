# Le factoriel d"un nombre
n= int(input("entre un nombre "))
while n<0:
    n=int(input("entre un nombre "))
p=1
i=0
if n>=0:
    for i in range(1,n+1):
        p=p*i
    print("le factoriel  est",p)