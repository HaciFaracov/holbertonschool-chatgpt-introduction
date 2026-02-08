#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1   # Decrease n to avoid infinite loop
    return result

if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        raise ValueError("Number must be non-negative")
except ValueError as e:
    print("Error:", e)
    sys.exit(1)

f = factorial(num)
print(f)
