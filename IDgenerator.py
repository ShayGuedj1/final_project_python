class NumberGenerator:
    def __init__(self):
        self.generated_numbers = None

    def generate_numbers(self):
        valid_range = range(100000000, 1000000000)

        while True:
            user_input = input("Please enter a number between 100000000 and 999999999: ")
            try:
                num = int(user_input)
                if num in valid_range:
                    digits = [int(digit) for digit in str(num)]
                    if len(digits) == 9:
                        new_numbers = []
                        for i in range(10):
                            new_num = int(''.join(map(str, digits)))
                            new_numbers.append(new_num)
                            digits[i % 9], digits[(i + 2) % 9] = digits[(i + 2) % 9], digits[i % 9]

                        # Store the generated numbers in the instance variable
                        self.generated_numbers = new_numbers
                        return
                    else:
                        print("The number must have exactly 9 digits. Please try again.")
                else:
                    print("The number is not within the valid range. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def print_generated_numbers(self):
        if self.generated_numbers is not None:
            print("Generated Numbers:")
            for num in self.generated_numbers:
                print(f"{num:09}")
        else:
            print("Numbers have not been generated yet. Call generate_numbers() first.")


# Create an instance of the NumberGenerator class
number_generator = NumberGenerator()

# Generate numbers and print them
number_generator.generate_numbers()
number_generator.print_generated_numbers()
