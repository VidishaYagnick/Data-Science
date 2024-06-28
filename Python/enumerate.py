marks = [12, 34, 56, 78, 90, 31, 45]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 4):
#         print("Highest marks")
#     index = index + 1

#This can be done easily using enumerate function : returns value as well as index

for index, mark in enumerate(marks):
    print(index, mark)
    if(index == 4):
        print("Highest marks ")

for v in enumerate(marks):
    print(v) #tuple....order is imp...1st is index 
    print(type(v))

#changing the starting index:
for index, mark in enumerate(marks, start=1):
    print(index, mark)