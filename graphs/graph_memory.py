import pandas as pd
import matplotlib.pyplot as plt


def graph_memory(results):
    """
    The function builds memory graph
    :param results: List from the memory function
    :return: graphs
    """
    m_available = results[0]
    m_free = results[1]
    x = results[2]

    data = {
        'Время в секундах': x,
        'MemFree': m_free,
        'MemAvailable': m_available
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
