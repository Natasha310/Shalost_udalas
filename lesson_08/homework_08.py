"""Module providing a new function printing python version."""



from tomlkit import array

ar = array(["1,2,3,4", "1,2,3,4,50","qwerty1,2,3"])

def count_massive(ar):
    try:
        result1, result2 = 0, 0
        l1 = list(map(int, ar[0].split(',')))
        l2 = list(map(int, ar[1].split(',')))
        result1 += sum(l1)
        result2 += sum(l2)
        print(result1,'\n',result2)
        l3 = list(map(int, ar[3].split(',')))


    except IndexError:
        print("Cannot do it")



count_massive(ar)








# End-of-file (EOF)# End-of-file (EOF)
