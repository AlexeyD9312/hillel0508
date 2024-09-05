def correct_sentence(text_1,text_2):
     text_1 = text_1[0].upper() + text_1[1:]
     if text_1[-1] != ".":
         print(text_1 + ".")
     else:
         print(text_1)
     text_2 = text_2[0].upper() + text_2[1:]
     if text_2[-1] != ".":
         print(text_2 + ".")
     else:
         print(text_2)
correct_sentence(input("Print your text_1:"),input("Print your text_2:"))
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'