import pandas as pd
import matplotlib.pyplot as plt


def graph_uptime(results):
    """
    The function builds Load Averages graphs
    :param results: List from the uptime function
    :return: graphs
    """
    value_1 = results[0]
    value_2 = results[1]
    value_3 = results[2]
    x = results[3]

    data = {
        'Время в секундах': x,
        'LoadAverages_1': value_1,
        'LoadAverages_2': value_2,
        'LoadAverages_3': value_3
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
