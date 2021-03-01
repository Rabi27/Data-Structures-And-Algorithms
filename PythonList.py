#Create a list
l = [1,2,44,55]

#append method adds element at the end of the list
l.append(33)

#Remove all the elements of the list
l.clear()

#Count the number of occurrences of an element
#It returns the count, which can be stored in a variable
a = l.count(2)

#extend method
#The extend() method adds the specified list elements (or any iterable) to the end of the current list.
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)

#Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

#Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

#Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

#The index() method returns the position at the first occurrence of the specified value.
#If the element is not found, a ValueError exception is raised.
#Arguments passed to the method are:
#element - the element to be searched

#start (optional) - start searching from this index
#end (optional) - search the element up to this index
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

#Remove all elements from the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

'''
The copy() method returns a shallow copy of the list.

A list can be copied using the = operator. For example,
'''
old_list = [1, 2, 3]
​new_list = old_list
'''
The problem with copying lists in this way is that if you modify new_list, old_list is also modified. 
It is because the new list is referencing or pointing to the same old_list object.

'''
old_list = [1, 2, 3]
new_list = old_list

# add an element to list
new_list.append('a')

print('New List:', new_list)
print('Old List:', old_list)

'''
However, if you need the original list unchanged when the new list is modified, you can use the copy() method.
'''
new_list = list.copy()
#cheat day

'''
The sort() method sorts the elements of a given list in a specific ascending or descending order.

The syntax of the sort() method is:

list.sort(key=..., reverse=...)
Alternatively, you can also use Python's built-in sorted() function for the same purpose.

sorted(list, key=..., reverse=...)
Note: The simplest difference between sort() and sorted() is: sort() changes the list directly and doesn't return any value, while sorted() doesn't change the list and returns the sorted list.

'''
