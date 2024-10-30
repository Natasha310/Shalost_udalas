"""Module providing a new function printing python version."""



print("Enter some text")
some_text = input()
for i in some_text.lower():
    if "h" in some_text.lower():
        print("Success")
    else:
        print("Enter char H/h to complete")
        some_text = input()

# End-of-file (EOF)# End-of-file (EOF)
