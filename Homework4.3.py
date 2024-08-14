import random
x=[]
ran=random.randint(3,8)
for i in range(ran,13,1):
    x.append(random.randint(0,100))
print(x)
print(x[0],x[2],x[-2])

lst = [random.randint(0, 9) for _ in range(6)]
