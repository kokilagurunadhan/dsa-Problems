def is_perfect(num):
    """Return whether num equals the sum of its proper divisors."""
    if num <= 1:
        return False

    divisor_sum = sum(
        divisor for divisor in range(1, num // 2 + 1) if num % divisor == 0
    )
    return divisor_sum == num


if __name__ == "__main__":
    input_number = int(input("Enter a number to check: "))

    if is_perfect(input_number):
        print(f"{input_number} is a perfect number.")
    else:
        print(f"{input_number} is NOT a perfect number.")
