def get_count_char(str_):
    symb_dict = {}

    lower_str = str_.lower()
    for symb in lower_str:
        if symb.isalpha():
            if symb in symb_dict:
                symb_dict[symb] += 1
            else:
                symb_dict[symb] = 1
    return symb_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
