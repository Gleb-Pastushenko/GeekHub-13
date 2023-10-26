# Create a Python script that takes an age as input.
# If the age is less than 18 or greater than 120, raise a custom exception called InvalidAgeError.
# Handle the InvalidAgeError by displaying an appropriate error message.

class InvalidAgeError(Exception):
    def __init__(self, message='You can\'t be that age!'):
        super().__init__(message)


if __name__ == "__main__":
    age = None

    while not age:
        try:
            age = int(input('Enter your age:  '))
            if not 18 <= age <= 120:
                raise InvalidAgeError()
        except InvalidAgeError as err:
            print(age)
            age = None
            print(f'{err} Try again!')
        except ValueError:
            print('Wrong data! The age should be a positive integer value! Try again!')
        except Exception:
            print('Unknown error accured! Try again!')
        else:
            print('The input is successful! Thank you!')
 