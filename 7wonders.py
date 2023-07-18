#(4,2,2) => 38

def wonder(a,b,c):
    sevens = 0
    suma = a**2 + b**2 + c**2
    while (a > 0 and b > 0 and c > 0):
        sevens += 1
        a -= 1 
        b -= 1 
        c -= 1 
    suma += 7*sevens
    return suma

print(wonder(4,3,2))
    