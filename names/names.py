import time
from binary_search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
bst_names = BSTNode(names_1[0])
for name in names_1[1:]:
    bst_names.insert(name)

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
#RunTime Complexity: O(n^2)
# for name_1 in names_1: 
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
#RunTime Complexity: O(nlog(n))
for name2 in names_2: 
    if bst_names.contains(name2):
        duplicates.append(name2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
#RunTime Complexity: Average case: O(min(len(names_1), len(names_2)), 
#Worst Case: O(len(names_1) * len(names_2))
set_duplicates = set(names_1).intersection(set(names_2))
end_time = time.time()
print (f"{len(set_duplicates)} set_duplicates:\n\n{', '.join(set_duplicates)}\n\n")
print (f"runtime of set_duplicates: {end_time - start_time} seconds")
