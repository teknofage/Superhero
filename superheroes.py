import random


#I worked on this with Eric and Donny. 

def validator(list_of_valid_entries, input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            for item in list_of_valid_entries:
                if item == entry:
                    is_valid = True
                else:
                    pass
            if is_valid:
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Invalid Input! Try again...")

def validator_num(input_text):
    is_valid = False
    while True:
        try:
            entry = input(input_text)
            if entry.isdigit()== True:
                is_valid = True
                return entry
            else:
                print("Invalid Input! Try again...")
        except:
            print("Invalid Input! Try again...")





class Hero:
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Append ability to self.abilities
        self.abilities.append(ability)

    def add_armor(self, armor):
        # Append armor
        self.armors.append(armor)

    def attack(self):
        totalAttacks = 0
        for ability in self.abilities:
            # attack(self)
            totalAttacks += ability.attack()
            # name of variable you assigned in the loop
            print(totalAttacks)
        return totalAttacks

    def defend(self):

        # Before anything, check or validate the hero's health
        totalDefense = 0
        # if self.health <= 0:
        #     return totalDefense

        for armor in self.armors:
            totalDefense += armor.defense
            print("Total Defense: {}".format(totalDefense))
        return int(totalDefense)

    def take_damage(self, damage_amt):
        damage_amt -= self.health
        if self.deaths >= 1:
            self.death += 1
        self.kills += num_kills

    def add_kill(self, num_kills):
        self.kills += num_kills

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        attack_value = random.randint((self.attack_strength // 2), self.attack_strength)
        return attack_value

    def update_attack(self, attack_strength):
        # Update the value of the current attack strength with the # new value passed in as a parameter.
        self.attack_strength = attack_strength
        
class Weapon(Ability):
    def attack(self):
        weapon_attack_value = random.randint(0, self.attack_strength)
        return weapon_attack_value


class Team:
    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()
        self.num_kills = 0

    def add_hero(self, Hero):
        self.heroes.append(Hero)

    def remove_hero(self, name):
        if len(self.heroes) <= 0:
            return 0
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
            else:
                return 0

    def find_hero(self, name):
        if len(self.heroes) <= 0:
            return 0
        for hero in self.heroes:
            if hero.name == name:
                return hero
            else:
                return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def attack(self, other_team):
        totalTeamAttackStrengths = 0
        # num_kills = 0
        for hero in self.heroes:
                totalTeamAttackStrengths += hero.attack()
                print("Total Team Attack Strength: {}".format(totalTeamAttackStrengths))
        # return totalTeamAttackStrengths
        num_kills = other_team.defend(totalTeamAttackStrengths)
        for hero in self.heroes:
            if num_kills >= 1:
                hero.add_kill(num_kills)
        return(num_kills)

    def defend(self, damage_amt):

        totalTeamDefense = 0
        excessDamage = 0
        for hero in self.heroes:
            for armor in hero.armors:
                totalTeamDefense += armor.defense

        for hero in self.heroes:
            for ability in hero.abilities:
                damage_amt += ability.attack_strength
                print("Damage amount: {}".format(damage_amt))
        excessDamage = damage_amt - totalTeamDefense
        return self.deal_damage(excessDamage)

    def deal_damage(self, damage):

        divisionOfDamage = damage // len(self.heroes)
        numHerosDiedInAttack = 0
        for hero in self.heroes:
            if hero.health > 0:
                hero.health -= divisionOfDamage
                if hero.health <= 0:
                    numHerosDiedInAttack += 1
                    hero.deaths += 1
        return numHerosDiedInAttack

    def revive_heroes(self):
        for hero in self.heroes:
            hero.health = hero.start_health

    def stats(self):
        print(self.name)
        for hero in self.heroes:
            print("{} had a kill/death ratio of {}/{}".format(hero.name, hero.kills, hero.deaths))

    def update_kills(self):
        for hero in self.heroes:
            health = 0


class Armor:
    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)

class Arena(Hero, Team):
    def __init__(self):
        """
        Declare variables
        """

    def build_abilities_list(self):
        # Return an ability and append ability
        abilities = [
            "Alien Attack",
            "Science",
            "Star Power",
            "Immortality",
            "Grandmas Cookies",
            "Blinding Strength",
            "Cute Kittens",
            "Team Morale",
            "Luck",
            "Obsequious Destruction",
            "The Kraken",
            "The Fire of A Million Suns",
            "Team Spirit",
            "Canada"]
        # Get one abilitiy out of the list
        index = random.randint(0, len(abilities) - 1)
        ability_name = abilities[index]
        abil_att_Strength = random.randint(0, 600)
        one_ability = Ability(ability_name, abil_att_Strength)
        return one_ability
        # hero.add_ability(one_ability) # <-- Doing this in create_hero

    def build_armors_list(self):
        armors = [
            "Calculator",
            "Laser Shield",
            "Invisibility",
            "SFPD Strike Force",
            "Social Workers",
            "Face Paint",
            "Damaskus Shield",
            "Bamboo Wall",
            "Forced Projection",
            "Thick Fog",
            "Wall of Will",
            "Wall of Walls",
            "Obamacare",
            "Thick Goo"]
        # Get one armor out of the list
        index = random.randint(0, len(armors) - 1)
        armor_name = armors[index]
        defense = random.randint(0, 600)
        one_armor = Armor(armor_name, defense)
        return one_armor

    def create_hero(self):
        heroes = [
            "Athena",
            "Jodie Foster",
            "Wonder Woman",
            "Christina Aguilera",
            "Gamora",
            "Supergirl",
            "Batgirl",
            "Carmen Sandiego",
            "Okoye",
            "America Chavez",
            "Cat Woman",
            "White Canary",
            "Nakia",
            "Mera",
            "Iris West",
            "Quake",
            "Wasp",
            "Storm",
            "Black Widow",
            "San Luis Obispo",
            "Ted Kennedy",
            "San Francisco",
            "Bananas"]
        index = random.randint(0, len(heroes) - 1)
        hero_name = heroes[index]
        hero = Hero(hero_name)
        # Ask how many abilities does the hero have then build that many abilities
        abilites_number = int(validator_num("How many abilities do you want your hero {} to have? ".format(hero.name)))
        for _ in range(0, abilites_number):
            ability = self.build_abilities_list()
            hero.add_ability(ability)
        print(hero.abilities)
        # Ask How many armor
        armors_number = int(validator_num("How many picecs of armor do you want your hero {} to have? ".format(hero.name)))
        # However many armor the user wants the hero get the ability and add to the heros list of armor that many times
        for _ in range(0, armors_number):
            hero.add_armor(self.build_armors_list())
        print(hero.armors)
        return hero
