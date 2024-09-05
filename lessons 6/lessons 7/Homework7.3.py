import re

def second_index(text, symbol):
    if text.count(symbol) > 1:
      matches = re.finditer(symbol, text)
      indices = [match.start() for match in matches]
      print(indices[1])
    else:
        print("None")
second_index(input("Print your text:"), input("Print your symbol:"))
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')