import os
import pathlib
import datetime


def check_dir():
    """Проверка наличия каталога"""
    while True:
        path = input('Укажите целевой каталог: ')
        if not os.path.exists(path):
            continue
        else:
            if path[len(path)-1] == '/':
                path = path[:len(path)-1]
            return path


def get_second_from_date(str_):
    """Преобразование даты в секунды"""
    list_ = str_.split('-')
    dt = datetime.datetime(int(list_[0]), int(list_[1]), int(list_[2]), 0, 0, 0)
    seconds = datetime.datetime.timestamp(dt)
    return seconds


def get_list_files(root_):
    """Функция получения списка файлов в каталоге и подкаталогах"""
    list_ = []
    for root, dirs, files in os.walk(root_):
        for file in files:
            list_.append(os.path.join(root, file))
    return list_


def get_list_file_ext(lst_, ext_):
    """Получить список файлов по расширению"""
    list_ext = []
    lh = len(ext_)
    for file in lst_:
        str_ = str(file[-lh:])
        if str_.lower() == str(ext_).lower():
            list_ext.append(file)
    return list_ext


def files_delete(full):
    """Удаление файлов"""
    for f in full:
        os.remove(f)


def search_file_date(list_, second, second2=None, opc='less'):
    """Поиск файлов с определенной датой создания"""
    # print(second,second2)
    list_search = []
    for f in list_:
        df = os.path.getmtime(f)
        if opc == 'less':
            if df < second:
                list_search.append(f)
        elif opc == 'more':
            if df > second:
                list_search.append(f)
        elif opc == 'between':
            if (df >= second) & (df <= second2):
                list_search.append(f)
    return list_search


def view_list(lst_):
    try:
        with open('search.txt', mode='w', encoding='utf-8') as ff:
            for f in lst_:
                file = pathlib.Path(f)
                size_f = os.path.getsize(file)
                date_f = datetime.datetime.fromtimestamp(os.path.getmtime(file))
                print('{:100} Размер: {:10}   дата: {}'.format(file.__fspath__(), size_f, date_f))
                ff.write('{:100} Размер: {:10}   дата: {}\n'.format(file.__fspath__(), size_f, date_f))
    except FileNotFoundError:
        pass