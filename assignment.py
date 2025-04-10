# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append 10, 20, 30, 40 to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element (70)
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of 30
index_of_30 = my_list.index(30)
print(f"Index of 30: {index_of_30}")
