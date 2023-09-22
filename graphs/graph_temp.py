import pandas as pd
import matplotlib.pyplot as plt


def graph_temp(results):
    """
    The function builds temp graph
    :param results: List from the temp function
    :return: graph
    """
    temp_0 = results[0]
    temp_1 = results[1]
    x = results[2]

    data = {
        'Время в секундах': x,
        'Термал зона 0': temp_0,
        'Термал зона 1': temp_1
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
