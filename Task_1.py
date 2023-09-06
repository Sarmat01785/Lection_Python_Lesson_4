# Анонимные, lambda-функции

# def f(x):
#     return x ** 2
# print(f(2))  # 4
# print(type(f)) # <class 'function'>


# def f(x):
#     return x ** 2
# g = f
# print(f(4)) # 16
# print(g(4)) # 16


# def calc1(x):
#     return x + 10
# print(calc1(10)) # 20


# def calc2(x):
#     return x * 10

# def math(op, x):
#     result = op(x)
#     print(result)
    
# math(calc2, 10) # 100





# def calc1(a):
#     return a + a


# def calc2(a):
#     return a * a

# def math(op, x):
#     result = op(x)
#     print(result)  # 10
    
# math(calc1, 5)



# def calc1(a):
#     return a + a


# def calc2(a):
#     return a * a

# def math(op, x):
#     result = op(x)
#     print(result)  # 25
    
# math(calc2, 5)


# def calc1(a, b):
#     return a + b




# Попробуем описать ту же логику для функции с двумя переменными.
# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     result = op(x, y)
#     print(result)  # 50
    
# math(calc1, 5, 45)



# def calc1(a, b):
#     return a + b


# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     result = op(x, y)
#     print(result)  # 225
    
# math(calc2, 5, 45)




def sum(x, y):
    return x + y
def mylt(x, y):
    return x * y
def calc(op, a, b):
    print(op(a, b))
calc(mylt, 4, 5) # 20

# Можно создать псевдоним для функции сложения (f).
f = sum
calc(f, 4, 5) # 9



