import pandas as pd
import matplotlib.pyplot as plt


def graph_all_params(results):
    """The function builds graphs
    :param results: List from the all_params function
    :return: graphs
    """
    temp_0 = results[0]
    temp_1 = results[1]
    value_1 = results[2]
    value_2 = results[3]
    value_3 = results[4]
    cpu_i = results[5]
    freq = results[6]
    m_available = results[7]
    m_free = results[8]
    x = results[9]

    data = {
        'Время в секундах': x,
        'Термал зона 0': temp_0,
        'Термал зона 1': temp_1,
        'Частота CPU в ГГц': freq,
        'idle': cpu_i,
        'MemFree': m_free,
        'MemAvailable': m_available,
        'LoadAverages_1': value_1,
        'LoadAverages_2': value_2,
        'LoadAverages_3': value_3
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
