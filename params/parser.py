import os
import subprocess
import time
from helpers import *


class Parser:
    def __init__(self, tr_id, result):
        self.tr_id = tr_id
        self.result = result

        subprocess.run(["adb", tr_id, "root"])

        self.seconds = []
        self.temp_zone0 = []
        self.temp_zone1 = []
        self.cpu = []
        self.cpu_idle = []
        self.available_mem = []
        self.free_mem = []
        self.uptime_0 = []
        self.uptime_1 = []
        self.uptime_2 = []
        self.counter = 0

    def all_params(self):
        """
        This function reads data from the device
        :return: list
        """
        while True:
            response = requests(self.tr_id)

            time.sleep(5)

            self.counter += 1
            self.seconds.append(self.counter)
            result = transformation(
                la=response[2],
                temp_1=response[0],
                temp_2=response[1],
                cpu_info=response[6],
                idle=response[3],
                mem_available=response[4],
                mem_free=response[5]
            )

            self.uptime_0.append(result[0])
            self.uptime_1.append(result[1])
            self.uptime_2.append(result[2])
            self.temp_zone0.append(result[3])
            self.temp_zone1.append(result[4])
            self.cpu.append(result[5])
            self.cpu_idle.append(result[6])
            self.available_mem.append(result[7])
            self.free_mem.append(result[8])

            if os.path.exists("function_completed.txt"):
                os.remove("function_completed.txt")
                break

        self.result.append(self.temp_zone0)
        self.result.append(self.temp_zone1)
        self.result.append(self.uptime_0)
        self.result.append(self.uptime_1)
        self.result.append(self.uptime_2)
        self.result.append(self.cpu_idle)
        self.result.append(self.cpu)
        self.result.append(self.available_mem)
        self.result.append(self.free_mem)
        self.result.append(self.seconds)

        return self.result

    def freq(self):
        """
        This function reads CPU frequency data from the device
        :return: list
        """
        while True:
            response = requests(self.tr_id)

            time.sleep(5)

            self.counter += 1
            self.seconds.append(self.counter)
            result = transformation(cpu_info=response)
            self.cpu.append(result[0])

            if os.path.exists("function_completed.txt"):
                os.remove("function_completed.txt")
                break

        self.result.append(self.cpu)
        self.result.append(self.seconds)

        return self.result

    def idle(self):
        """
        This function reads data from the device
        :return: list
        """
        while True:
            response = requests(self.tr_id)

            time.sleep(5)

            self.counter += 1
            self.seconds.append(self.counter)
            result = transformation(idle=response)
            self.cpu_idle.append(result[0])

            if os.path.exists("function_completed.txt"):
                os.remove("function_completed.txt")
                break

        self.result.append(self.cpu_idle)
        self.result.append(self.seconds)

        return self.result

    def memory(self):
        """
        This function reads free RAM data from the device
        :return: list
        """
        while True:
            response = requests(self.tr_id)

            time.sleep(5)

            self.counter += 1
            self.seconds.append(self.counter)
            result = transformation(mem_available=response[0], mem_free=response[1])
            self.available_mem.append(result[0])
            self.free_mem.append(result[1])

            if os.path.exists("function_completed.txt"):
                os.remove("function_completed.txt")
                break

        self.result.append(self.available_mem)
        self.result.append(self.free_mem)
        self.result.append(self.seconds)

        return self.result

    def temp(self):
        """
        This function reads temperature data from the device
        :return: list
        """
        while True:
            response = requests(self.tr_id)

            time.sleep(5)

            self.counter += 1
            self.seconds.append(self.counter)
            result = transformation(temp_1=response[0], temp_2=response[1])
            self.temp_zone0.append(result[0])
            self.temp_zone1.append(result[1])

            if os.path.exists("function_completed.txt"):
                os.remove("function_completed.txt")
                break

        self.result.append(self.temp_zone0)
        self.result.append(self.temp_zone1)
        self.result.append(self.seconds)

        return self.result

    def uptime(self):
        """
        This function reads load averages data from the device
        :return: list
        """
        while True:
            response = requests(self.tr_id)

            time.sleep(5)

            self.counter += 1
            self.seconds.append(self.counter)
            result = transformation(la=response)
            self.uptime_0.append(result[0])
            self.uptime_1.append(result[1])
            self.uptime_2.append(result[2])

            if os.path.exists("function_completed.txt"):
                os.remove("function_completed.txt")
                break

        self.result.append(self.uptime_0)
        self.result.append(self.uptime_1)
        self.result.append(self.uptime_2)
        self.result.append(self.uptime_2)
        self.result.append(self.seconds)

        return self.result
