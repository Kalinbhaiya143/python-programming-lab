"""
Python code to demonstrate
checking of element existence
using List count() method
"""

# Initializing list
test_list = [10, 15, 20, 7, 46, 2808]

print("Checking if 15 exists in list")

# number of times element exists in list
exist_count = test_list.count(15)

# checking if it is more then 0
if exist_count > 0:
	print("Yes, 15 exists in list")
else:
	print("No, 15 does not exists in list")
