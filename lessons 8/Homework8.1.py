def add_one(some_list):
    some_list= int(''.join(map(str, some_list)))
    some_list += 1
    def digits_iterative(some_list):
        digits = []
        while some_list:
            digits += [some_list % 10]
            some_list //= 10
        return digits[::-1] or [0]
some_list = input("Введіть числа:")
print(add_one(some_list))
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")