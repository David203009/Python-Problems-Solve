# Write a function named sumDigits which takes a number as input and returns the sum 
# of the absolute value of each of the number's decimal digits.

def sumDigits(n):
    if n < 0: n *= (-1)
    suma = 0
    while(n > 0):
        suma += n % 10
        n = n // 10
    return suma

print(sumDigits(-32))





