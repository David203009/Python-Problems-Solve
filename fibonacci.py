def fib(a,b,n):
    if n < 10:
        print(a, end="-")
        fib(b,a+b,n+1)
    else:
        print(a)

fib(0,1,1)
