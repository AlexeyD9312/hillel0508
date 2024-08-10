x=[1,3,5,0,7,4,232,64,3,56,6]
y=[x for x in x if not x%2]
z=x[-1]
r=sum(y)
i=r*z
print(i)