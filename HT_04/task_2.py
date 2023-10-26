# Create a custom exception class called NegativeValueError.
# Write a Python program that takes an integer as input and raises the NegativeValueError if the input is negative.
# Handle this custom exception with a try/except block and display an error message.


class NegativeValueError(Exception):
    def __init__(self, message="The age can't be negative!"):
        super().__init__(message)


if __name__ == "__main__":
    age = None

    while not age:
        try:
            age = int(input("Enter your age:  "))
            if age < 0:
                raise NegativeValueError()
        except NegativeValueError as error:
            age = None
            print(f'{error} Try again!')
        except ValueError:
            print('Wrong data! The age should be a positive integer value! Try again!')
        except Exception:
            print('Unknown error accured! Try again!')
        else:
            print('The input is successful! Thank you!')
