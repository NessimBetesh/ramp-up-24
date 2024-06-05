def factorial_loops(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("EROOR. Please enter a non-negative integer.")
else:
    factorial_with_loop = factorial_loops(number)
    print(f"Factorial of {number} using loops: {factorial_with_loop}")

    factorial_with_recursion = factorial_recursive(number)
    print(f"Factorial of {number} using recursion: {factorial_with_recursion}")