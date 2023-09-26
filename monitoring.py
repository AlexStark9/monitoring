#!/usr/bin/env python3
import multiprocessing
from params import *
from graphs import *
from args import arg_parse
from checking_device import device_selection
from helpers import *


def main():
    args = arg_parse()
    time_sec = args.time

    tr_id = device_selection()

    if args.all:
        print(f'Запущен мониторинг всех парметров. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        pr = Parser(tr_id=tr_id, result=result)
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec, ))
        target2 = multiprocessing.Process(target=pr.all_params)

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        pl = Plotting(results)
        pl.graph_all_params()
    elif args.freq:
        print(f'Запущен мониторинг частоты CPU. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        pr = Parser(tr_id=tr_id, result=result)
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec, ))
        target2 = multiprocessing.Process(target=pr.freq)

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        pl = Plotting(results)
        pl.graph_freq()
    elif args.idle:
        print(f'Запущен мониторинг idle. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        pr = Parser(tr_id=tr_id, result=result)
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec, ))
        target2 = multiprocessing.Process(target=pr.idle)

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        pl = Plotting(results)
        pl.graph_idle()
    elif args.memory:
        print(f'Запущен мониторинг свободной RAM. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        pr = Parser(tr_id=tr_id, result=result)
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec, ))
        target2 = multiprocessing.Process(target=pr.memory)

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()

        pl = Plotting(results)
        pl.graph_memory()
    elif args.temp:
        print(f'Запущен мониторинг тумпературы. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        pr = Parser(tr_id=tr_id, result=result)
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec, ))
        target2 = multiprocessing.Process(target=pr.temp)

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()
        print(results)
        pl = Plotting(results)
        pl.graph_temp()
    elif args.uptime:
        print(f'Запущен мониторинг load averages. Время выполнения теста {time_sec} секунд.')
        manager = multiprocessing.Manager()
        result = manager.list()
        pr = Parser(tr_id=tr_id, result=result)
        target1 = multiprocessing.Process(target=monitoring_time, args=(time_sec, ))
        target2 = multiprocessing.Process(target=pr.uptime)

        target1.start()
        target2.start()

        target1.join()
        results = result
        target2.join()
        print(results)
        pl = Plotting(results)
        pl.graph_uptime()
    else:
        print('Выберете параметр, для мониторинга! "-h" или "--help" поможет с выбором параметра.')
        quit()


if __name__ == "__main__":
    main()
