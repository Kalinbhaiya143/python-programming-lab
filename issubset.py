
# using issubset()

# initializing list
test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5]

# printing original lists
print("Original list : " + str(test_list))
print("Original sub list : " + str(sub_list))

# using issubset() to
# check subset of list
flag = 0
if(set(sub_list).issubset(set(test_list))):
	flag = 1

# printing result
if (flag):
	print("Yes, list is subset of other.")
else:
	print("No, list is not subset of other.")
