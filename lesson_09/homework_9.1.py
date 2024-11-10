"""Module providing a new function printing python version."""



list1 = [1, 3, 5, 7]
list2 = [1, 4, 5]

list_target = [(list1[i] if i < len(list1) else 0, list2[i] if i < len(list2) else 0) for i in range(max(len(list1), len(list2)))]

print(list_target)
# End-of-file (EOF)# End-of-file (EOF)


