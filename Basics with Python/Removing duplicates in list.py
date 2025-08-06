from collections import OrderedDict
A=['a','a','m','m','r','r']
B=[2,2,'k','k',0,0,1,1]
AA=list(OrderedDict.fromkeys(A))
BB=list(OrderedDict.fromkeys(B))
print(AA)
print(BB)