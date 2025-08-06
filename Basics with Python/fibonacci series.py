a=0
b=1
#print(a)
#print(b)
c=int(input("Enter Nth Value"))
print(a)
print(b)
for i in range(1,c):
    c=a+b
    print(c)
    a,b=b,c