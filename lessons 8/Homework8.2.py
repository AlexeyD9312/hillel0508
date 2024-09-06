def is_palindrome(text):
    text = ''.join([a for a in text if a.isalpha()])
    text = text.lower()
    rev_text = text[::-1]
    print(text)
    print(rev_text)
    print("True" if rev_text == text else "False")
text = input()
#assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
#assert is_palindrome('0P') == False, 'Test2'
#assert is_palindrome('a.') == True, 'Test3'
#assert is_palindrome('aurora') == False, 'Test4'
#print("ОК")
