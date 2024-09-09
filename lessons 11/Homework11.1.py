def prime_generator(end):
    num_list = {}
    n = 2
    while n <= end:
        if n not in num_list:
            yield n
            num_list[n * n] = [n]
        else:
            for x in num_list[n]:
                num_list.setdefault(x + n, []).append(x)
            del num_list[n]

        n += 1

print(*prime_generator(29))


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'