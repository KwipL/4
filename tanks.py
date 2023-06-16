class Tank:
    def __init__(self,hp,armor,damage):
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def shoot(self,enemy):
        enemy.health_down(self.damage)
        print(f'Шмальнули по {enemy}')

    def health_down(self,damage):
        total_damage = damage / self.armor
        self.hp -= total_damage
        print(f'Нас шмальнули на {damage}')

class T34(Tank):
    def __str__(self):
        return 'T34'

class KV44(Tank):
    def  __init__(self,hp,armor,damage):
        super().__init__(hp,armor*10,damage*10)
    def __str__(self):
        return 'KV44'

t34 = T34(1000, 1500, 200)
kv44 = KV44(1000, 1500, 100)

t34.shoot(KV44)


class User:
    def __init__(self, health):
        self.health = health

    def attack(self, target):
        damage = 286
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
