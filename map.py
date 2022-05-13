li = [x for x in range(1, 11)]

def func(x):

    return x**2

li2 = list(map(func, li))
print(li2)

li3 = list(map(lambda x : x**3, li))
print(li3)

x = [1, 2, 3]
y = [4, 5, 6, 7]
li4 = list(map(lambda a, b : a + b, x, y[1:]))
print(li4)