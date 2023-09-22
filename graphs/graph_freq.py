import pandas as pd
import matplotlib.pyplot as plt


def graph_freq(results):
    """
    The function builds freq graph
    :param results: List from the freq function
    :return: graph
    """
    freq = results[0]
    x = results[1]

    data = {
        'Время в секундах': x,
        'Частота CPU в ГГц': freq
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
