import argparse


def arg_parse():
    parser = argparse.ArgumentParser(prog='monitoring.py',
                                     description='Утилита для мониторинга перформанса девайса на платформе Android.'
                                                 ' Для запуска утилиты вам нужно указать время в '
                                                 'секундах при помощи аргумента "-tm" или "--time"'
                                                 ' и выбрать конкретный агрумент для '
                                                 'мониторинга опреденного параметра '
                                                 '(выбор нескольких аргументов пока не доступен), '
                                                 'или указать параметр "-a" или "--all". '
                                                 'После завершения вам будут выведены графики для анализа '
                                                 'и min, avg, max значения в консоль. '
                                                 'Пока не адаптировано для Y4!'
                                     )

    parser.add_argument('-tm', '--time',
                        required=True,
                        type=int,
                        help="[ Время работы мониторинга в секундах ]",
                        action='store',
                        metavar=''
                        )

    parser.add_argument('-a',
                        '--all',
                        required=False,
                        help="[ Запустить мониторинг всех параметоров ]",
                        action="store_true"
                        )

    parser.add_argument('-m', '--memory',
                        required=False,
                        help="[ Запуск мониторинга свободной памяти ]",
                        action="store_true"
                        )

    parser.add_argument('-i', '--idle',
                        required=False,
                        help="[ Запуск мониторинга idle из утилиты top ]",
                        action="store_true"
                        )

    parser.add_argument('-t', '--temp',
                        required=False,
                        help="[ Запуск мониторинга температуры ]",
                        action="store_true"
                        )

    parser.add_argument('-f', '--freq',
                        required=False,
                        help="[ Запуск мотиторинга частоты CPU ]",
                        action="store_true"
                        )

    parser.add_argument('-u', '--uptime',
                        required=False,
                        help="[ Запуск мотиторинга load averages ]",
                        action="store_true"
                        )

    parser.add_argument('-v', '--version',
                        action='version',
                        version='Версия 1.0'
                        )

    return parser.parse_args()
