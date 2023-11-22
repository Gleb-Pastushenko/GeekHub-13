# 1. Створити клас Calc, який буде мати атребут last_result та 4 методи.
#    Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання, множення, ділення.
# - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення.
# - Якщо використати один з методів - last_result повенен повернути результат виконання ПОПЕРЕДНЬОГО методу.
#     Example:
#     last_result --> None
#     1 + 1
#     last_result --> None
#     2 * 3
#     last_result --> 2
#     3 * 4
#     last_result --> 6
#     ...
# - Додати документування в клас (можете почитати цю статтю:
# https://realpython.com/documenting-python-code/ )


class Calc:
    """
    A class used for making basic math operations:
    sum, difference, multiplying, division

    Attributes
    ----------
    last_result : int, float
        the result of the last operation (None after instance creation)

    Methods
    -------
    get_sum(a, b)
        calculates the sum of a and b and puts the result into the last_result attribute

    get_difference(a, b)
        calculates the difference of a and b and puts the result into the last_result attribute

    get_product(a, b)
        calculates the product of a and b and puts the result into the last_result attribute

    get_quotient(a, b)
        devides a by b and puts the result into the last_result attribute

    """

    def __init__(self):
        """
        Creates a last_result attribute and initialize is with None value
        """
        self.last_result = None

    def get_sum(self, a, b):
        """
        Calculates sum of a and b and assign it to last_result attribute

        Parameters
        ----------
        a : int, float
            first term

        b: int, float
            second term
        """
        self.last_result = a + b

    def get_difference(self, a, b):
        """
        Calculates difference of a and b and assign it to last_result attribute

        Parameters
        ----------
        a : int, float
            minuend

        b: int, float
            subtrahend
        """
        self.last_result = a - b

    def get_product(self, a, b):
        """
        Calculates product of a and b and assign it to last_result attribute

        Parameters
        ----------
        a : int, float
            multiplicand

        b: int, float
            multiplier
        """
        self.last_result = a * b

    def get_quotient(self, a, b):
        """
        Calculates quotient of a and b and assign it to last_result attribute

        Parameters
        ----------
        a : int, float
            dividend

        b: int, float
            divisor
        """
        self.last_result = a / b


if __name__ == "__main__":
    calc = Calc()
    print(calc.last_result)

    calc.get_sum(10, 12)
    print(calc.last_result)

    calc.get_product(15, 4)
    print(calc.last_result)
