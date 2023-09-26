import time


def monitoring_time(time_sec):
    """
    This function acts as a timer
    :return: bool
    """
    print('Start timer')
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        time_sec = time_sec
        if elapsed_time >= time_sec:
            with open("function_completed.txt", "w") as signal_file:
                signal_file.write("Function completed")
            return False, print('Timer stopped')


def digit(data):
    """
    This function converts a string to a number
    :return: int
    """
    data_digit = ''
    for i in data:
        if i.isdigit():
            data_digit += i
    return int(data_digit)
