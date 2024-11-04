"""Module providing a new function printing python version."""



print("Enter your sentence")
uniq_symbols = input()
for c in uniq_symbols:
    if len(set(uniq_symbols.lower())) >= 10:
        print(True)
    else:
        print(False)
    break











# End-of-file (EOF)# End-of-file (EOF)
