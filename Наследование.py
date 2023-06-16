# class A:
#     def info(self):
#           print('A')
#
# a  = A()
# a.info()
#
# class B(A):
#     pass
#
# b = B()
# b.info()

class Pet:
    has_tail = True
    legs = 4
    name = None
    animal = None

    def __str__(self):
          result = f" Питомец  {self.name}.  Это  {self.animal} . " \
                      f" У него  {'есть хвост' if self.has_tail else 'хвоста нет'}. У него {self.legs}"

          return result

    def sound(self):
        return 'КВА'

class Frog(Pet):
    has_tail = False
    name = 'пепе'
    animal = 'Лягушка'

print(Frog(), Frog().sound())