"""Module providing a new function printing python version."""



lst1 = [1, 3, 5, 7]
lst2 = [1, 4, 5]

result = [(lst1[i] if i < len(lst1) else 0, lst2[i] if i < len(lst2) else 0) for i in range(max(len(lst1), len(lst2)))]

print(result)



# End-of-file (EOF)# End-of-file (EOF)


