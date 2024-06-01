lst = [6, 8, 12, 10, 2, 4]

# check whether an element is present in list or no (works with strings as well)
if 6 in lst:
    print("Yes")
else:
    print("No")

#list slicing :
print(lst[0:6:2])

# Note : List comprehension
lists = [i for i in range(1,11) if i % 2 == 0]
print(lists)

lst.append(17)
print(lst)
# lst.sort()
# print(lst)
