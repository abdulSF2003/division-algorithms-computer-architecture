def non_restoring_division(dividend, divisor):
    """
    Performs non-restoring division algorithm.
    """
    quotient = 0
    remainder = dividend
    divisor <<= len(bin(dividend)) - 2  # Align divisor with dividend

    for _ in range(len(bin(dividend)) - 2):
        remainder <<= 1  # Shift left
        quotient <<= 1  # Shift quotient left
        if remainder >= 0:
            remainder -= divisor
            quotient += 1
        else:
            remainder += divisor

    if remainder < 0:
        remainder += divisor

    return quotient, remainder

# Example usage
if __name__ == "__main__":
    dividend, divisor = 25, 3
    quotient, remainder = non_restoring_division(dividend, divisor)
    print(f"Dividend: {dividend}, Divisor: {divisor}")
    print(f"Quotient: {quotient}, Remainder: {remainder}")
