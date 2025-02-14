
def find(x, L):

    if not L:
        return False
    
    if x == L[0]:
        return True
    
    return find(x, L[1:])

x = 18
L = [2,5,7,8,10]

found = find(x, L)

print(found)