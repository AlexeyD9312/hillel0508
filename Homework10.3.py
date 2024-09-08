def is_even(digit):
    if digit %2 == 0:
        return True
    else:
        return False

digit = int(input("Введіть число:"))
print(is_even(digit))

assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'

