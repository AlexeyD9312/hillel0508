import string
import keyword
name = input('Enter name:')
print(not any(i in name for i in string.punctuation)
      and not any(i in name for i in ' ')
      and name[0].isalpha() and name.isupper() and name == keyword.kwlist)
