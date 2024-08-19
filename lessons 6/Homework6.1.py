import string
alphabet = string.ascii_letters
let_interval = input("Enter interval:")
let_list = list(let_interval)
for i in alphabet:
 if i == let_list[0]:
  print(alphabet[alphabet.find(let_list[0]):alphabet.find(let_list[2])+1])


