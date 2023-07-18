def binary_array_to_number(arr):
    sum = 0
    for i,x in enumerate(arr):
        if x == 1:
            sum += 2**(len(arr)-1-i)
    return sum

print(binary_array_to_number([1,1,1,1,1]))
        