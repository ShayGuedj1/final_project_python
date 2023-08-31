class NumberIterator:
    def __init__(self):
        self.valid_range = range(100000000, 1000000000)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            user_input = input("Please enter a number between 100000000 and 999999999: ")

            try:
                num = int(user_input)
                if num in self.valid_range:
                    digits = [int(digit) for digit in str(num)]
                    if len(digits) == 9:
                        break
                    else:
                        print("The number must have exactly 9 digits. Please try again.")
                else:
                    print("The number is not within the valid range. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        new_numbers = []
        for i in range(10):
            new_num = int(''.join(map(str, digits)))
            new_numbers.append(new_num)
            digits[i % 9], digits[(i + 1) % 9] = digits[(i + 1) % 9], digits[i % 9]

        return new_numbers

# Create an instance of the iterator
iterator = NumberIterator()

# Get and print the next set of numbers
next_numbers = next(iterator)
print("Generated Numbers:")
for num in next_numbers:
    print(f"{num:09}")  # Print numbers with leading zeros if necessary
