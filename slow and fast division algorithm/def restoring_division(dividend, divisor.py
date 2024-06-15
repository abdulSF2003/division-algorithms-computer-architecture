def restoring_division(dividend, divisor):
    """
    Performs restoring division algorithm.
    """
    quotient = 0
    remainder = dividend
    divisor <<= len(bin(dividend)) - 2  # Align divisor with dividend

    for _ in range(len(bin(dividend)) - 2):
        remainder <<= 1  # Shift left
        quotient <<= 1  # Shift quotient left
        if remainder >= divisor:
            remainder -= divisor
            quotient += 1

    return quotient, remainder

# Example usage
if __name__ == "__main__":
    dividend, divisor = 25, 3
    quotient, remainder = restoring_division(dividend, divisor)
    print(f"Dividend: {dividend}, Divisor: {divisor}")
    print(f"Quotient: {quotient}, Remainder: {remainder}")
