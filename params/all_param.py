import os
import subprocess
import time
from converts import digit


def all_params(tr_id, result):
    """
    This function reads data from the device
    :param result: list
    :param tr_id: str
    :return: list
    """
    subprocess.run(["adb", tr_id, "root"])

    seconds = []
    temp = []
    temp_temp = []
    cpu = []
    cpu_idle = []
    available_mem = []
    free_mem = []
    uptime_0 = []
    uptime_1 = []
    uptime_2 = []
    counter = 0
    while True:
        cpu_info = subprocess.check_output(
            ["adb", tr_id, "shell", "cat", "/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq"])

        temp_1 = str(subprocess.run(["adb", tr_id, "shell", "cat", "/sys/class/thermal/thermal_zone0/temp"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL).stdout)

        temp_2 = str(subprocess.run(["adb", tr_id, "shell", "cat", "/sys/class/thermal/thermal_zone1/temp"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL).stdout)

        la = str(subprocess.run(["adb", tr_id, "shell", "uptime"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL).stdout)

        idle = str(subprocess.run(["adb", tr_id, "shell", "top", "|",
                                   "grep", "-m1", "idle", "|", "awk", "'{print $5}'"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL).stdout)

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

        uptime_0.append(float(la.split(" ")[11][0:4]))
        uptime_1.append(float(la.split(" ")[12][0:4]))
        uptime_2.append(float(la.split(" ")[13][0:4]))

        temp.append(int(temp_1.split("'")[1][0:5]) / 1000)
        temp_temp.append(int(temp_2.split("'")[1][0:5]) / 1000)

        cpu.append(int(cpu_info) / 1000000)

        idle = digit(idle)
        cpu_idle.append(idle)

        available = digit(mem_available) // 1000
        available_mem.append(available)

        free = digit(mem_free) // 1000
        free_mem.append(free)

        if os.path.exists("function_completed.txt"):
            os.remove("function_completed.txt")
            break

    result.append(temp)
    result.append(temp_temp)
    result.append(uptime_0)
    result.append(uptime_1)
    result.append(uptime_2)
    result.append(cpu_idle)
    result.append(cpu)
    result.append(available_mem)
    result.append(free_mem)
    result.append(seconds)

    return result
