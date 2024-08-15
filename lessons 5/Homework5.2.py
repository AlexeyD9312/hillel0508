while True:
    x=float(input('число 1:'))
    d=input('математична дія:')
    y=float(input('число 2:'))
    if y!=0:
        if '*' in d:
            print('дорівнює',x*y)
        elif '+' in d:
            print('дорівнює', x + y)
        elif '-' in d:
            print('дорівнює', x - y)
        elif '/' in d and y!=0:
               print('дорівнює', x / y)
        else:
               print("некоректна дія")
    else:
        print('not dilit na 0')
    reset = input ("Запустить калькулятор заново: " )
    if reset == 'y':
        continue
    else:
        break