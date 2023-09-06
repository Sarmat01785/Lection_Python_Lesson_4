# Функция map

# list_1 = [x for x in range (1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)



"""
Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя
используется пробел. Этот набор чисел будет считан в качестве строки. Как
превратить list строк в list чисел?
"""

# data = '1 2 3 5 8 15 23 38'
# print(data) # 1 2 3 5 8 15 23 38
# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

# data = '1 2 3 5 8 15 23 38'
# data = list(map(int,data.split()))
# print(data) # [1, 2, 3, 5, 8, 15, 23, 38]






def where(f, col):
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]
res = list(map(lambda x: (x, x ** 2), res))
print(res)  # [(2, 4), (8, 64), (38, 1444)]

