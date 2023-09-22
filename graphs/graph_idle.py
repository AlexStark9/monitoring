import pandas as pd
import matplotlib.pyplot as plt


def graph_idle(results):
    """
    The function builds idle graph
    :param results: List from the idle function
    :return: graph
    """
    freq = results[0]
    x = results[1]

    data = {
        'Время в секундах': x,
        'idle': freq
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
