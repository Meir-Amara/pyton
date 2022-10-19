from add_mod import add_mod

def mul (x,y):
    total=0
    for i in range(y):
        total= add_mod(total,x)
    return total

mul(2,4)