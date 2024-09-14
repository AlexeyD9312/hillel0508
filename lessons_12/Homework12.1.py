import codecs


import pandas


with codecs.open('draft.html', 'r', 'utf-8') as file:
    html = file.read()

#html = '<p><span>is not <b><span>allowed</span></b></span></p>'
#print(bleach.clean(html, tags=[], strip=True))

#C:\Users\User\AppData\Local\Programs\Python\Python312\Scripts
with codecs.open('cleaned.txt', 'w','utf-8') as f:
    f.write(html)

