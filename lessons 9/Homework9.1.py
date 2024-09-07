from collections import Counter
def popular_words(text, words):
    c = Counter(text.lower().split())
    return {word: c.get(word, 0) for word in words}
print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'just', 'near']))
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'