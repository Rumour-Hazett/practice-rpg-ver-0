'''

  .-')        ('-.      ('-.
 ( OO ).    _(  OO)    ( OO ).-.
(_)---\_)  (,------.   / . --. /
/    _ |    |  .---'   | \-.  \
\  :` `.    |  |     .-'-'  |  |
 '..`''.)  (|  '--.   \| |_.'  |
.-._)   \   |  .--'    |  .-.  |
\       /.-.|  `---..-.|  | |  |.-.
 `-----' `-'`------'`-'`--' `--'`-'

A crappy game by J. Maddox.
ver 0.0.1
12-30-2017
the.session04

'''

from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random
print(bcolors.HEADER + bcolors.FAIL + '''
  .-')        ('-.      ('-.        
 ( OO ).    _(  OO)    ( OO ).-.    
(_)---\_)  (,------.   / . --. /    
/    _ |    |  .---'   | \-.  \     
\  :` `.    |  |     .-'-'  |  |    
 '..`''.)  (|  '--.   \| |_.'  |    
.-._)   \   |  .--'    |  .-.  |    
\       /.-.|  `---..-.|  | |  |.-. 
 `-----' `-'`------'`-'`--' `--'`-' 
    ''')
print(bcolors.HEADER + bcolors.FAIL + bcolors.BOLD + "SOME ENEMIES ATTACK!" + bcolors.ENDC)
print('''A crappy game by J. Maddox.
ver 0.0.1
12-30-2017
the.session'''+ bcolors.OKGREEN + "04" + bcolors.ENDC)
# Create Black magic
fire = Spell("Fire", 25, 600, "black")
thunder = Spell("Thunder", 25, 600, "black")
blizzard = Spell("Blizzard", 25, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create White magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 32, 1500, "white")
curaga = Spell("Curaga", 73, 6000, "white")

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP.", 50, 15)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP.", 100, 5)
superpotion = Item("SuperPotion", "potion", "Heals 500 HP.", 500, 3)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member.", 9999, 3)
hielixir = Item("MegaElixir", "elixir", "Fully restores the HP/MP of the whole party.", 9999, 2)

grenade = Item("Grenade", "attack", "Deals 500 points of explosive damage.", 500, 10)

player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"name": "Potion", "type": "potion", "quantity": 15,
                 "description": "Heals 50 HP.", "prop": 50},
                {"name": "Hi-Potion", "type": "potion", "quantity": 5,
                 "description": "Heals 100 HP.", "prop": 100},
                {"name": "SuperPotion", "type": "potion", "quantity": 3,
                 "description": "Heals 500 HP.", "prop": 500},
                {"name": "Elixir", "type": "elixir", "quantity": 3,
                 "description": "Fully restores HP/MP of one party member.", "prop": 9999},
                {"name": "MegaElixir", "type": "elixir", "quantity": 2,
                 "description": "Fully restores the HP/MP of the whole party.", "prop": 9999},
                {"name": "Grenade", "type": "attack", "quantity": 10,
                 "description": "Deals 500 points of explosive damage.", "prop": 500}]

# Instantiate characters
player1 = Person("Valos:", 3260, 132, 300, 34, player_magic, player_items)
player2 = Person("Nick :", 4160, 188, 311, 34, player_magic, player_items)
player3 = Person("Robot:", 3089, 174, 288, 34, player_magic, player_items)
players = [player1, player2, player3]

enemy1 = Person("Datway:", 11200, 701, 525, 25, [fire, meteor, curaga], [])
enemy2 = Person("Imp   :", 1250, 130, 560, 325, [fire, cura], [])
enemy3 = Person("Imp   :", 1250, 130, 560, 325, [fire, cura], [])
enemies = [enemy1, enemy2, enemy3]

running = True
while running:
    print("======================")
    print("NAME                     HP                                      MP")

    for enemy in enemies:
        enemy.get_enemy_stats()
    print("")
    for p in players:
        p.get_stats()
    for player in players:
        '''if player.living is not True:
            continue'''
        while True:
            player.choose_action()
            try:
                choice = int(input("Choose action: "))
            except ValueError:
                print(bcolors.FAIL + bcolors.BOLD + "Please enter an option number." + bcolors.ENDC)
                continue
            else:
                index = choice - 1
                if index > len(player.actions) or index < 0:
                    print(bcolors.FAIL + bcolors.BOLD +
                          "Invalid option chosen. Please enter a valid option number." + bcolors.ENDC)
                    continue
                if index == 1:
                    lowest_cost = 9999
                    for m in player.magic:
                        if m.cost < lowest_cost:
                            lowest_cost = m.cost
                    if lowest_cost > player.mp:
                        print(bcolors.FAIL + bcolors.BOLD + player.name.split(":")[0].rstrip(),
                              "does not have enough MP to use any magic! Please choose again." + bcolors.ENDC)
                        continue
                    break
                break

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print(player.name.split(":")[0].rstrip(), "used a basic attack against",
                  enemies[enemy].name.split(":")[0].rstrip(), "for", str(dmg), "points of damage.",
                  enemies[enemy].name.split(":")[0].rstrip() + "'s", "HP:", str(enemies[enemy].get_hp()) +
                  ".")
            if enemies[enemy].get_hp() == 0:
                print(bcolors.OKGREEN + player.name.split(":")[0].rstrip(),
                      "has defeated", enemies[enemy].name.split(":")[0].rstrip() +
                      ". He dead!" + bcolors.ENDC)
                del enemies[enemy]
        elif index == 1:
            while True:
                player.choose_magic()
                try:
                    magic_choice = int(input("Choose magic: "))
                except ValueError:
                    print(bcolors.FAIL + bcolors.BOLD + "Please enter an option number." + bcolors.ENDC)
                    continue
                else:
                    magic_choice -= 1
                    if magic_choice > len(player.magic) or magic_choice < 0:
                        print(bcolors.FAIL + bcolors.BOLD +
                              "Invalid option chosen. Please enter a valid option number." + bcolors.ENDC)
                        continue
                    spell = player.magic[magic_choice]
                    magic_dmg = spell.generate_damage()

                    current_mp = player.get_mp()

                    if spell.cost > current_mp:
                        print(bcolors.FAIL + player.name.split(":")[0].rstrip(),
                              "does not have enough MP for this spell." + bcolors.ENDC)
                        continue

                    player.reduce_mp(spell.cost)

                    if spell.type == "white":
                        player.heal(magic_dmg)
                        print(bcolors.OKBLUE + spell.name, "heals for", str(magic_dmg),
                              "HP.", player.name.split(":")[0].rstrip() + "'s", "HP:",
                              str(player.get_hp()) + "." + bcolors.ENDC)
                        break
                    elif spell.type == "black":
                        enemy = player.choose_target(enemies)
                        enemies[enemy].take_damage(magic_dmg)
                        print(bcolors.WARNING + player.name.split(":")[0].rstrip(), "attacked",
                              enemies[enemy].name.split(":")[0].rstrip(), "with the", spell.name, "spell for",
                              str(magic_dmg), "points of damage.", enemies[enemy].name.split(":")[0].rstrip() + "'s",
                              "HP:", str(enemies[enemy].get_hp()) + "." + bcolors.ENDC)
                        if enemies[enemy].get_hp() == 0:
                            print(bcolors.OKGREEN + player.name.split(":")[0].rstrip(),
                                  "has defeated", enemies[enemy].name.split(":")[0].rstrip() +
                                  ". He dead!" + bcolors.ENDC)
                            del enemies[enemy]
                        break
        elif index == 2:
            player.choose_item()
            while True:
                try:
                    item_choice = int(input("Choose action: "))
                except ValueError:
                    print("Please enter an option number.")
                    continue
                item_choice -= 1
                if item_choice > len(player_items) or item_choice < 0:
                    print(bcolors.FAIL + bcolors.BOLD +
                          "Invalid option chosen. Please enter a valid option number." + bcolors.ENDC)
                    continue
                item = player.items[item_choice]
                if item["quantity"] == 0:
                    print(bcolors.FAIL + player.name.split(":")[0].rstrip(),
                          "doesn't have any more of that item." + bcolors.ENDC)
                    continue
                else:
                    break

            if item["type"] == "potion":
                player.heal(item["prop"])
                print(bcolors.OKGREEN + item["name"], "heals",
                      player.name.split(":")[0].rstrip(), "for", str(item["prop"]), "HP.",
                      player.name.split(":")[0].rstrip() + "'s", "HP:", str(player.get_hp()) +
                      "." + bcolors.ENDC)
            elif item["type"] == "elixir":
                if item["name"] == "MegaElixir":
                    print(bcolors.OKGREEN + player.name.split(":")[0].rstrip() + "'s",
                          item["name"], "fully restores everyone's HP/MP." + bcolors.ENDC)
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                        print(bcolors.OKGREEN + i.name.split(":")[0].rstrip() +
                              "'s HP/MP are fully restored." + bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + item["name"], "fully restores",
                          player.name.split(":")[0].rstrip() + "'s HP/MP." + bcolors.ENDC)
            elif item["type"] == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item["prop"])
                print(bcolors.FAIL + player.name.split(":")[0].rstrip() + "'s",
                      item["name"], "deals", str(item["prop"]), "points of damage to",
                      enemies[enemy].name.split(":")[0].rstrip() + ".",
                      enemies[enemy].name.split(":")[0].rstrip() + "'s",
                      "HP:", str(enemy.get_hp()) +
                      "." + bcolors.ENDC)
                if enemies[enemy].get_hp() == 0:
                    print(bcolors.OKGREEN + player.name.split(":")[0].rstrip(),
                          "has defeated", enemies[enemy].name.split(":")[0].rstrip() +
                          ". He dead!" + bcolors.ENDC)
                    del enemies[enemy]
            item["quantity"] -= 1
        else:
            print(bcolors.FAIL + bcolors.BOLD +
                  "Invalid option chosen. Please enter a valid option number." + bcolors.ENDC)
            continue
        # Check if battle is over
        defeated_enemies = 0
        defeated_players = 0

        for e in enemies:
            if e.get_hp() == 0:
                defeated_enemies += 1

        for p in players:
            if p.get_hp() == 0:
                defeated_players += 1
        # Check if player won
        if defeated_enemies == len(enemies):
            print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
            running = False
            break
        # Check if enemy won
        elif defeated_players == len(players):
            print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
            running = False
            break

        # Enemy attack phase
        for enemy in enemies:
            while True:
                enemy_choice = random.randrange(0, 2)
                if len(players) == 0:
                    break
                target = random.randrange(0, len(players))

                if enemy_choice == 1:
                    lowest_cost = 9999
                    for m in enemy.magic:
                        if m.cost < lowest_cost:
                            lowest_cost = m.cost
                    if lowest_cost > enemy.mp:
                        continue
                    break
                break
            if enemy_choice == 0:
                enemy_dmg = enemy.generate_damage()
                players[target].take_damage(enemy_dmg)
                print(enemy.name.split(":")[0].rstrip(), "attacks",
                      players[target].name.split(":")[0].rstrip(), "for",
                      str(enemy_dmg), "points of damage.", players[target].name.split(":")[0].rstrip() + "'s",
                      "HP:", str(players[target].get_hp()) + ".")
                if players[target].get_hp() == 0:
                    print(bcolors.FAIL + players[target].name.split(":")[0].rstrip(), "was defeated by",
                          enemy.name.split(":")[0].rstrip() + "!" + bcolors.ENDC)
                    del players[target]
                    # players[target].living = False
            elif enemy_choice == 1:
                enemy_spell, enemy_magic_dmg = enemy.choose_enemy_spell()
                if enemy_spell.type == "black":
                    players[target].take_damage(enemy_magic_dmg)
                    print(enemy.name.split(":")[0].rstrip(), "chose the", enemy_spell.name, "spell and did",
                          str(enemy_magic_dmg), "points of damage to", players[target].name.split(":")[0].rstrip() +
                          ".", players[target].name.split(":")[0].rstrip() + "'s", "HP:", str(players[target].get_hp()) + ".")
                    if players[target].get_hp() == 0:
                        print(bcolors.FAIL + players[target].name.split(":")[0].rstrip(), "was defeated by",
                              enemy.name.split(":")[0].rstrip() + "!" + bcolors.ENDC)
                        del players[target]
                        # players[target].living = False
                elif enemy_spell.type == "white":
                    enemy.heal(enemy_magic_dmg)
                    print(bcolors.OKBLUE + enemy.name.split(":")[0].rstrip(), "chose", enemy_spell.name,
                          "and heals for", str(enemy_magic_dmg), "HP.", enemy.name.split(":")[0].rstrip() +
                          "'s", "HP:", str(enemy.get_hp()) + "." +
                          bcolors.ENDC)

        # Check if battle is over
        defeated_enemies = 0
        defeated_players = 0

        for e in enemies:
            if e.get_hp() == 0:
                defeated_enemies += 1

        for p in players:
            if p.get_hp() == 0:
                defeated_players += 1
        # Check if player won
        if defeated_enemies == len(enemies):
            print(bcolors.HEADER + bcolors.OKGREEN + "You win!" + bcolors.ENDC)
            print(bcolors.HEADER + bcolors.OKBLUE + '''
                                      _ .-') _                             .-. .-')  ,---.         _ .-') _   
                                     ( (  OO) )                            \  ( OO ) |   |        ( (  OO) )  
  ,----.     .-'),-----.  .-'),-----. \     .'_            ,--. .-'),-----. ;-----.\ |   |      .-.\     .'_  
 '  .-./-') ( OO'  .-.  '( OO'  .-.  ',`'--..._)       .-')| ,|( OO'  .-.  '| .-.  | |   |      `-',`'--..._) 
 |  |_( O- )/   |  | |  |/   |  | |  ||  |  \  '      ( OO |(_|/   |  | |  || '-' /_)|   |         |  |  \  ' 
 |  | .--, \\_) |  |\|  |\_) |  |\|  ||  |   ' |      | `-'|  |\_) |  |\|  || .-. `. |  .'      .-.|  |   ' | 
(|  | '. (_/  \ |  | |  |  \ |  | |  ||  |   / :      ,--. |  |  \ |  | |  || |  \  |`--'       `-'|  |   / : 
 |  '--'  |    `'  '-'  '   `'  '-'  '|  '--'  /      |  '-'  /   `'  '-'  '| '--'  /.--.          |  '--'  / 
  `------'       `-----'      `-----' `-------'        `-----'      `-----' `------' '--'          `-------'  
            ''')
            running = False
            break
        # Check if enemy won
        elif defeated_players == len(players):
            print(bcolors.HEADER + bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
            print(bcolors.HEADER + bcolors.FAIL + '''
  .-')                _  .-')  _  .-')                          ,-. 
 ( OO ).             ( \( -O )( \( -O )                        /  | 
(_)---\_) .-'),-----. ,------. ,------.   ,--.   ,--.      .-.'  .' 
/    _ | ( OO'  .-.  '|   /`. '|   /`. '   \  `.'  /       `-'|  |  
\  :` `. /   |  | |  ||  /  | ||  /  | | .-')     /           |  |  
 '..`''.)\_) |  |\|  ||  |_.' ||  |_.' |(OO  \   /         .-.|  |  
.-._)   \  \ |  | |  ||  .  '.'|  .  '.' |   /  /\_        `-''  '. 
\       /   `'  '-'  '|  |\  \ |  |\  \  `-./  /.__)           \  | 
 `-----'      `-----' `--' '--'`--' '--'   `--'                 `-' 
                ''')
            running = False
            break

        '''print("----------------------------")
        print("Enemy HP:", bcolors.FAIL + str(enemies[enemy].get_hp()) + "/" +
              str(enemies[enemy].get_max_hp()) + "." + bcolors.ENDC)

        print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + "." + bcolors.ENDC)
        print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + "."+ bcolors.ENDC)'''



