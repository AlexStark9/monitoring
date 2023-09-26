from helpers import *


def transformation(la=None, temp_1=None, temp_2=None, cpu_info=None, idle=None, mem_available=None, mem_free=None):
    """
    This function converts the data it receives
    :param la:str
    :param temp_1:str
    :param temp_2:str
    :param cpu_info:str
    :param idle:str
    :param mem_available:str
    :param mem_free:str
    :return:list
    """

    result = []

    temp = 0
    temp_temp = 0
    cpu = 0
    cpu_idle = 0
    available_mem = 0
    free_mem = 0
    uptime_0 = 0
    uptime_1 = 0
    uptime_2 = 0

    if la is not None:
        uptime_0 += (float(la.split(" ")[11][0:4]))
        uptime_1 += (float(la.split(" ")[12][0:4]))
        uptime_2 += (float(la.split(" ")[13][0:4]))
        result.append(uptime_0)
        result.append(uptime_1)
        result.append(uptime_2)

    if temp_1 is not None:
        temp += (int(temp_1.split("'")[1][0:5]) / 1000)
        result.append(temp)

    if temp_2 is not None:
        temp_temp += (int(temp_2.split("'")[1][0:5]) / 1000)
        result.append(temp_temp)

    if cpu_info is not None:
        cpu += (int(cpu_info) / 1000000)
        result.append(cpu)

    if idle is not None:
        cpu_idle += digit(idle)
        result.append(cpu_idle)

    if mem_available is not None:
        available = digit(mem_available) // 1000
        available_mem += available
        result.append(available_mem)

    if mem_free is not None:
        free = digit(mem_free) // 1000
        free_mem += free
        result.append(free_mem)

    return result
