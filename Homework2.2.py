number=int(input('Print:'))
n1=number//1%10
n2=(number//10%10)
n3=number//100%10
n4=number//1000%10
n5=number//10000
k1=n1*10000
k2=n2*1000
k3=n3*100
k4=n4*10
k5=n5*1
print(k1+k2+k3+k4+k5)

