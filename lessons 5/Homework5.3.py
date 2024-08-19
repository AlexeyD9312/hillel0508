hashtag = input('Enter name :')
print('#' +''.join([i for name in hashtag.split() for i in name.capitalize() if i.isalpha()])[:140])


