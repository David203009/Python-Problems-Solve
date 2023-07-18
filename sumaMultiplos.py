# Your Job
# Find the sum of all multiples of n below m

# Keep in Mind
# n and m are natural numbers (positive integers)
# m is excluded from the multiples

def multiplos(n, m):
    if n < 0 or m < 0:
        return "Invalid"
    res = sum(x for x in range(m+1) if x % n == 0)
    return(res)

print(multiplos(4,-7))