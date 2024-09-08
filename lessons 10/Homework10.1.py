def pow(x):
    return x ** 2

def some_gen(begin, end, func):
    n = 1
    while n <= end:
        yield begin
        begin = pow(begin)
        n += 1

gen = some_gen(2, 4, pow)
for value in gen:
    print(list[value])
