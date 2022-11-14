#!/usr/bin/env python3
# -*- coding^ utf-8 -*-


import sys

if __name__ == '__main__':
    contacts = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':

            family = input("Фамилия? ")
            name = input("Имя? ")
            number = int(input("Номер телефона? "))
            born = list(map(int, input("Дата рождения? ").split('.', 2)))

            contact = {
                'family': family,
                'name': name,
                'number': number,
                'born': born,
            }

            contacts.append(contact)

            if len(contacts) > 1:
                contacts.sort(key=lambda item: item.get('number', [0 - 2]))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 30,
                '-' * 20
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^30} | {:^20} |'.format(
                    "№",
                    "Фамилия",
                    "Имя",
                    "Номер телефона",
                    "Дата Рождения"
                )
            )
            print(line)

            for idx, contact in enumerate(contacts, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:<30} | {:>20} |'.format(
                        idx,
                        contact.get('family', ''),
                        contact.get('name', ''),
                        contact.get('number', 0),
                        '.'.join((str(i) for i in contact['born']))
                    )
                )
            print(line)


        elif command.startswith('select'):

            count = 0
            period = input('Введите Фамилию человека, информацию по которому Вы хотите найти: ')

            for contact in contacts:
                if contact.get('family') == period:
                    count += 1
                    print(
                        '{:>4} {}: {}, {}'.format(contact.get('family', ''),
                                                  contact.get('name', ''),
                                                  contact.get('number', ''),
                                                  '.'.join((str(i) for i in contact['born'])))
                    )

            if count == 0:
                print('Человека с такой фамилией в списке нет.')
        elif command == 'help':

            print("Список команд:\n")
            print("add - Добавить контакт;")
            print("list - Вывести список контактов;")
            print("select Поиск по фамилии;")
            print("help - Отобразить справку;")
            print("exit - Завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
