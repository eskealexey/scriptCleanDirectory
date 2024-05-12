from my_lib import my_liba as ml

path_dist = ml.check_dir()
print(f'Выбран каталог "{path_dist}"')
# path_dist = '/home/alexey/tmp'
list_full = ml.get_list_files(path_dist)
ext_ = None
list_ext = []
list_search = []
while True:
    while 1:
        try:
            ans = input('Ищем по расширению файла? (1-Да, 0-Нет):')
            if int(ans) == 0:
                break
            elif int(ans) == 1:
                ext_ = input('Расширение файла: ').strip()
                if ext_[0] != '.':
                    ext_ = '.' + ext_
                list_ext = ml.get_list_file_ext(list_full, ext_)
                ml.view_list(list_ext)
                break
        except ValueError:
            continue

    while 1:
        try:
            sec, sec2 = None, None
            ans1 = input('Ищем по дате? (1-Да, 0-Нет):')
            if int(ans1) == 0:
                # ml.view_list(list_full)
                break
            elif int(ans1) == 1:
                a = input('Используем одну дату? (1-Да, 0-Нет):')
                if int(a) == 1:
                    print('Используем 1 дату')
                    dat = input('Введите 1-ю дату в формате "YYYY-MM-DD":')
                    sec = ml.get_second_from_date(dat)
                    par = input('Как искать (0 - меньше даты, 1 - больше даты)?:')
                    if int(par) == 0:
                        arg = 'less'
                    elif int(par) == 1:
                        arg = 'more'
                    if len(list_ext) == 0:
                        list_search = ml.search_file_date(list_full, sec, sec2, arg)
                    else:
                        list_search = ml.search_file_date(list_ext, sec, sec2, arg)
                    # ml.view_list(list_search)
                elif int(a) == 0:
                    print('Используем 2 даты')
                    dat = input('Введите 1-ю дату в формате "YYYY-MM-DD":')
                    sec = ml.get_second_from_date(dat)
                    dat2 = input('Введите 2-ю дату в формате "YYYY-MM-DD":')
                    sec2 = ml.get_second_from_date(dat2)
                    if len(list_ext) == 0:
                        list_search = ml.search_file_date(list_full, sec, sec2, 'between')
                    else:
                        list_search = ml.search_file_date(list_ext, sec, sec2, 'between')
                    # ml.view_list(list_search)
                break
        except ValueError:
            continue
    break

if len(list_search) == 0:
    list_search = list_full

ml.view_list(list_search)