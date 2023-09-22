import os
import subprocess
import time
from converts import digit


def idle(tr_id, result):
    """
    This function reads data from the device
    :param result: list
    :param tr_id: str
    :return: list
    """
    subprocess.run(["adb", tr_id, "root"])

    seconds = []
    cpu_idle = []
    counter = 0

    while True:
        idle = str(subprocess.run(["adb", tr_id, "shell", "top", "|",
                                   "grep", "-m1", "idle", "|", "awk", "'{print $5}'"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL).stdout)

        time.sleep(5)

        counter += 1
        seconds.append(counter)

        idle = digit(idle)
        cpu_idle.append(idle)

        if os.path.exists("function_completed.txt"):
            os.remove("function_completed.txt")
            break

    result.append(idle)
    result.append(seconds)

    return result
