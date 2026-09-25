# to fill the name and date in letter template.

letter = '''Dear <|Name|> You are selected <|Date|>'''

# first replace function will return the string and then second function will change in that string.
print(letter.replace("<|Name|>", "Meet,").replace("<|Date|>", "on 03 september 2026.")) # chaining of replace function.