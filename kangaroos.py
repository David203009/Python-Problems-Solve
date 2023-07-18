#falta
def kangaroo(x1, v1, x2, v2):
    for i in range(4):
        x1 += v1
        x2 += v2
    if(x1 == x2):
        return "YES"
    return "NO"

print(kangaroo(42,3,94,2))



