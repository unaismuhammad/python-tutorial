

row = 5
for a in range(1,row+1):
    for j in range(1,a+1):
        print(j,end=" ")
    print()




a="the cat and dog"
print("the",a.count("the"),"cat",a.count("cat"),"and",a.count("and"),"dog",a.count("dog")) 

#1

list2=[1,2,3,4,5,6,7,8,9,10]
a=max(list2)
b=min(list2)
print(a)
print(b)

#2

c=list2[::-1]
print(c)

#3

d=list2.count(3)
print(d)

#4

set1=(set(list2))
list1=(list(set1))
print(list1)

#5

a=[1,2,3,4,5,7]
b=[6,7,8,9,10]
c=a+b
print(c)


#6

a="malayalam"
if a==a[::-1]:
    print("palindrome")
elif a !=a[::1]:
        print("not palindrome")


#7
my_tuple = ("apple","banana","orange")
temp_list = list (my_tuple)
