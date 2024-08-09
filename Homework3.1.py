x=float(input('число 1:'))
d=input('математична дія:')
y=float(input('число 2:'))
if '*' in d:
    print('дорівнює',x*y)
elif '+' in d:
    print('дорівнює',x + y)
elif '/' in d:
    print('дорівнює',x / y)
elif '-' in d :
    print('дорівнює',x - y)
else:
    print('некоректна математична дія!')
#у цій программі може обчислюватися лише 2 числа


