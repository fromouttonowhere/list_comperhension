
with open("file1.txt") as file1:
    list1 = file1.readlines()
    # list1_updated = [int(item.strip()) for item in list1]
with open("file2.txt") as file2:
    list2 = file2.readlines()
    # list2_updated = [int(item.strip()) for item in list2]

common_items = [int(num) for num in list1 if num in list2]
print(common_items)
