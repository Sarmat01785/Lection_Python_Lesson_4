"""
В Python есть механизм, который позволяет превратить подобный вызов во что-то
более красивое — lambda.
"""
# def sum(x, y):
#     return x + y
# # ⇔ (равносильно)
# sum = lambda x, y: x + y

# # Также можно пропустить шаг создания переменной sum и сразу вызвать lambda:
# sum(lambda x, y: x + y, 4, 5) # 9


# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))
#     # result = op(x, y)
#     # print(result)
# calc1 = lambda a, b: a + b

# math(calc1, 5, 45) # 50


# def calc2(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))
#     # result = op(x, y)
#     # print(result)

# # def calc1(a, b):
# #     return a + b

#  # ⇔ (равносильно)
# calc1 = lambda a, b: a + b

# math(calc1, 5, 45) # 50


def calc2(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))   # 50
    # result = op(x, y)
    # print(result)


math(lambda a, b: a + b, 5, 45)
