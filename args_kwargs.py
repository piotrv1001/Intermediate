def adder(*nums):

    sum = 0
    for num in nums:
        sum += num

    return sum

print(adder(1,2))
print(adder(1,2,3))
print(adder(1,2,3,4))

def info(**kwargs):

    for key, value in kwargs.items():
        print(f"Key = {key}, value = {value}")


info(Name = "Lebron", Surname = "James")
print('')
info(Name = "Kevin", Surname = "Durant", Playoffs = False)