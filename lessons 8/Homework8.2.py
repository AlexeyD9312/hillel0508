text = input("Введіть текст:")
def is_palindrome(text):
    text = ''.join([a for a in text if a.isalpha()])
    text = text.lower()
    rev_text = text[::-1]
    if rev_text == text:
        print("True")
    else:
        print("False")

print(is_palindrome(text))
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
