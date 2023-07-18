#s y t marcan la casa de pepito, s como minimo y t como maximo
#a marca el punto de manzanas y b el de naranjas
#a esta a la derecha de la casa y b a la izquierda
#apples es un array que indica la distancia en la que cayeron las manzanas
#oranges hace lo mismo con las naranjas que caen


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [a+x for x in apples]
    oranges = [b+x for x in oranges]
    ap = sum(1 for x in apples if x >= s and x <=t)
    ora = sum(1 for x in oranges if x >= s and x <=t)
    print(f"{ap}\n{ora}")

countApplesAndOranges(7,11,5,15,[-2,2,1],[5,-6])
