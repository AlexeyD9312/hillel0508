list=[4,0,0,8,0,1,87,0,5,-3,0,-5,0,-56,6]
new_list=[]
zero_list=[]
for i in list:
    if i!=0:
       new_list.append(i)
    else:
        zero_list.append(i)
print(new_list+zero_list)

