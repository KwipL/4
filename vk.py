from contextlib import contextmanager
# import time
# my_list = (time.sleep(x) for x in range(1,3))
# print(type(my_list))
# def lazy():
#     for i in range(1,11):
#         print('До',i)
#         yield i
#         print('После',i)
#
# for i in lazy():
#     print(i)
# def lazy(items):
#     yield from (i **2 for i in items)
# for i in lazy([1,2,3,4]):
#     print(i)
# with open('test.txt','w', encoding='utf-8') as f:
#     f.write('Скоро')
#     print(f.closed)
my_list = [1,2]
# @contextmanager
# def exc_handler(exc):
#     try:
#         yield True
#     except exc:
#         print('Ошибка')
#
# with exc_handler(IndexError):
#     my_list[4]
squares = (n** 2 for n in range(1000000))
for square in squares:
    print(square)