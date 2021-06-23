from labwork.py import *

class TestCharacters(object):
   def test_hero(self):
      self.hero = Hero('Hero', 8, 18, 12, 14, 8, 10)
      return self.hero

   def test_dragon(self):
      self.dragon = Dragon('Dragon', 10, 20, 10, 16, 8, 20)
      return self.dragon

heroes = TestCharacters()
hero = heroes.test_hero()
dragon = heroes.test_dragon()

hero_attacks_count = []
hero_perks_count = []
hero_heals_count = []
dragon_attacks_count = []
dragon_perks_count = []

def hero_average():
   for key in hero_attacks_count:
      return (key + key) / len(hero_attacks_count)

def dragon_average():
   for key in dragon_attacks_count:
      return (key + key) / len(dragon_attacks_count)

def abilitie():
   abilities = 2 + floor((hero.charisma - 10) / 2)
   if(abilities > 0):
      abilities = abilities - 1
      return hero.perk()
   else:
      return None

if hero.initiative > dragon.initiative:
   for i in range(dragon.hp):
      if dragon.hp > 0:
         if hero.hp > 11:
            if abilitie() == True:
               hero_perk = abilitie()
               dragon.hp = dragon.hp - hero_perk
               hero_perks_count.append(hero_perk)
            else:
               hero_atack = hero.attack()
               dragon.hp = dragon.hp - hero_atack
               hero_attacks_count.append(hero_atack)
         else:
            healing = hero.save_throw(hero.wisdom)
            hero.hp = hero.hp + healing
            hero_heals_count.append(healing)
      else:
         dragon.death()
         break;
else:
   for i in range(hero.hp):
      if hero.hp > 0:
         if abilitie() == True:
            dragon_perk = abilitie()
            hero.hp = hero.hp - dragon_perk
            dragon_perks_count.append(dragon_perk)
         else:
            dragon_atack = dragon.attack()
            hero.hp = hero.hp - dragon_atack
            dragon_attacks_count.append(dragon_atack)
      else:
         hero.death()
         break;

result = 'Среднее значения атаки персонажа "Dragon" составляет: ' + str(dragon_average()) + '\nКоличество атаки персонажа "Dragon" составляет: ' + str(len(dragon_attacks_count)) + '\nКоличество атаки способностью персонажа "Dragon" составляет: ' + str(len(dragon_perks_count)) + '\n──────────────────────────────────────────────────────────────────────────' + '\nСреднее значения атаки персонажа "Hero" составляет: ' + str(hero_average()) + '\nКоличество атаки персонажа "Hero" составляет: ' + str(len(hero_attacks_count)) + '\nКоличество лечении персонажа "Hero" составляет: ' + str(len(hero_heals_count)) +'\nКоличество атаки способностью персонажа "Hero" составляет: ' + str(len(hero_perks_count))
print(result)
