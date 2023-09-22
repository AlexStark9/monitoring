import subprocess
import time
import os


def freq(tr_id, result):
    """
    This function reads CPU frequency data from the device
    :param result: list
    :param tr_id: str
    :return: list
    """
    subprocess.run(["adb", tr_id, "root"])

    seconds = []
    cpu = []
    counter = 0

    while True:
        cpu_info = subprocess.check_output(
            ["adb", tr_id, "shell", "cat", "/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq"])

        time.sleep(5)

        counter += 1
        seconds.append(counter)

        cpu.append(int(cpu_info) / 1000000)

        if os.path.exists("function_completed.txt"):
            os.remove("function_completed.txt")
            break

    result.append(cpu)
    result.append(seconds)

    return result
