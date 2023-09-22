import time


def monitoring_time(time_sec):
    print('Start timer')
    start_time = time.time()
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= time_sec:
            with open("function_completed.txt", "w") as signal_file:
                signal_file.write("Function completed")
            return False, print('Timer stopped')
