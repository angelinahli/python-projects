# filename: acrobatic_text_art.py
# author: Angelina Li
# date: 2017
# desc: Script written long ago to print words using fancy ascii fonts

with open('acrobatic_font.txt') as font:
    font_info = font.read().splitlines()

list_structure = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '!', '?', 
                  '+', '=', '-', '_', ';', ':', '(', ')', '@', '#', '$', '%', '^',
                  '&', '*', ',', '<', '>','`', '~']

def make_font_dict(font_strings, n, list_structure, recur_dct):
    if len(list_structure) > 0:
        lines = [font_strings[i].rstrip() for i in range(n)]
        width = max([len(line) for line in lines])
        recur_dct[list_structure[0]] = [line + ' '*(width - len(line)) for line in lines]
        make_font_dict(font_strings[n:], n, list_structure[1:], recur_dct)
        return recur_dct
    else:
        recur_dct["'"] = ['   o/ ', '  /v  ', ' />   '] + ['      ' for n in range(9)]
        recur_dct['"'] = ['  o   o    o   o  ', ' <|> <|>  <|> <|> ', ' < > < >  < > < > '] + ['                  ' for n in range(9)]
        recur_dct[' '] = ['    ' for n in range(12)]
        return recur_dct

def print_word(font_strings, n, list_structure):
    chars_graphics = make_font_dict(font_strings, 12, list_structure, {})
    word = raw_input("Print this: ").lower()
    output = []
    for row in range(n):
        txt = ''
        for char in word:
            line = chars_graphics[char][row]
            if len(line) > 0:
                txt += line + ' '
            else:
                txt += max([len(lin) for lin in chars_graphics[char]])*' ' + ' '
        output.append(txt)
    if len(output[0]) < 200:
        for line in output:
            print line
    else:
        print "Sorry, this string is too long. Try breaking it up into smaller chunks?"
        print_word(font_strings, n, list_structure)
    return output
 
print_word(font_info, 12, list_structure)