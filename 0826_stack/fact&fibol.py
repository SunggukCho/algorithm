def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(8))