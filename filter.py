nums = [x for x in range(1, 21)]
print(nums)

def is_even(num):
    return num % 2 == 0

even_nums = list(filter(is_even, nums))
print(even_nums)

letters = ['a', 'A', 'b', 'B', 'c', 'C', 'e', 'E']
print(letters)
small_letters = list(filter(lambda letter : letter.islower(), letters))
print(small_letters)

small_vowels = list(map(lambda letter : 3 * letter, filter(lambda letter : letter.islower() and letter in "aeiou", letters)))
print(small_vowels)
print(' '.join(small_vowels))