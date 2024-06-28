# f = open("file.txt",'r')
# text = f.read()
# print(text)
# f.close()

# f = open("file.txt",'w')
# f.write("Hello, this is vidisha")
# f.close()

# f = open("file.txt",'a')
# f.write(" Hello, this is vidisha")
# f.close()

#automatically closes the file:
with open("file.txt",'a') as f:
    f.write(" I am inside with")
