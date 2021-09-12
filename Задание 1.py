#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


import sys

if __name__ == '__main__':
    workers = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            start = input("Название начального пункта маршрута? ")
            finish = input("Название конечного пункта маршрута? ")
            number = int(input("Номер маршрута? "))

            worker = {
                'start': start,
                'finish': finish,
                'number': number,
            }

            workers.append(worker)

            if len(workers) > 1:
                workers.sort(key=lambda item: item.get('number', ''))
        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "№",
                    "Начальный пункт",
                    "Конечный пункт",
                    "Номер маршрута"
                )
            )
            print(line)

            for idx, worker in enumerate(workers, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        worker.get('start', ''),
                        worker.get('finish', ''),
                        worker.get('number', 0)
                    )
                )
            print(line)

        elif command.startswith('select '):

            parts = command.split(' ', maxsplit=1)
            count = 0
            period = int(parts[1])

            for worker in workers:
                if worker.get('number') == period:
                    count += 1
                    print(
                        '{:>4} - {}'.format(worker.get('start', ''),
                                            worker.get('finish', ''))
                    )

            if count == 0:
                print("Маршрут с таким номером не найден.")
        elif command == 'help':

            print("Список команд:\n")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select <номер маршрута> - запросить данные о маршруте;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
