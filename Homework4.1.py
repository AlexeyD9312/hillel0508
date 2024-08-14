
list=[4,0,0,8,0,1,87,5,-3,0,-5,-56,0,3]
list_nozero=[i for i in list if i!=0]
list_zero=[i for i in list if i==0]
print(list_nozero+list_zero)
