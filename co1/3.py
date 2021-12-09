list=[2,-6,4,-8,5,-7,1,2]
n=[num for num in list if num>0]
print(n)


n=int(input(" enter the limit"))
zlist=[i**2 for i in range(1,n+1)]
print("square of no=",zlist)

n=str(input("enter the string"))
for i in n:
    if(i in 'a,e,i,o,u'):
        print("vowels=",i)

y=input("enter word")
for i in y:
    print(i)
    print(ord(i))
