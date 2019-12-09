# Case #5

# The program calculates Quarterback passer rating in American football.
# The rating is calculated according to the formula proposed by the
# National Football League (NFL). Five parameters are used for calculation:
# ATT, COMP, YDS, TD, INT.
# The program reads the URLs of pages describing the profile of each player from the NFL website.

# Developers:   Zemtseva A. (%),
#               Zaitseva A. (30%),
#               Daniel A.   (%).

import urllib.request

file = open('input.txt')
line = file.readline()
out_file = open('output.txt', 'w')

# Draw a table for the titles.
name = 'NAME'
COMP = 'COMP'
ATT = 'ATT'
YDS = 'YDS'
INT = 'INT'
TD = 'TD'
passer_rating = 'PR'
name += ((20 - len(name)) * ' ')
COMP += ((7 - len(COMP)) * ' ')
ATT += ((7 - len(ATT)) * ' ')
YDS += ((7 - len(YDS)) * ' ')
TD += ((7 - len(TD)) * ' ')
INT += ((7 - len(INT)) * ' ')
passer_rating += ((7 - len(passer_rating)) * ' ')
out_file.write('%2s %3s %4s %5s %6s %7s %8s' % (name, TD, INT, YDS, ATT, COMP, passer_rating))
out_file.write('\n')

# The loop that changes a link to the player's page.
while line:
    url = line
    url = urllib.request.urlopen(url)
    url = url.read()
    text = str(url)

    # Searching in the string for the name of player.
    part_name = text.find('player-name')
    name = text[text.find('>', part_name) + 1:text.find('&', part_name)]

    # Clearing the string from extra symbols.
    text = text[text.find('TOTAL') + 5:]
    text = text.replace("</", ' ')
    text = text.replace("<td>", '')
    text = text.replace("t", '')
    text = text.replace("n", '')
    text = text.replace("\\", '')
    text = text.replace("d>", '')
    text = text.replace(',', '')

    # Searching in the string for the required values.
    ptr = text.find(' ')
    COMP = text[ptr + 1:text.find(' ', ptr + 1)]
    ptr = text.find(' ', ptr + 1)
    ATT = text[ptr + 1:text.find(' ', ptr + 1)]
    ptr = text.find(' ', text.find(' ', ptr + 1) + 1)
    YDS = text[ptr + 1:text.find(' ', ptr + 1)]
    ptr = text.find(' ', text.find(' ', text.find(' ', ptr + 1)) + 1)
    TD = text[ptr + 1:text.find(' ', ptr + 1)]
    ptr = text.find(' ', text.find(' ', ptr) + 1)
    INT = text[ptr + 1:text.find(' ', ptr + 1)]

    # Passer rating counting.
    passer_rating = (((float(COMP) / float(ATT) - 0.3) * 5 + (float(YDS) / float(ATT) - 3)
                      * 0.25 + (float(TD) / float(ATT)) * 20 + 2.375 -
                      (float(INT) / float(ATT) * 25)) / 6) * 100

    passer_rating = "{0:.2f}".format(passer_rating)

    # Create a table from the values in the file.
    name += ((20 - len(name)) * ' ')
    COMP += ((7 - len(COMP)) * ' ')
    ATT += ((7 - len(ATT)) * ' ')
    YDS += ((7 - len(YDS)) * ' ')
    TD += ((7 - len(TD)) * ' ')
    INT += ((7 - len(INT)) * ' ')
    passer_rating += ((7 - len(passer_rating)) * ' ')
    out_file.write('%2s %3s %4s %5s %6s %7s %8s' % (name, TD, INT, YDS, ATT, COMP, passer_rating))
    out_file.write('\n')
    line = file.readline()

out_file.close()
file.close()
