def newton_raphson_division(dividend, divisor, iterations=5):
    """
    Performs Newton-Raphson division algorithm.
    """
    x = 1.0 / divisor  # Initial guess
    for _ in range(iterations):
        x = x * (2.0 - divisor * x)
    quotient = int(dividend * x)
    remainder = dividend - quotient * divisor
    return quotient, remainder

# Example usage
if __name__ == "__main__":
    dividend, divisor = 25, 3
    quotient, remainder = newton_raphson_division(dividend, divisor)
    print(f"Dividend: {dividend}, Divisor: {divisor}")
    print(f"Quotient: {quotient}, Remainder: {remainder}")
