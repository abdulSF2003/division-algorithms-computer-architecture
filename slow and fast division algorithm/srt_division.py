def srt_division(dividend, divisor):
    """
    Performs SRT division algorithm.
    """
    # Simplified implementation, more complex in actual hardware
    return dividend // divisor, dividend % divisor

# Example usage
if __name__ == "__main__":
    dividend, divisor = 25, 3
    quotient, remainder = srt_division(dividend, divisor)
    print(f"Dividend: {dividend}, Divisor: {divisor}")
    print(f"Quotient: {quotient}, Remainder: {remainder}")
