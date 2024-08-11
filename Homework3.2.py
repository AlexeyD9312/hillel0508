from copy import deepcopy
x=[90,43,84,0,6,87]
y=deepcopy(x)
y.insert(0,y[-1])
z=y.pop()
print(x)
print(y)

