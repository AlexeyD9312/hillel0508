def first_word(text) :
    def removeExtraSymbols(text) :
        result = text.replace('.', '')
        result = result.replace(',', '')
        return result

    allWords = text.split()
    for word in allWords:
        if not removeExtraSymbols(word) == '':
            if "." in word:
                word = word.split(".")[0]
            if "," in word:
                word = word.split(",")[0]
            return removeExtraSymbols(word)

print(first_word("don't touch it"))
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'