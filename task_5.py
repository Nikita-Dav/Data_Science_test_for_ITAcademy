def func_5(queries_list):
    words_count_list = []
    for el in queries_list:
        words_count_list.append(len(el.split()))

    words_count_list_unique = sorted(set(words_count_list))

    for el in words_count_list_unique:
        print(f'{el} слов: {words_count_list.count(el) / len(words_count_list) * 100}%')