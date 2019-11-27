# Case #5


# The program ...

# Developers:   Zemtseva A. (%),
#               Zaitseva A. (%),
#               Daniel A.   (%).


import urllib.request

# Choosing the language.
print('Choose language/ Выберите язык.\n1) English/ Английский язык;\n2) '
      'Russian/ Русский язык.')
language = input('Input number/ Введите цифру: ')

while True:
    if language == '1':
        import eng_local as lc

        break
    elif language == '2':
        import rus_local as lc

        break
    print('Choose language/ Выберите язык./n1) English/ Английский язык;\n2) '
          'Russian/ Русский язык.')
    language = input('Input number/ Введите цифру: ')


url = 'http://www.nfl.com/player/brycepetty/2495443/profile'
url = urllib.request.urlopen(url)
url = url.read()
text = str(url)

part_name = text.find('player-name')
name = text[text.find('>', part_name)+1:text.find('&', part_name)]

text = text[text.find('TOTAL')+5:]
text = text.replace("</", ' ')
text = text.replace("<td>", '')
text = text.replace("t", '')
text = text.replace("n", '')
text = text.replace("\\", '')
text = text.replace("d>", '')
text = text.replace(',', '')

ptr = text.find(' ')
COMP = text[ptr+1:text.find(' ', ptr+1)]
ptr = text.find(' ', ptr+1)
ATT = text[ptr+1:text.find(' ', ptr+1)]
ptr = text.find(' ', text.find(' ', ptr+1)+1)
YDS = text[ptr+1:text.find(' ', ptr+1)]
ptr = text.find(' ', text.find(' ', text.find(' ', ptr+1))+1)
TD = text[ptr+1:text.find(' ', ptr+1)]
ptr = text.find(' ', text.find(' ', ptr)+1)
INT = text[ptr+1:text.find(' ', ptr+1)]

print(name)
print(TD)
print(INT)
print(YDS)
print(ATT)
print(COMP)
