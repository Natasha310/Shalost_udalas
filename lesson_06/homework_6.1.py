"""Module providing a new function printing python version."""



print("Enter your sentence")
characters = input()
char_list = []
for c in characters:
    if c.isalnum() :
        print(characters)
    else:
        char_list.append(c)
        continue

print(len(char_list))

# End-of-file (EOF)# End-of-file (EOF)
