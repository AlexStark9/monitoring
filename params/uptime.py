import os
import subprocess
import time


def uptime(tr_id, result):
    """
    This function reads load averages data from the device
    :param result: list
    :param tr_id: str
    :return: list
    """
    subprocess.run(["adb", tr_id, "root"])

    seconds = []
    uptime_0 = []
    uptime_1 = []
    uptime_2 = []
    counter = 0

    while True:
        la = str(subprocess.run(["adb", tr_id, "shell", "uptime"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL).stdout)

        time.sleep(5)

        counter += 1
        seconds.append(counter)

        uptime_0.append(float(la.split(" ")[11][0:4]))
        uptime_1.append(float(la.split(" ")[12][0:4]))
        uptime_2.append(float(la.split(" ")[13][0:4]))

        if os.path.exists("function_completed.txt"):
            os.remove("function_completed.txt")
            break

    result.append(uptime_0)
    result.append(uptime_1)
    result.append(uptime_2)
    result.append(seconds)

    return result

