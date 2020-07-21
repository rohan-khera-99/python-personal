from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random

# Black MAgic
fire = Spell("Fire", 20, 2563, "black")
thunder = Spell("Thunder", 37, 3652, "black")
meteor = Spell("Meteor", 46, 4521, "black")
wrath = Spell("Wrath", 54, 5845, "black")

# White magic
heal = Spell("Heal", 15, 1250, "white")
cure = Spell("Cure", 2, 2350, "white")

# Create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 75 HP", 75)
superpotion = Item("Super-Potion", "potion", "Heals 450 HP", 450)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP for member", 9999)
# Sab kuch full kar deta h but fir enemy attack kar deta h toh Hp/MP fir kam ho jate h.
hielixer = Item("Mega-Elixer", "elixer", "Fully restores team's HP/MP", 9999)
grenade = Item("Grenade", "attack", "Deals 450 damage.", 450)

player_spells = [fire, thunder, meteor, wrath, heal, cure]
enemy_spells = [fire, thunder, meteor, wrath, heal, cure]
player_items = [{"item": potion, "quantity": 3}, {"item": hipotion, "quantity": 3},
                {"item": superpotion, "quantity": 3}, {"item": elixer, "quantity": 1},
                {"item": hielixer, "quantity": 1}, {"item": grenade, "quantity": 3}]

# player instantiation
player1 = Person("Kratos:", 4500, 175, 453, 30, player_spells, player_items)
player2 = Person("Atreus:", 2500, 125, 354, 30, player_spells, player_items)
player3 = Person("ZEUS  :", 3750, 225, 255, 30, player_spells, player_items)

enemy1 = Person("Odin   ", 3510, 475, 640, 360, enemy_spells, [])
enemy2 = Person("THOR   ", 2256, 295, 425, 240, enemy_spells, [])
enemy3 = Person("Baulder", 1810, 180, 580, 420, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "Enemy Attacks!!!" + bcolors.ENDC)

while running:
    print("============================")

    # For multiple players Stats
    print("\n")
    print("NAME         HP                                      MP")

    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:

        # selecting user choice

        player.choose_action()
        choice = input("Choose Action")
        index = int(choice) - 1

        # setting up the attack and damage

        if index == 0:
            dmg = player.gen_dmg()
            # Enemy target defining
            enemy = player.choose_target(enemies)
            enemies[enemy].take_dmg(dmg)
            print("You attacked " + enemies[enemy].name + "for ", dmg, "points of damage")
            # deleting the enemy with 0 hp
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " Has fallen.")
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.gen_damage(i)

            current_mp = player.get_mp()
            # to check if we have req magic points or not
            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot Enough Magic Points\n", bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)
            #Spell damaging
            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "heals for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage to: "
                      + enemies[enemy].name + bcolors.ENDC)
            # deleting the enemy with 0 hp and its magic too.
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + "Has fallen.")
                del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose Item: ")) - 1

            if item_choice == -1:
                continue
            # Reducing item quantity
            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1
            # If item reaches 0

            # Setting up the items
            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + "heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "Mega-Elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "fully restores HP\MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_dmg(item.prop)
                enemy.take_dmg(item.prop)
                print(bcolors.FAIL + "\n" + item.name + "deals", str(item.prop),
                      "points of damage to" + enemies[enemy].name + bcolors.ENDC)
                # deleting the enemy with 0 hp
                if enemies[enemy].get_hp() == 0:
                    print(enemy[enemies].name + " Has fallen.")
                    del enemy[enemies]

        # HP reaches 0
        # check each character hp to 0 in order to win

    def_enemies = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            def_enemies += 1

    def_players = 0
    for player in players:
        if player.get_hp() == 0:
            def_players += 1

    if def_enemies == 2:
        print(bcolors.OKGREEN + 'You Win, Congratulations!!!', bcolors.ENDC)
        running = False
        break

    elif def_players == 2:
        print(bcolors.FAIL + "You lost!!!, Better luck next time.", bcolors.ENDC)
        running = False
        break

    print("\n")
    # Setting the enemies attacks and to also target the character. {enemy is object}
    for enemy in enemies :
        enemy_choice = random.randrange(0, 2)

        if enemy_choice == 0:
            target = random.randrange(0, 2)
            enemy_dmg = enemy.gen_dmg()
            players[target].take_dmg(enemy_dmg)
            print(enemy.name.replace(" ", "") + " attacks " + players[target].name.replace(" ", "") + " for ", enemy_dmg, " points of damage ")

        elif enemy_choice == 1:
            spell, magic_dmg = enemy.choose_enemy_spell()
            enemy.reduce_mp(spell.cost)

            if spell.type == "white":
                enemy.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + "heals" + enemy.name + "for", str(magic_dmg), "HP." + bcolors.ENDC)
            elif spell.type == "black":
                target = random.randrange(0, 3)
                players[target].take_dmg(magic_dmg)
                print(bcolors.OKBLUE + enemy.name.replace(" ", "") + "'s " + spell.name + " deals", str(magic_dmg), "points of damage to: "
                      + players[target].name + bcolors.ENDC)

                # deleting the player with 0 hp and its magic too.
            if players[target].get_hp() == 0:
                print(players[target].name.replace(" ", "") + "Has fallen.")
                del players[target]

            #print("Enemy chose ", spell, " damage = ", magic_dmg)

