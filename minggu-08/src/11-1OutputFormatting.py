import reprlib
print(reprlib.repr(set('superclaifragilisticexpialidocious')))
print()

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]

pprint.pprint(t, width=30)
print()

import textwrap
doc = """The wrap() method is just like fill() except that it returns
    a list of strings instead of one big string with newlines to separate
     the wrapped lines."""
print(textwrap.fill(doc, width=40))
print()

import locale
print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))
conv = locale.localeconv() #getting a mapping of conventions
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                            conv['frac_digits'], x), grouping=True))
