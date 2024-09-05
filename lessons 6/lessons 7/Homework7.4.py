def common_elements():
    num_lis1 = [i for i in range(0, 100) if i % 3 == 0]
    num_lis2 =  [i for i in range(0, 100) if i % 5 == 0]
    gen_lis = list(set(num_lis1) & set(num_lis2))
    print(gen_lis)
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
