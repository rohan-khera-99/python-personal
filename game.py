import random


# Setting the functions of the game
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# initializing variables and its functions
class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    # Setting the damages
    def gen_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    # Healing the person
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    # HP points
    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    # Magic points
    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    # Selecting players actions
    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for items in self.actions:
            print(str(i) + ':', items)
            i += 1

    # User magic
    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ':', spell.name, "cost:", str(spell.cost), "Points: ", str(spell.dmg))
            i += 1

    # User Item
    def choose_item(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print(str(i) + ':', item["item"].name + ":", item["item"].desc, "( x" + str(item["quantity"]) + ")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "   TARGET: " + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + "->" + enemy.name)
                i += 1
        choice = int(input("    Choose Target: ")) - 1
        return choice

    # Getting enemy stats
    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_str = str(self.hp) + "/" + str(self.maxhp)
        cur_hp = ""
        # To add blnk spaces in hp and mp points so that they stay in one line

        if len(hp_str) < 11:
            dec = 11 - len(hp_str)
            while dec > 0:
                cur_hp += " "
                dec -= 1
            cur_hp += hp_str
        else:
            cur_hp = hp_str

        print("                          __________________________________________________")
        print(bcolors.BOLD + self.name + ":     " +
              cur_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC  + "|")

    # Getting player stats

    def get_stats(self):
        mp_bar = ""
        bar_mp_ticks = (self.mp / self.maxmp) * 100 / 10
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        while bar_mp_ticks > 0:
            mp_bar += "█"
            bar_mp_ticks -= 1
        # Create empty spaces
        while len(mp_bar) < 10:
            mp_bar += " "

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        # Create empty spaces
        while len(hp_bar) < 25:
            hp_bar += " "

        hp_str = str(self.hp) + "/" + str(self.maxhp)
        cur_hp = ""
# To add blnk spaces in hp and mp points so that they stay in one line

        if len(hp_str) < 9:
            dec = 9 - len(hp_str)
            while dec > 0:
                cur_hp += " "
                dec -= 1
            cur_hp += hp_str
        else:
            cur_hp = hp_str

        mp_str = str(self.mp) + "/" + str(self.maxmp)
        cur_mp = ""
        if len(mp_str) < 7:
            dec = 7 - len(mp_str)
            while dec > 0:
                cur_mp += " "
                dec -= 1

            cur_mp += mp_str
        else:
            cur_mp = mp_str
        print("                        _________________________               __________")
        print(bcolors.BOLD + self.name + "      " +
              cur_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|     " +
             cur_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")

    #Enemy Spell
    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.gen_damage(self)

        #checking the enemy hp if below certain lvl use healing stuff
        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type =="white" and pct > 30:
            return self.choose_enemy_spell()
        else:
            return spell, magic_dmg
