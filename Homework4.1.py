
x=[4,0,0,8,0,1,87,5,-3,0,-5,-56,0,4]
n =len(x)
k = 0
for i in list(range(n)):
    if x[i]:
        x[k] = x[i]
        k += 1
x[k:n:1] = [0]*(n-k)
print(x)

