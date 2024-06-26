def multiply_digits(num):
    result = 1
    for digit in str(num):
        result *= int(digit)
    return result

def digit_multiplication_count(num):
    count = 0
    while num >= 10:
        num = multiply_digits(num)
        count += 1
    return count

def main():
    numbers_processed = 0
    seed = 277777788888899 # int(input("Enter a number: "))
    for number in range(seed * 1, seed * 9):
        repeats = digit_multiplication_count(number)
        if repeats >= 11:
            print(f"So far processed {numbers_processed} out of which - the number '{number}', the number of repeats until a single digit: {repeats}")
        numbers_processed += 1

if __name__ == "__main__":
    main()
