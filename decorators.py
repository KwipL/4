import time

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print('Прошло:', time.time() - start)
        return result
    return wrapper

@timer
def get_list_by_default_way(val):
    my_list = []
    for i in range(val):
        my_list.append(i)

    return my_list

@timer
def get_list_by_list_comp(val):
    return [i for i in range(val)]
    return my_list



get_list_by_default_way(10 ** 6 * 15)
get_list_by_list_comp(10** 6 * 15)


