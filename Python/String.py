a = '''
Hey guys
Good afternoon
I am learning Strings
'''
print(a)
for c in a:
    print(c)

word = "Vidisha Yagnick"
#string methods return new string
print(word.upper())
print(word.lower())
word1 = "Vidisha!!"
print(word1.rstrip("!"))
print(word.replace("i","a"))

word2 = "vidisha is a Girl"
print(word2.split(" "))
print(word2.capitalize())
print(word2.count("vidisha"))
