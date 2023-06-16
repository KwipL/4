if __name__ == '__main__':
# goods = [
#     {
#         'name':'Iphone 7',
#         'brand':'Apple',
#         'price': 100,
#     },
#     {
#         'name':'Ipad',
#         'brand':'Apple',
#         'price': 50,
#     },
#     {
#         'name':'Windows XP',
#         'brand':'Microsoft',
#         'price': 150,
#     }
# ]
# Функция лямбда
# def on_price(item):
#     return item['price']

# print(sorted(goods, key=lambda item: item['price']))

#Функция фильтра
# filtered_list = filter(lambda item: item['brand'] == 'Apple', goods)
# print(filtered_list)

#Функция мап
# numbers = ['1','2','3','4','5']
# result = list(map(int, numbers))
# print(result)

# name_list = ['Igor', 'Артем', 'Аня', 'Ксюша']
# surname = ['Иванов', 'Петрович', 'Максимовна', 'Андреевна']
#
# persons = list(map(lambda name, surname: f'{name} {surname}', name_list, surname))
# print(persons)

#Функция енумерейт
# new_goods = []
# for index, item in enumerate(goods):
#     print(index)
#     new_goods.append({index:item})
# print(new_goods)

#Функция зип
# name_list = ['Igor', 'Артем', 'Аня', 'Ксюша']
# surname = ['Иванов', 'Петрович', 'Максимовна', 'Андреевна']
# for person in zip(name_list,surname):
#     name,surname = person
#     print(name, surname)

#переменная name
print(__name__)
