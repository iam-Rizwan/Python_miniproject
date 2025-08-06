def add(x, y):
    z=x + y
    return z
    
def multi(x, y):
    z=x * y
    return z

def div(x, y):
    z=x / y
    return z

def sub(x, y):
    z=x - y
    return z

print("Enter X & Y to get calculation for + , - , * and /")
x=int(input("Enter X value"))
y=int(input("Enter X value"))
 
print("Addition :",add(x, y))
print("Subraction :",sub(x, y))
print("multiplication :",multi(x, y))
print("division :",div(x, y))
