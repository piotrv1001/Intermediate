from collections import Counter

li = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]
print(Counter(li))

di = {"A" : 3, "B" : 4, "C" : 2, "D" : 5}
print(Counter(di))

print(Counter(A = 2, B = 3, C = 8, D = 11))

c1 = Counter([1, 1, 1, 2, 2, 3, 3, 3, 3])
print(c1)
c1.update([4, 5, 1])
print(c1)
print(len(c1.keys())) # Count distinct values in a list ( keys )

# Make list of items who appear more than once
li2 = [1, 1, 2, 2, 3, 3, 4, 5, 6]
c2 = Counter(li2)
more_than_once = [key for key, counter in c2.items() if counter > 1]
print(more_than_once)

orders = ["Adam", "Jason", "Julia", "Peter", "Adam", "Peter", "Peter"]
c3 = Counter(orders)
tuples = [(key, value) for key, value in c3.items()]
tuples.sort()
for i in tuples:
    print("Customer: {name}, Orders = {orders}".format(name = i[0], orders = i[1]))

print(c2.most_common(2))

x = {1 : 2, 2 : 2, 3 : 4}
y = [1, 1, 2 , 3, 3]
cx = Counter(x)
cx.subtract(y)
print(cx)

