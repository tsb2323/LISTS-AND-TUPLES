#lists like arrrays
#built is data structure that store multiple variables
marks=["tanvir",33,22,33.3]
print(marks)
print(type(marks))
print(marks[0])#indexing
#srings are immutable but lists are mutable (values can be changed )
marks[0]="batman"
print(marks)

#slicing in list
#marks[start-index:end-index]
#marks[ :3](0:4)
#marks[1:](1:len(marks))
print(marks[1: ])

#LIST METHODS
list=[1,2,3,4]
list.append(5)#add element at the end of the list 
list.insert(0,2)#add element at specific index 0
print(list)#new list[2,1,2,3,4,5]
list.sort()#sort in ascending order
print(list)
list.sort(reverse=True)#sort in descending order
print(list)
list.reverse()#reverse the list
print(list)
#in strings sorting is done using alphabet priority
list.remove(3)#remove element from the list
list.pop(0)#remove element from the indexxx
print(list)

#tuples like lists but are immutable ()used in tyuples
age=(2,2,3,3,4,4)
print(type(age))
#but
tup=(3)#it will be integer to decalre it a tuple tup=(3,), is always required
#tuple methods
print(age.count(2))#count the number of times 2 is present in the tuple
print(age.index(3))#find the index of the first occurrence of 3 in the tuple


