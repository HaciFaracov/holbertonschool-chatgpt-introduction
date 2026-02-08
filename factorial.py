import sys
import math

# Allows printing results larger than 4,300 digits
sys.set_int_max_str_digits(0)

def main():
    """
    Entry point for calculating factorial via command line.
    Calculates n! = n * (n-1) * ... * 1
    """
    if len(sys.argv) < 2:
        print("Usage: python script.py <non-negative integer>")
        return

    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("Number must be non-negative.")
            
        # math.factorial is the gold standard for performance
        print(math.factorial(n))
        
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
