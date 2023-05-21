"""Задайте собственную программу «Адресная книга», работающую из
командной строки и позволяющую просматривать, добавлять, изменять,
удалять или искать контактные
данные ваших знакомых.
Кроме того, эта информация также должна сохраняться на диске для
последующего доступа."""


def add_book(ab_dict):
    name_friend = input('Введите имя друга, которого вы хотите добавить -> ')
    number_friend = input('Введите номер телефона друга -> ')
    ab_dict[name_friend] = number_friend
    print(f'Друг {name_friend}, с номером {number_friend} добавлен в список контактов.')
    return ab_dict


def del_book(ab_dict):
    name_del = input('Введите имя друга, которого хотите удалить -> ')
    del ab_dict[name_del]
    print(f'Друг {name_del} был удалён из книги.')
    return ab_dict


def view_book(ab_dict):
    print('\n\t\t\t\t Список контактов')
    print('\t\t Имя друга \t\t | \t\t Контакт друга')
    for name, number in ab_dict.items():
        print(f'\t\t {name} \t\t -> \t\t {number}')


def edit_book(ab_dict):
    count = input('Введите значение, которое хотите изменить("Имя" или "Номер") -> ')
    if count == 'Имя':
        name_old = input('Введите имя друга, которого хотите изменить -> ')
        name_new = input('Введите изменённое имя друга -> ')
        ab_dict[name_new] = ab_dict[name_old]
        del ab_dict[name_old]
        print(f'Имя друга {name_old} было изменено на {name_new}.')
        return ab_dict
    elif count == 'Номер':
        number_friend = input('Введите имя друга, номер которого хотите изменить -> ')
        number_edit = input('Введите изменённый номер друга -> ')
        ab_dict[number_friend] = number_edit
        print(f'Номер друга {number_friend} был изменён на {number_edit}.')
        return ab_dict
    else:
        return '<Неизвестный запрос>'


def search_book(ab_dict):
    search_name = input('Введите имя друга, которого хотите найти -> ')
    return print(f'Друг {search_name} с контактными данными {ab_dict[search_name]} был найден!')
