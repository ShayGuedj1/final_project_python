class NumberIterator:
    def __init__(self):
        self.valid_range = range(100000000, 1000000000)  # The constructor (__init__) initializes the valid_range attribute with a range of numbers from 100,000,000 to 999,999,999.

    def __iter__(self):
        return self  # This method is required for an iterator and returns the iterator object itself (in this case, self).

    def __next__(self):  # This method is required for an iterator and is responsible for generating the next set of numbers.
        while True:
            user_input = input("Please enter a number between 100000000 and 999999999: ")  # It enters an infinite loop, prompting the user to input a number between 100,000,000 and 999,999,999.

            '''
                The input is then converted to an integer, and the following checks are performed:

                If the input number is within the valid range, the code proceeds to process the number further.
                If the input number is not within the valid range, an error message is displayed.
                If the input is not a valid integer, an error message is displayed.
                If a valid input number is provided, the digits of the number are extracted and stored in the digits list.
            '''

            try:  # The loop breaks when a valid number with exactly 9 digits is entered.
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
        ''' 
            In each iteration, a new number is generated using the digits extracted earlier.

            The new number is created by swapping the positions of two adjacent digits in a circular manner.
            The generated new numbers are stored in the new_numbers list.
            The new_numbers list containing the generated numbers is returned.
        '''
        for i in range(10):  # The loop continues with the valid input number and iterates 10 times.
            new_num = int(''.join(map(str, digits)))
            new_numbers.append(new_num)
            digits[i % 9], digits[(i + 2) % 9] = digits[(i + 2) % 9], digits[i % 9]

        return new_numbers

# Create an instance of the iterator
iterator = NumberIterator()

# Get and print the next set of numbers
next_numbers = next(iterator)
print("Generated Numbers:")
for num in next_numbers:
    print(f"{num:09}")  # Print numbers with leading zeros if necessary
