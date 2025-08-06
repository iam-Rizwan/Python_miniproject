A=int(input("Enter A value"))
B=int(input("Enter B Value"))
C=input("Enter an Operator(+,-,/,*,%)")
if C== '-' :
    print(A-B)
elif C== '+' :
    print(A+B)
elif C== '/' :
    if A and B > 0:
        print(A/B)
    else:
        print('0s cannot be used')
elif C== '+' :
    print(A+B)
elif C== '**' :
    print(A*B)
elif C== '%' :
    print(A%B)
else:           
    print("incorrect")