import pandas as pd
import matplotlib.pyplot as plt


class Plotting:
    def __init__(self, results):
        self.results = results

    def graph_all_params(self):
        """
        The function builds graph
        :return: graphs all params
        """
        value_0 = self.results[0]
        value_1 = self.results[1]
        value_2 = self.results[2]
        value_3 = self.results[3]
        value_4 = self.results[4]
        value_5 = self.results[5]
        value_6 = self.results[6]
        value_7 = self.results[7]
        value_8 = self.results[8]
        value_9 = self.results[9]

        data = {
            'Термал зона 0': value_0,
            'Термал зона 1': value_1,
            'LoadAverages_1': value_2,
            'LoadAverages_2': value_3,
            'LoadAverages_3': value_4,
            'idle': value_5,
            'Частота CPU в ГГц': value_6,
            'MemAvailable': value_7,
            'MemFree': value_8,
            'Время в секундах': value_9
        }
        df = pd.DataFrame(data)

        df.plot(x='Время в секундах',
                y=['Термал зона 0', 'Термал зона 1'],
                title='График температуры')

        print()
        print("thermal_zone0 / thermal_zone0:",
              f"Мин.значение = {df['Термал зона 0'].min()} / {df['Термал зона 1'].min()}",
              f"Сред.значение =  {df['Термал зона 0'].mean()} / {df['Термал зона 1'].mean()}",
              f"Макс.значение = {df['Термал зона 0'].max()} / {df['Термал зона 1'].max()}",
              sep='\n')
        print()

        df.plot(x='Время в секундах',
                y='Частота CPU в ГГц',
                title='График частоты CPU')

        print("freq:",
              f"Мин.значение = {df['Частота CPU в ГГц'].min()}",
              f"Сред.значение =  {df['Частота CPU в ГГц'].mean()}",
              f"Макс.значение = {df['Частота CPU в ГГц'].max()}",
              sep='\n')
        print()

        df.plot(x='Время в секундах',
                y=['MemFree', 'MemAvailable'],
                title='График свободной памяти в mb')

        print("MemFree / MemAvailable:",
              f"Мин.значение = {df['MemFree'].min()} / {df['MemAvailable'].min()}",
              f"Сред.значение =  {df['MemFree'].mean()} / {df['MemAvailable'].mean()}",
              f"Макс.значение = {df['MemFree'].max()} / {df['MemAvailable'].max()}",
              sep='\n')
        print()

        df.plot(x='Время в секундах',
                y='idle',
                title='График свободной времени CPU в %:')

        print("idle:",
              f"Мин.значение = {df['idle'].min()}",
              f"Сред.значение =  {df['idle'].mean()}",
              f"Макс.значение = {df['idle'].max()}",
              sep='\n')
        print()

        df.plot(x='Время в секундах',
                y=['LoadAverages_1', 'LoadAverages_2', 'LoadAverages_3'],
                title='График средней загрузки')

        print("LoadAverages_1 / LoadAverages_2 / LoadAverages_3:",
              f"Мин.значение = {df['LoadAverages_1'].min()} / {df['LoadAverages_2'].min()} / {df['LoadAverages_3'].min()}",
              f"Сред.значение =  {df['LoadAverages_1'].mean()} / {df['LoadAverages_2'].mean()} / "
              f"{df['LoadAverages_3'].mean()}",
              f"Макс.значение = {df['LoadAverages_1'].max()} / {df['LoadAverages_2'].max()} / {df['LoadAverages_3'].max()}",
              sep='\n')

        return plt.show(), quit()

    def graph_freq(self):
        """
        The function builds freq graph
        :return: frequency graph
        """
        value_0 = self.results[0]
        value_1 = self.results[1]

        data = {
            'Частота CPU в ГГц': value_0,
            'Время в секундах': value_1
        }
        df = pd.DataFrame(data)

        df.plot(x='Время в секундах',
                y='Частота CPU в ГГц',
                title='График частоты CPU'
                )

        print()
        print("freq:",
              f"Мин.значение = {df['Частота CPU в ГГц'].min()}",
              f"Сред.значение =  {df['Частота CPU в ГГц'].mean()}",
              f"Макс.значение = {df['Частота CPU в ГГц'].max()}",
              sep='\n')

        return plt.show(), quit()

    def graph_idle(self):
        """
        The function builds idle graph
        :return: CPU free time graph
        """
        value_0 = self.results[0]
        value_1 = self.results[1]

        data = {
            'idle': value_0,
            'Время в секундах': value_1
        }
        df = pd.DataFrame(data)

        df.plot(x='Время в секундах',
                y='idle',
                title='График свободного времени CPU в %'
                )

        print()
        print("idle:",
              f"Мин.значение = {df['idle'].min()}",
              f"Сред.значение =  {df['idle'].mean()}",
              f"Макс.значение = {df['idle'].max()}",
              sep='\n')

        return plt.show(), quit()

    def graph_memory(self):
        """
        The function builds memory graph
        :return: free RAM graph
        """
        value_0 = self.results[0]
        value_1 = self.results[1]
        value_2 = self.results[2]

        data = {
            'MemAvailable': value_0,
            'MemFree': value_1,
            'Время в секундах': value_2
        }
        df = pd.DataFrame(data)

        df.plot(x='Время в секундах',
                y=['MemFree', 'MemAvailable'],
                title='График свободной памяти в mb'
                )

        print()
        print("MemFree / MemAvailable:",
              f"Мин.значение = {df['MemFree'].min()} / {df['MemAvailable'].min()}",
              f"Сред.значение =  {df['MemFree'].mean()} / {df['MemAvailable'].mean()}",
              f"Макс.значение = {df['MemFree'].max()} / {df['MemAvailable'].max()}",
              sep='\n')

        return plt.show(), quit()

    def graph_temp(self):
        """
        The function builds temp graph
        :return: temperature graph
        """
        value_0 = self.results[0]
        value_1 = self.results[1]
        value_2 = self.results[2]

        data = {
            'Термал зона 0': value_0,
            'Термал зона 1': value_1,
            'Время в секундах': value_2
        }
        df = pd.DataFrame(data)

        df.plot(x='Время в секундах',
                y=['Термал зона 0', 'Термал зона 1'],
                title='График температуры'
                )

        print()
        print("thermal_zone0 / thermal_zone0:",
              f"Мин.значение = {df['Термал зона 0'].min()} / {df['Термал зона 1'].min()}",
              f"Сред.значение =  {df['Термал зона 0'].mean()} / {df['Термал зона 1'].mean()}",
              f"Макс.значение = {df['Термал зона 0'].max()} / {df['Термал зона 1'].max()}",
              sep='\n')

        return plt.show(), quit()

    def graph_uptime(self):
        """
        The function builds Load Averages graphs
        :return: Load average graph
        """
        value_0 = self.results[0]
        value_1 = self.results[1]
        value_2 = self.results[2]
        value_3 = self.results[3]

        data = {
            'LoadAverages_1': value_0,
            'LoadAverages_2': value_1,
            'LoadAverages_3': value_2,
            'Время в секундах': value_3
        }
        df = pd.DataFrame(data)

        df.plot(x='Время в секундах',
                y=['LoadAverages_1', 'LoadAverages_2', 'LoadAverages_3'],
                title='График средней загрузки'
                )

        print()
        print("LoadAverages_1 / LoadAverages_2 / LoadAverages_3:",
              f"Мин.значение = {df['LoadAverages_1'].min()} / {df['LoadAverages_2'].min()} / {df['LoadAverages_3'].min()}",
              f"Сред.значение =  {df['LoadAverages_1'].mean()} / {df['LoadAverages_2'].mean()} / "
              f"{df['LoadAverages_3'].mean()}",
              f"Макс.значение = {df['LoadAverages_1'].max()} / {df['LoadAverages_2'].max()} / {df['LoadAverages_3'].max()}",
              sep='\n')

        return plt.show(), quit()
