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
# lst.sort()   ---->sort in ascending
# print(lst)
# lst.sort(reverse=True) -------> sort in descending
# print(lst)

print(lst.index(10))
print(lst.count(10))

# Copy a list
# m = lst  ### not recommended
# m[0] = 0
# print(lst)   #this changes lst as well...both refer to same list

m = lst.copy()  ### recommended
m[0] = 0
print(lst)   #this changes m only
print(m)

# insert at any index
lst.insert(1,44)
print(lst)

n = [1,3,5,7]
lst.extend(n)
print(lst)

# n = l + m add two list






