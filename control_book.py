import book_function as bf
import pickle


def set_command():
    return print('\n\t\t\t\t Список доступных команд \n add - добавить друга в книгу контактов\
     \n del - удалить контакт \n view - посмотреть книгу контактов \n edit - изменить контакт\
     \n search - найти контакт по имени\n')


# Функция сохранения словаря в программу
def save_book(filename, book):
    with open(filename, 'wb') as f:
        pickle.dump(book, f)


# Функция загрузки словаря в программу
def load_book(filename):
    with open(filename, 'rb') as f:
        book = pickle.load(f)
    return book


# Начало программы
print('\n\t\t Добро пожаловать в FContact!')
try:
    address_book = load_book('address_book.data')
except FileNotFoundError:
    print('\nНет сохранённых контактов! Создайте новую адресную книгу.')
    address_book = {}

while True:
    request = input('\nВведите запрос (Помощь -> help) : ')

    if request == 'help':
        set_command()
    elif request == 'add':
        bf.add_book(address_book)
    elif request == 'del':
        bf.del_book(address_book)
    elif request == 'view':
        bf.view_book(address_book)
    elif request == 'edit':
        bf.edit_book(address_book)
    elif request == 'search':
        bf.search_book(address_book)
    elif request == 'exit':
        save_book('address_book.data', address_book)
        print('Все данные успешно сохранены!')
        break
