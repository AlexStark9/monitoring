def digit(data):
    """
    This function converts a string to a number
    :param data: str
    :return: int
    """
    data_digit = ''
    for c in data:
        if c.isdigit():
            data_digit += c
    return int(data_digit)
