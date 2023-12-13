def fibonacci_dynamic(n):
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Read the value of n from the console
n = int(input("Enter the Fibonacci number position: "))

result = fibonacci_dynamic(n)
print(f"The Fibonacci number at position {n} is {result}")
