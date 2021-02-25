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
