import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # This ensures the loop eventually ends
    return result

# It's good practice to check if an argument was actually provided
if len(sys.argv) > 1:
    f = factorial(int(sys.argv[1]))
    print(f)
else:
    print("Please provide a number as a command-line argument.")
