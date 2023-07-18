# Create a function named divisors/Divisors 
# that takes an integer n > 1 and returns an array with all of the integer
#  divisors(except for 1 and the number itself), from smallest to largest. 
#  If the number is prime return the string '(integer) is prime'.
 
def divisors(integer):
    arr = [x for x in range(2,integer) if integer % x == 0]
    if arr == []:
        return f"{integer} is prime"
    return arr

print(divisors(12))