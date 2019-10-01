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
        ''' Add ability to abilities list '''
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
        
    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check whether the hero is alive and return true or false
        if self.current_health <= 0:
            return False
        else:
            print("Your hero {} is dead!")
            return True
            

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
        Instantiate variables
        """
        self.team_one = None 
        self.team_two = None 

    def build_abilities_list(self):
        # Return an ability and append ability
        abilities = [
            "Spinning Bird Kick",
            "Flashbang",
            "Dazzle",
            "Invulnerability",
            "BAMF!",
            "Telekenisis",
            "Rain of Frogs",
            "Pym Particles",
            "Super Stretchy",
            "Lava Hands",
            "Multiplicity",
            "One Inch Punch",
            "Assumed Superiority",
            "Hella Henchmen"]
        # Get one abilitiy out of the list
        index = random.randint(0, len(abilities) - 1)
        ability_name = abilities[index]
        abil_att_Strength = random.randint(0, 600)
        one_ability = Ability(ability_name, abil_att_Strength)
        return one_ability
        # hero.add_ability(one_ability) # <-- Doing this in create_hero

    def build_armors_list(self):
        armors = [
            "Chain Mail",
            "Forcefield",
            "Energy Absorption",
            "Woad",
            "Riot Gear",
            "Sun Hat",
            "Turtle Shell",
            "Kevlar Suit",
            "Invisibility",
            "Skunk Power",
            "Battle Suit",
            "Jockstrap",
            "Ion Shield",
            "Shroud of Mystery"]
        # Get one armor out of the list
        index = random.randint(0, len(armors) - 1)
        armor_name = armors[index]
        defense = random.randint(0, 600)
        one_armor = Armor(armor_name, defense)
        return one_armor

    def create_hero(self):
        heroes = [
            "Captain Planet",
            "Colin Kaepernick",
            "Optimus Prime",
            "Harriet Tubman",
            "Frankenstein",
            "Animal Man",
            "Johnny Alpha",
            "Durham Red",
            "Nikolai Dante",
            "Banana Man",
            "Black Widow",
            "Cable",
            "Deadpool",
            "Namor",
            "Wolverine",
            "Jubilee",
            "Elektra",
            "Hulk",
            "Moon Knight",
            "Future Man",
            "Avatar Korra",
            "Desperate Dan",
            "Nightcrawler"]
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
        armors_number = int(validator_num("How many pieces of armor do you want your hero {} to have? ".format(hero.name)))
        # However many armor the user wants the hero get the ability and add to the heros list of armor that many times
        for _ in range(0, armors_number):
            hero.add_armor(self.build_armors_list())
        print(hero.armors)
        return hero


    def build_team_one(self):
    
        print("Welcome to the Pit of Despair:")
        print("   Where two teams enter, and only one team leaves")

        team_name = input("Name your team, fleshy one! ")

        self.team_one = Team(team_name)
        choosing_Team_Size = True
        while choosing_Team_Size:
            hero_number = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Do you want to add a hero? (Y/N)")
            # every time I create a hero apppend that hero to the team
            if hero_number == "Yes" or hero_number == "yes" or hero_number == "y" or hero_number == "Y":
                self.team_one.add_hero(self.create_hero())
                print(self.team_one.heroes)
            else:
                choosing_Team_Size = False

        # print("This is Team 1 list of heroes: {}.".format(team_one.heroes))

    def build_team_two(self):

        print("\n")
        print("Build Team 2!")
        team_name = input("Name your team, weakling! ")

        self.team_two = Team(team_name)
        choosing_Team2_Size = True
        while choosing_Team2_Size:
            hero_number = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Do you want to add a hero? (Y/N)")
            # every time I create a hero apppend that hero to the team
            if hero_number == "Yes" or hero_number ==  "yes" or hero_number == "y" or hero_number == "Y" :
                self.team_two.add_hero(self.create_hero())
                print(self.team_two.heroes)
            else:
                choosing_Team2_Size = False


    def team_battle(self):
        """
        This method should continue to battle teams until one or both teams are dead.
        """
        print("\n")
        print("{} vs. {}".format(self.team_one.name, self.team_two.name))
        in_battle = True

        while in_battle:
            if self.team_one.attack(self.team_two) == len(self.team_two.heroes):
                print("Team 1 Wins!!")
                in_battle = False
            else:
                if self.team_two.attack(self.team_one) == len(self.team_one.heroes):
                    print("Team 2 Wins!!")
                    in_battle = False
                else:
                    continue

    def show_stats(self):
        """
        This method should print out the battle statistics including each heroes kill/death ratio.
        """
        self.team_one.stats()
        self.team_two.stats()


if __name__ == "__main__":
    # created a variable and assigned a boolean value
    game_is_running = True

    # Instantiate Game Arena - Object
    arena = Arena()

    # Build Teams
    # calling a method
    arena.build_team_one()
    arena.build_team_two()

    # while condition is true run this code
    while game_is_running:
        # teams battle
        arena.team_battle()
        # show kill/death ratio of each hero
        arena.show_stats()
        # After game ask user do they want to play again
        play_again = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Play Again? Y or N: ")
        if play_again ==  "No" or play_again ==  "no" or play_again ==  "n" or play_again == "N":
            game_is_running = False

        else:
            recreate_teams = validator(["Yes","yes","y", "Y", "No", "no", "n", "N"],"Do you want new teams? (Y/N)")
            if recreate_teams == "y" or "Y" or "Yes" or "yes":
                arena.build_team_one()
                arena.build_team_two()
            else:
                # Revive heroes to play again
                # call function that resets all heroes to original value health
                arena.team_one.revive_heroes()
                arena.team_two.revive_heroes()
                
