my_list =[]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)# Adding an element to the list
print(my_list)  # Output: [10, 20, 30, 40]
my_list.insert(1, 15)  # Inserting an element at index 
print(my_list)  # Output: [10, 15, 20, 30, 40]
my_list.extend([50, 60, 70])  # Extending the list with multiple elements
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]
my_list.pop(7)  # Removing the last element
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]
my_list.sort()  # Sorting the list
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]
my_list.index(30)  # Finding the index of an element
print(my_list.index(30))  # Output: 3


