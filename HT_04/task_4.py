# Write a Python program that demonstrates exception chaining.
# Create a custom exception class called CustomError and another called SpecificError.
# In your program (could contain any logic you want), raise a SpecificError,
# and then catch it in a try/except block, re-raise it as a CustomError with the original exception as the cause.
# Display both the custom error message and the original exception message.


class CustomError(Exception):
    def __init__(self, message="The CustomError", *args):
       super().__init__(message, *args)


class SpecificError(Exception):
    def __init__(self, message="The SpecificError", *args):
        super().__init__(message, *args)


if __name__ == "__main__":
    try:
        print('Raising the SpecificError...')
        raise SpecificError()
    except SpecificError as err:
        try:
            print('Catching the SpecificError...')
            print(f'Catched error: {err}')
            print('Reraising the original error...')
            raise CustomError("Rerised error!", err)
        except CustomError as err:
            print(f'The original error:  {err}')
            print('This is the custom error Message!')
    except:
        print('Unknown error occured!')