def func_2(vec_1, vec_2):
    if len(vec_1) != len(vec_2):
        print('Ошибка: невозможно рассчитать косинусное расстояние для векторов различных размерностей')
        return
    
    norm_1 = 0
    norm_2 = 0
    scalar_mul = 0
    
    for i in range(len(vec_1)):
        norm_1 += vec_1[i] ** 2
        norm_2 += vec_2[i] ** 2
        scalar_mul += vec_1[i] * vec_2[i]

    if norm_1 == 0:
        print('Ошибка: 1-ый вектор является нулевым')
        return
    
    if norm_2 == 0:
        print('Ошибка: 2-ой вектор является нулевым')
        return
    
    cos_dist = 1 - (scalar_mul / ((norm_1 ** 0.5) * (norm_2 ** 0.5)))
    print(cos_dist)