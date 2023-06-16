a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = list(filter(lambda x: x % 2, a))
even = list(filter(lambda x: not x % 2, a))
print(odd, even)