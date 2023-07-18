
def nb(n):
    sum = 0
    x = 1
    while n != sum:
        sum += x ** 3
        x += 1
        if(sum > n):
            return -1
    return x - 1

print(nb(1071225))
print(nb(91716553919377))
91716553919377
  

