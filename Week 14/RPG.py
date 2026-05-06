# Alex W.
# Period: 6 & 7
# Week 14 - Inheritance RPG Character
# Time: 141

import random,math



class Character:
    def __init__(self,name,hp,ap,lvl):
        self._name = name
        self._max_hp = hp
        self._ap = ap
        self._lvl = lvl
        self._current_hp = hp
    def attack(self):
        print(f'''You deal {random.randint(math.floor(0.8 * self._ap), math.floor(1.3 * self._ap))} damage with your unarmed attack!''')
    def take_dmg(self):
        dmg = random.randint(math.floor(0.08 * self._max_hp), math.floor(0.13 * self._max_hp))
        self._current_hp = self._current_hp - dmg
        print(f'''You take {dmg} damage!''')
    def stats_screen(self):
        print(f'''
Name: {self._name}
Level: {self._lvl}
HP: {self._current_hp}/{self._max_hp}
Attack Power: {self._ap}''')

class Knight(Character):
    def __init__(self,name,hp,ap,lvl,armor):
        Character.__init__(self,name,hp,ap,lvl)
        self._armor = armor
    def take_dmg(self):
        dmg = math.floor(random.randint(math.floor(0.08 * self._max_hp), math.floor(0.13 * self._max_hp)) * (1/(1+(self._armor/100)))) 
        self._current_hp = self._current_hp - dmg
        print(f'''You take {dmg} damage!''')
    def stats_screen(self):
        print(f'''
Name: {self._name}
Level: {self._lvl}
HP: {self._current_hp}/{self._max_hp}
Attack Power: {self._ap}
Armor: {self._armor}''')


me = Knight("Mr. A",100,10,1,100)
me.attack()
me.take_dmg()
me.stats_screen()
