def prod_numbers(user_number):
   while user_number > 10:
       remain = 1
       for i in range(len(str(user_number))):
           remain *= int(str(user_number)[i])
       user_number = remain
   print(remain)

user_number = int(input('Enter number:'))
prod_numbers(user_number)