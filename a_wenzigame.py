import random

print('''欢迎来到大话中北''')


class Creature():
    def __init__(self,hp,name):
        self.hp = hp
        self.name = name

    def attack(self):
        attack_value = random.randint(0,50)
        return attack_value

    def being_attrack(self,attack_value):
        self.hp = self.hp - attack_value

    def not_dead(self):
        if self.hp<0:
            return False
        else:
            return True

    def show_status(self):
        print('{}\'s hp is {}.'.format(self.name,self.hp))

player = Creature(100,'boy')
enemy = Creature(80,'enemy')

while player.not_dead() and enemy.not_dead():
    player.show_status()
    enemy.show_status()

    user_input = input('Attrack or Defence(A/D):')

    if user_input == 'A':
        player_attrack_value = player.attack()
        enemy_attrarck_value = enemy.attack()
        enemy.being_attrack(player_attrack_value)
        player.being_attrack(enemy_attrarck_value)
    elif user_input == 'D':
        enemy_attrarck_value = enemy.attack()
        player.being_attrack(enemy_attrarck_value)

if player.not_dead():
    print('You win!')
else:
    print('You lose!')
