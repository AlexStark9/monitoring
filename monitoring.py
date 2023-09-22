#!/usr/bin/env python3
import multiprocessing
from params import *
from graphs import *
from args import arg_parse
from checking_device import device_selection
from time_checkig import monitoring_time


def main():
    args = arg_parse()
    time_sec = args.time

    tr_id = device_selection()

    if args.all:
        print(f'Запущен мониторинг всех парметров. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec,))
        target2 = multiprocessing.Process(target=all_params, args=(tr_id, result,))

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        graph_all_params(results)
    elif args.freq:
        print(f'Запущен мониторинг частоты CPU. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec,))
        target2 = multiprocessing.Process(target=freq, args=(tr_id, result,))

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        graph_freq(results)
    elif args.idle:
        print(f'Запущен мониторинг idle. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec,))
        target2 = multiprocessing.Process(target=idle, args=(tr_id, result,))

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        graph_idle(results)
    elif args.memory:
        print(f'Запущен мониторинг свободной RAM. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec,))
        target2 = multiprocessing.Process(target=memory, args=(tr_id, result,))

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()
        print(results)
        graph_memory(results)
    elif args.temp:
        print(f'Запущен мониторинг тумпературы. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec,))
        target2 = multiprocessing.Process(target=temp, args=(tr_id, result,))

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        graph_temp(results)
    elif args.uptime:
        print(f'Запущен мониторинг load averages. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec,))
        target2 = multiprocessing.Process(target=uptime, args=(tr_id, result,))

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()
        print(results)
        graph_uptime(results)
    else:
        print('Выберете параметр, для мониторинга! "-h" или "--help" поможет с выбором параметра.')
        quit()


if __name__ == "__main__":
    main()
