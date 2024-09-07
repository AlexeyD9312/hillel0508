def difference(number_list ):
    if number_list:
        max_number = max(number_list )
        min_number = min(number_list )
        difference = max_number - min_number
        print(difference)
    else:
        print("0")

number_list=[1, 2, 3]
print(difference(number_list))
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
