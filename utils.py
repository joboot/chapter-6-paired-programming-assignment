"""
Utility code and validation code for output and data input from the user.
"""

__authors__ = "Jordan Booth and Mackenzie Eskey"
__version__ = "1.0"
__date__ = "11.2.2021"
__status__ = "Development"


def main():
    """
    Test each function to see if they work correctly
    :return: n/a
    """
    display_line()
    pos_num_int = get_positive_num('positive num int: ', 'int')
    pos_num_float = get_positive_num('positive num float: ', 'float')
    num_int = get_num('num int: ', 'int')
    num_float = get_num('num float: ', 'float')
    range_int = get_range('get range int(1-100): ', 0, 100, 'int')
    range_float = get_range('get range float(1-100): ', 0, 100, 'float')

    print(pos_num_int)
    print(pos_num_float)
    print(num_int)
    print(num_float)
    print(range_int)
    print(range_float)


def display_line():
    """
    Displays a line for program output
    :return: n/a
    """
    line_length = 60
    print('=' * line_length)


def get_num(prompt, data_type='int'):
    """
    Prompt user for input
    :param data_type: Data type to be converted to (int or float)
    :param prompt: Text to ask the user for input
    :return: Number input by the user
    """
    try:
        if data_type == 'int':
            number = int(input(prompt))
        else:
            number = float(input(prompt))

        return number
    except ValueError:
        print("Invalid input. Input must be a number.")


def get_yn(prompt):
    """
    Prompt user for input
    :param prompt: Text to ask the user for input
    :return: Answer input by the user
    """
    while True:
        user_input = input(prompt)
        user_input = user_input.lower()
        if user_input == 'y' or user_input == 'n' or user_input == 'yes' or user_input == 'no':
            return user_input
        else:
            print('Please enter y = Yes, n = No.')


def get_positive_num(prompt, data_type='int'):
    """
    Prompt user for input and ensure input number is positive
    :param data_type: Data type to be converted to (int or float)
    :param prompt: Text to ask the user for input
    :return: Number input by the user
    """

    while True:
        try:
            if data_type == 'int':
                number = int(input(prompt))
            else:
                number = float(input(prompt))
            if number > 0:
                return number
            else:
                print('Entry must be greater a positive number.')
        except ValueError:
            print("Invalid input. Input must be a number.")


def get_range(prompt, low, high, data_type='int'):
    """
    Prompt user for input and keep input number inside of a range
    :param data_type: Data type to be converted to (int or float)
    :param prompt: Text to ask the user for input
    :param low: Lowest possible number input
    :param high: Highest possible number input
    :return: Number input by the user
    """

    while True:
        try:
            if data_type == 'int':
                number = int(input(prompt))
            else:
                number = float(input(prompt))
            if low < number <= high:
                return number
            else:
                print("Entry must be greater than", low,
                      "and less than or equal to", high)
        except ValueError:
            print("Invalid input. Input must be a number.")


# runs this specific module's main
if __name__ == "__main__":
    main()
