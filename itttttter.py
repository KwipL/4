import random
class RandomIter:
    def __init__(self,limit):
        self.limit = limit

    def __iter__(self):

        return self

    def __next__(self):
        if self.limit == 0:
            raise StopIteration
        self.limit -= 1

        return random.randint(0,100)

random_iterator = RandomIter(10)

for i in RandomIter(10):
    print(i)















# my_list = [1,2,3]

# for i in my_list:
#     print(i)
# iterator = iter(my_list)
#
# for i in iterator:
#     print(i)
#
# for i in iterator:
#     print(i)
# print(next(iterator))
