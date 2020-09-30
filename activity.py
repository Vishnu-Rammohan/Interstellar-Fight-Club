# Team name: Contest of Champions

import random

class Alien:

    def __init__(self, name, class_type, health, attack, defense, special_weapon, chance):
        self.name = name
        self.class_type = class_type
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_weapon = special_weapon
        self.chance = chance

# Attack Move
    def attack_enemy(self, other_alien):
        num= 0
        num = round(random.randint(1,11))

        if num >= self.chance: 
            dmg = self.attack
            other_alien.health -= dmg
            
            if other_alien.health <= 0:
                print(f"{self.name} is attacking {other_alien.name} for {dmg}")
                print(f"{self.name} wins!")
            else:
                print(f"{self.name} is attacking {other_alien.name} for {dmg}")
            self.defend_from_attack(other_alien)
        else:
            
            print(f"{other_alien.name} has Missed!")

            
        return self

    
    def heal_self(self):
        heal= (self.health * .25)
        self.health += heal
        print(f"{self.name} has healed by {heal}")
        return self

# Defense move: 
    def defend_from_attack(self, other_alien):  

        if other_alien.attack > self.defense:
            self.health = self.health - (other_alien.attack - self.defense)
        elif other_alien.attack < self.defense:
            pass
        
            print(f"{self.name} has defended from {other_alien.name} for {self.defense}")
        return self

    def display_current_status(self):
        print(f"Name: {self.name}, Health: {self.health}")
        # print(f"Name: {other_alien.name}, Health: {other_alien.health}")
        return self
    
    def special_atk(self,other_alien):
        if self.special_weapon == "Meatball":
            dmg = -5
            other_alien.health -= dmg
        elif self.special_weapon == "Pencil":
            dmg = 90
            other_alien.health -= dmg
        elif self.special_weapon == "Spoon":
            dmg = 75
            other_alien.health -= dmg
        elif self.special_weapon == "Fork":
            dmg = 5
            other_alien.health -= dmg
        print(f"{self.name} has used 'SPECIAL WEAPON: {self.special_weapon}' on {other_alien.name}")
        
        if other_alien.health <= 0:
            print(f"{self.name} is attacking {other_alien.name} for {dmg}")
            print(f"{self.name} wins!")
        else:
            print(f"{self.name} is attacking {other_alien.name} for {dmg}")
        return self

    
# name, class_type, health, attack, defense, special_weapon, chance
vishnu = Alien("Vishnu","Meat Shield", 100, 10, 35, "Meatball", 7)
frank = Alien('Frank','Glass_Cannon',100,70,0,"Pencil", 3)
mika = Alien("Mika","Warrior", 100, 40, 50, "Spoon", 6)
jay = Alien("Jay", "Healer", 50, 5, 5, "Fork", 10)

frank.attack_enemy(mika)
mika.defend_from_attack(frank)
mika.attack_enemy(frank)
frank.defend_from_attack(mika)
frank.heal_self()
frank.display_current_status()  # => attack vishnu 
mika.display_current_status()
frank.special_atk(mika)
mika.display_current_status()