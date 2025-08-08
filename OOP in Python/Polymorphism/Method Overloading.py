class simpCalc():
    def simp(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            x=a+b+c
            y=a-b-c
            return x,y
        elif a!=None and b!=None and c==None:
            x=a+b
            y=a-b
            return x,y    
calc=simpCalc()
print(calc.simp(12,22))
print(calc.simp(10,20,30))