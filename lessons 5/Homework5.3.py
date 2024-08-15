#hashtag = input('Enter hastag :')
#print(hashtag.capitalize())
print('#' + ''.join([i for name in input('Enter name:').split() for i in name.title() if i.isalpha()])[:140])
