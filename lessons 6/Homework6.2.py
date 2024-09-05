
my_number = int(input('Enter number:'))
if my_number >= 0 and my_number < 8640000:
  minutes, seconds = divmod(my_number, 60)
  hours, minutes = divmod(minutes, 60)
  days,hours = divmod(hours, 24)
  if days >=5:
      print(days, 'Днів,')
  elif days == 0:
      print(days, 'Днів,')
  elif days == 1:
      print(days, 'День,')
  else:
    print(days, 'Дня,')
  print(hours, minutes, seconds, sep=':')
else:
   print('wrong range')

