import subprocess
from args import arg_parse


def requests(tr_id):
    args = arg_parse()
    if args.all:
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
        cpu_info = subprocess.check_output(
            ["adb", tr_id, "shell", "cat", "/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq"])

        return temp_1, temp_2, la, idle, mem_available, mem_free, cpu_info
    elif args.freq:
        cpu_info = subprocess.check_output(
            ["adb", tr_id, "shell", "cat", "/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq"])

        return cpu_info
    elif args.idle:
        idle = str(subprocess.run(["adb", tr_id, "shell", "top", "|",
                                   "grep", "-m1", "idle", "|", "awk", "'{print $5}'"],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL).stdout)
        return idle
    elif args.memory:
        mem_available = str(subprocess.run(["adb", tr_id, "shell", "cat", "proc/meminfo",
                                            "|", "grep", "'MemAvailable'", "|", "awk", "'{print $2}'"],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.DEVNULL).stdout)
        mem_free = str(subprocess.run(["adb", tr_id, "shell", "cat", "proc/meminfo",
                                       "|", "grep", "'MemFree'", "|", "awk", "'{print $2}'"],
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.DEVNULL).stdout)
        return mem_available, mem_free
    elif args.temp:
        temp_1 = str(subprocess.run(["adb", tr_id, "shell", "cat", "/sys/class/thermal/thermal_zone0/temp"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL).stdout)
        temp_2 = str(subprocess.run(["adb", tr_id, "shell", "cat", "/sys/class/thermal/thermal_zone1/temp"],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.DEVNULL).stdout)
        return temp_1, temp_2
    elif args.uptime:
        la = str(subprocess.run(["adb", tr_id, "shell", "uptime"],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL).stdout)
        return la
