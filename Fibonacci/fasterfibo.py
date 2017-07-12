def fibonacci(n):
    fib2less = 0
    fib1less = 1
    ans = 0
    i = 1
    while i < n:
        i += 1
        fib2less = fib1less
        fib1less = ans
        ans = fib1less + fib2less
    return ans

print(fibonacci(2))
