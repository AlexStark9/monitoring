import os
import subprocess
import time
from converts import digit


def memory(tr_id, result):
    """
    This function reads free RAM data from the device
    :param result: list
    :param tr_id: str
    :return: list
    """
    subprocess.run(["adb", tr_id, "root"])

    seconds = []
    available_mem = []
    free_mem = []
    counter = 0

    while True:
        mem_available = str(subprocess.run(["adb", tr_id, "shell", "cat", "proc/meminfo",
                                            "|", "grep", "'MemAvailable'", "|", "awk", "'{print $2}'"],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.DEVNULL).stdout)

        mem_free = str(subprocess.run(["adb", tr_id, "shell", "cat", "proc/meminfo",
                                       "|", "grep", "'MemFree'", "|", "awk", "'{print $2}'"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.DEVNULL).stdout)

        time.sleep(5)

        counter += 1
        seconds.append(counter)

        available = digit(mem_available) // 1000
        available_mem.append(available)

        free = digit(mem_free) // 1000
        free_mem.append(free)

        if os.path.exists("function_completed.txt"):
            os.remove("function_completed.txt")
            break

    result.append(available_mem)
    result.append(free_mem)
    result.append(seconds)

    return result
