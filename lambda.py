square = lambda x : x**2

for i in range(1, 11):
    print(square(i))

def func():

    mini_func = lambda x : x + 3
    for i in range(3):
        print(mini_func(i))

func()