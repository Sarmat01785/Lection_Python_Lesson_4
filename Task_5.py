# Функция filter
# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) # [0, 2, 4, 6, 8]




# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res) # [15, 65, 175]



data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)

res = filter(lambda x: x % 2 == 0, res)

res = list(map(lambda x: (x, x ** 2), res))
print(res)  # [(2, 4), (8, 64), (38, 1444)]