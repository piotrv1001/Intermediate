l1 = [x for x in range(1, 21) if x % 2 == 0]
print(l1)

l2 = [x for x in range(1, 21) if x % 2 == 0 and x % 5 == 0]
print(l2)

l3 = [x for x in range(1, 21) if x == 13 or x > 16]
print(l3)

l4 = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 21)]
print(l4)

l5 = [f"{x}: Even" if x % 2 == 0 else f"{x}: Odd" for x in range(1, 21) if x >= 10]
print(l5)

matrix = [[1,2,3,4], [5,6,7,8]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

# transposed = []
# for i in range(len(matrix[0])):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

width = 5
height = 6
l6 = [[0 for _ in range(height)] for _ in range(width)]
print(l6)
print(l6[0][0])

def makeTranspose(matrix):

    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(makeTranspose([[1,2,3], [4,5,6]]))

squares = [x**2 for x in range(1, 11)]
print(squares)

dict1 = {x : x**3 for x in range(1, 11) if x % 2 == 1}
print(dict1)

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd', 'e']
c = {key : value for (key, value) in zip(a, b)}
print(c)

d = [2, 2, 2, 4, 4, 6, 6, 6, 6]
print(d)
e = {x for x in d if x % 2 == 0}
print(e)

gen = (x for x in d)
for x in gen:
    print(x, end = ' ')

print('')