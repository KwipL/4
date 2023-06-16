# class Year:
#     def __init__(self):
#         self.__days = 365
#
#     def get_days(self):
#         return self.__days
#
#     def set_days(self, days):
#         if days == 365 or days ==366:
#             self.__days = days
#         else:
#             raise ValueError
#
# year = Year()
# print(year.get_days())
# year.set_days(365)
# print(year.get_days())
# year.set_days(367)
# class Person:
# #     def __init__(self,name,age):
# #         self.__name = name
# #         self.__age = age
# #     @property
# #     def age(self):
# #         return self.__age #getter
# #     @age.setter
# #     def age(self, age): #setter
# #         if age < 0:
# #             raise ValueError
# #         self.__age = age
# #
# # person = Person('bd', 16)
# # print(person.age)
person_age =int(input())
if person_age > 0:
    ...
else:
    raise ValueError