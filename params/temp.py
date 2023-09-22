import os
import subprocess
import time


def temp(tr_id, result):
    """
    This function reads temperature data from the device
    :param result: list
    :param tr_id: str
    :return: list
    """
    subprocess.run(["adb", tr_id, "root"])

    seconds = []
    temp = []
    temp_temp = []
    counter = 0

    while True:
        temp_1 = str(subprocess.run(["adb", tr_id, "shell", "cat", "/sys/class/thermal/thermal_zone0/temp"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL).stdout)

        temp_2 = str(subprocess.run(["adb", tr_id, "shell", "cat", "/sys/class/thermal/thermal_zone1/temp"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL).stdout)

        time.sleep(5)

        counter += 1
        seconds.append(counter)

        temp.append(int(temp_1.split("'")[1][0:5]) / 1000)
        temp_temp.append(int(temp_2.split("'")[1][0:5]) / 1000)

        if os.path.exists("function_completed.txt"):
            os.remove("function_completed.txt")
            break

    result.append(temp)
    result.append(temp_temp)
    result.append(seconds)

    return result

