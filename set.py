# #empty sets

# a=set()
# print(type(a))

# #value adding

# a={"apple","orange","banana"}
# print(type(a))


#adding a single item in set

# my_set ={1,2,3}
# my_set.add(4)
# print(my_set)

#adding multiple

# my_set={1,2,3,4,5}
# my_set.update([6,7,9])
# print(my_set)


#forloop

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

#remove number

# a={1,2,3}
# a.remove(3)
# print(a)

#discard

# a={1,2,3}
# a.discard(5)
# print(a)

# set1 = {1,2,3}
# set2 = {1,2,3,4,5,6}
# result=set1 ^ set2
# print(result)

# set1 = {1,2,3}
# set2 = {1,2,3,4,5,6}
# result=set1 & set2
# print(result)


#subset

set1 = {1,2,3}
set2 = {1,2,3,4,5,6}
print(set1.issubset(set2))

set1 = {1,2,3}
set2 = {1,2,3,4,5,6}
print(set2.issubset(set1))

#superset

set1 = {1,2,3}
set2 = {1,2,3,4,5,6}
print(set2.issuperset(set1))