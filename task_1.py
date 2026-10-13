def func_1(initial_list):
    new_list = []
    for num in initial_list:
        if num % 2 == 0 and num not in new_list:
            new_list.append(num)

    return sorted(new_list, reverse=True)