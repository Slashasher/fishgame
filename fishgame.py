import pygame
import sys
import random
import time

pygame.init()
pygame.mixer.init()

cooldown_over = pygame.mixer.Sound('mixkit-game-success-alert-2039.wav')
def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    if minutes == 1:
        minute_str = "minute"
    else:
        minute_str = "minutes"
    return f"{minutes} {minute_str} {seconds} seconds"
def countdown_timer(seconds):
    for i in range(seconds, 0, -1):
        hours, remainder = divmod(i, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
        sys.stdout.write("\r{} Remaining...".format(time_str))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write(f"\rCooldown Over!                    \n")
    cooldown_over.play()
    sys.stdout.flush()
turtle = ('🐢')
watersnake = ('🐍')
whale = ('🐋')
dolphin = ('🐬')
tuna = ('🐟')
tropical = ('🐠')
pufferfish = ('🐡')
shark = ('🦈')
octopus = ('🐙')
crab = ('🦀')
lobster = ('🦞')
shrimp = ('🦐')
squid = ('🦑')
oyster = ('🦪')
fishes = {turtle: 'turtle', watersnake: 'watersnake', whale: 'whale', dolphin: 'dolphin',
tuna: 'tuna', tropical: 'tropical fish', pufferfish: 'pufferfish', shark: 'shark', octopus: 'octopus', 
crab: 'crab', lobster: 'lobster', shrimp: 'shrimp', squid: 'squid', oyster: 'oyster'}
fish = [turtle, watersnake, whale, dolphin, tuna, tropical, pufferfish,
         shark, octopus, crab, lobster, shrimp, squid, oyster]
fish_prices = {turtle: 2, watersnake: 3, whale: 5, dolphin: 4, tuna: 3, tropical: 2, pufferfish: 2,
                shark: 4, octopus: 4, crab: 3, lobster: 3, shrimp: 2, squid: 2, oyster: 2}

catchchance = 99
coins = 10
purchaseamount = 0
purchaseamount_int = int(purchaseamount)
cricketpurchase = 10 * purchaseamount_int
flypurchase = 8 * purchaseamount_int
wormpurchase = 6 * purchaseamount_int
crickets = 0
flies = 0
worms = 0
casts_stat = 0
fishcaught_stat = 0
traps_stat = 0
coins_stat = 0

ring_trash = '💍 - Ring - 5 coins'
toiletpaper_trash = '🧻 - Toilet Paper - 0 coins'
skull_trash = '💀 - Skull - 1 coins'
glasses_trash = '👓 - Glasses - 1 coin'
book_trash = '📕 - Book - 0 coins'
newspaper_trash = '🗞️  - Newspaper - 0 coins'
seaweed_trash = '🌿 - Seaweed - 0 coins'
rock_trash = '🪨  - Rock - 0 coins'
trash = [ring_trash, toiletpaper_trash, skull_trash, glasses_trash, book_trash, newspaper_trash, seaweed_trash, rock_trash,
          toiletpaper_trash, skull_trash, glasses_trash, book_trash, newspaper_trash, seaweed_trash, rock_trash]
inventory = []
fishinv = []
print('')
while True:
    
    print(f'\n[F]ish - [T]rap - [M]arket - [I]nventory - [S]tats - [H]elp')
    print('\033[2m(you cannot do anything during a cooldown for now, very sorry)\033[0m')
    choice = input('')
    print('\n-------------------------------------------------\n')
    if choice.lower() == '' or choice.lower() == 'f':
        fishcatch = random.randrange(len(fish))
        fishcaught = fish[fishcatch]
        fishes1 = fishes.get(fishcaught)
        casts_stat = casts_stat + 1
        if crickets == 0 and flies == 0 and worms == 0:
            catchchance = 99
        elif crickets >= 0:
            catchchance = 60
            crickets = crickets - 1
        elif flies >= 0:
            catchchance = 75
            flies = flies - 1
        elif worms >= 0:
            catchchance = 85
            worms = worms - 1
        catch = random.randint(0, catchchance)
        if fishcatch == 0:
            size = random.randint(10, 50)
        if fishcatch == 1:
            size = random.randint(30, 150)
        if fishcatch == 2:
            size = random.randint(300, 3000)
        if fishcatch == 3:
            size = random.randint(40, 180)
        if fishcatch == 4:
            size = random.randint(30, 60)
        if fishcatch == 5:
            size = random.randint(5, 30)
        if fishcatch == 6:
            size = random.randint(10, 30)
        if fishcatch == 7:
            size = random.randint(100, 1200)
        if fishcatch == 8:
            size = random.randint(30, 90)
        if fishcatch == 9:
            size = random.randint(5, 100)
        if fishcatch == 10:
            size = random.randint(20, 60)
        if fishcatch == 11:
            size = random.randint(1, 15)
        if fishcatch == 12:
            size = random.randint(15, 50)
        if fishcatch == 13:
            size = random.randint(5, 20)
        if catch == 0:
            fishcaught_stat = fishcaught_stat + 1
            fishinv.append(fishcaught)
            inventory.append(fishcaught)
            print(f'\033[32mYou caught a {size}cm ✨{fishcaught:}✨! ({fishes1})\033[0m')
            print('Cooldown: 1/2 Hour\n')
            countdown_seconds = 1800
            countdown_timer(countdown_seconds)
        else:
            print(f'\033[31mNo fish\033[0m\n')
            distance = random.randint(1, 1000)
            print(f'Your line landed {distance}cm away from you...\n')
            random_cooldown_seconds = random.randint(30, 90)
            formatted_time = format_time(random_cooldown_seconds)
            print(f'Cooldown: {formatted_time}\n')
            countdown_timer(random_cooldown_seconds)
        catchchance = 99
        print('\n-------------------------------------------------')
    
    if choice.lower() == 't':
        print('You laid out your traps')
        countdown_seconds = 3600
        traps_stat = traps_stat + 1
        print(f'Cooldown: 1 Hour\n')
        countdown_timer(countdown_seconds)
        catch = random.randint(0, 50)
        if catch == 0:
            trash1 = random.randrange(len(trash))
            trash11 = trash[trash1]
            inventory.append(trash11)
            trash2 = random.randrange(len(trash))
            trash22 = trash[trash2]
            inventory.append(trash22)
            trash3 = random.randrange(len(trash))
            trash33 = trash[trash3]
            inventory.append(trash33)
            trash4 = random.randrange(len(trash))
            trash44 = trash[trash4]
            inventory.append(trash44)
            trash5 = random.randrange(len(trash))
            trash55 = trash[trash5]
            inventory.append(trash55)
            fishcatch = random.randrange(len(fish))
            fishcaught = fish[fishcatch]
            inventory.append(fishcaught)
            fishinv.append(fishcaught)
            trash6 = random.randrange(len(trash))
            trash66 = trash[trash6]
            inventory.append(trash66)
            trash7 = random.randrange(len(trash))
            trash77 = trash[trash7]
            inventory.append(trash77)
            trash8 = random.randrange(len(trash))
            trash88 = trash[trash8]
            inventory.append(trash88)
            trash9 = random.randrange(len(trash))
            trash99 = trash[trash9]
            inventory.append(trash99)
            print('You got...')
            print(f'{trash11, trash22, trash33, trash44, trash55,fishcaught, trash66, trash77, trash88, trash99}')
            print('\n-------------------------------------------------')
        else:
            trash1 = random.randrange(len(trash))
            trash11 = trash[trash1]
            inventory.append(trash11)
            trash2 = random.randrange(len(trash))
            trash22 = trash[trash2]
            inventory.append(trash22)
            trash3 = random.randrange(len(trash))
            trash33 = trash[trash3]
            inventory.append(trash33)
            trash4 = random.randrange(len(trash))
            trash44 = trash[trash4]
            inventory.append(trash44)
            trash5 = random.randrange(len(trash))
            trash55 = trash[trash5]
            inventory.append(trash55)
            trash6 = random.randrange(len(trash))
            trash66 = trash[trash6]
            inventory.append(trash66)
            trash7 = random.randrange(len(trash))
            trash77 = trash[trash7]
            inventory.append(trash77)
            trash8 = random.randrange(len(trash))
            trash88 = trash[trash8]
            inventory.append(trash88)
            trash9 = random.randrange(len(trash))
            trash99 = trash[trash9]
            inventory.append(trash99)
            trash10 = random.randrange(len(trash))
            trash1010 = trash[trash10]
            inventory.append(trash1010)
            print('You got...')
            print(f'{trash11}\n{trash22}\n{trash33}\n{trash44}\n{trash55}\n{trash66}\n{trash77}\n{trash88}\n{trash99}\n{trash1010}')
            print('\n-------------------------------------------------')

    if choice.lower() == 'm':
        print('\nDo you want to...')
        print('\nBuy: [B]ait')
        print('Sell: [F]ish [P]awn shop\n')
        choice = input('')
        print('\n-------------------------------------------------\n')

        if choice.lower() == 'p':
            print(f'\033[4m\033[1m- Available Junk -\033[0m')
            for trashes in sorted(inventory):
                print(f'{trashes}')
            print('\nWhat would you like to sell?')
            print('\033[2mtype the trash name or click enter to not sell anything and exit (ex: seaweed)\033[0m')
            choice = input('')
            print('')
            if choice.lower() == '':
                print('\r')
            elif choice.lower() == 'ring':
                if ring_trash in inventory:
                    inventory.remove(ring_trash)
                    coins = coins + 5
                    coins_stat = coins_stat + 5
                    print('You sold your ring')
                    print('+5 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            elif choice.lower() == 'toiletpaper':
                if toiletpaper_trash in inventory:
                    inventory.remove(toiletpaper_trash)
                    print('You sold your toiletpaper')
                    print('+0 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            elif choice.lower() == 'skull':
                if skull_trash in inventory:
                    inventory.remove(skull_trash)
                    coins = coins + 1
                    coins_stat = coins_stat + 1
                    print('You sold your skull')
                    print('+1 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            elif choice.lower() == 'glasses':
                if glasses_trash in inventory:
                    inventory.remove(glasses_trash)
                    coins = coins + 1
                    coins_stat = coins_stat + 1
                    print('You sold your book')
                    print('+1 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            elif choice.lower() == 'book':
                if book_trash in inventory:
                    inventory.remove(book_trash)
                    print('You sold your book')
                    print('+0 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            elif choice.lower() == 'newspaper':
                if newspaper_trash in inventory:
                    inventory.remove(newspaper_trash)
                    print('You sold your newspaper')
                    print('+0 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            elif choice.lower() == 'seaweed':
                if seaweed_trash in inventory:
                    inventory.remove(seaweed_trash)
                    print('You sold your seaweed')
                    print('+0 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            elif choice.lower() == 'rock':
                if rock_trash in inventory:
                    inventory.remove(rock_trash)
                    print('You sold your rock')
                    print('+0 coins')
                else:
                    print('\033[31mYou do not have that piece of trash...\033[0m')
            print('\n-------------------------------------------------')


        if choice.lower() == 'f':
            print(f'\033[4m\033[1m- Available Fish -\033[0m')
            for fish in sorted(fishinv):
                if fish in fishes:
                    fishinv_name = fishes[fish]
                    if fish in fish_prices:
                        fish_price = fish_prices[fish]
                        print(f'{fish} - {fishinv_name.title()} - {fish_price} coins')
            print('\nWhat would you like to sell?')
            print('\033[2mtype the fish name or click enter to not sell anything and exit (ex: turtle)\033[0m')
            choice = input('')
            print('')
            if choice.lower() == '':
                print('\r')
            elif choice.lower() == 'turtle':
                if turtle in fishinv:
                    fishinv.remove(turtle)
                    coins = coins + 4
                    coins_stat = coins_stat + 4
                    print('You sold your turtle')
                    print('+4 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'watersnake':
                if watersnake in fishinv:
                    fishinv.remove(watersnake)
                    coins = coins + 6
                    coins_stat = coins_stat + 6
                    print('You sold your watersnake')
                    print('+6 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'whale':
                if whale in fishinv:
                    fishinv.remove(whale)
                    coins = coins + 10
                    coins_stat = coins_stat + 10
                    print('You sold your whale')
                    print('+10 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'dolphin':
                if dolphin in fishinv:
                    fishinv.remove(dolphin)
                    coins = coins + 8
                    coins_stat = coins_stat + 8
                    print('You sold your dolphin')
                    print('+8 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'tuna':
                if tuna in fishinv:
                    fishinv.remove(tuna)
                    coins = coins + 6
                    coins_stat = coins_stat + 6
                    print('You sold your tuna')
                    print('+6 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'tropical fish' or choice.lower() == 'tropical':
                if tropical in fishinv:
                    fishinv.remove(tropical)
                    coins = coins + 4
                    coins_stat = coins_stat + 4
                    print('You sold your tropical fish')
                    print('+4 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'pufferfish':
                if pufferfish in fishinv:
                    fishinv.remove(pufferfish)
                    coins = coins + 4
                    coins_stat = coins_stat + 4
                    print('You sold your pufferfish')
                    print('+4 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'shark':
                if shark in fishinv:
                    fishinv.remove(shark)
                    coins = coins + 8
                    coins_stat = coins_stat + 8
                    print('You sold your shark')
                    print('+8 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'octopus':
                if octopus in fishinv:
                    fishinv.remove(octopus)
                    coins = coins + 8
                    coins_stat = coins_stat + 8
                    print('You sold your octopus')
                    print('+8 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'crab':
                if crab in fishinv:
                    fishinv.remove(crab)
                    coins = coins + 6
                    coins_stat = coins_stat + 6
                    print('You sold your crab')
                    print('+6 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'lobster':
                if lobster in fishinv:
                    fishinv.remove(lobster)
                    coins = coins + 6
                    coins_stat = coins_stat + 6
                    print('You sold your lobster')
                    print('+6 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'shrimp':
                if shrimp in fishinv:
                    fishinv.remove(shrimp)
                    coins = coins + 4
                    coins_stat = coins_stat + 4
                    print('You sold your shrimp')
                    print('+4 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'squid':
                if squid in fishinv:
                    fishinv.remove(squid)
                    coins = coins + 4
                    coins_stat = coins_stat + 4
                    print('You sold your squid')
                    print('+4 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            elif choice.lower() == 'oyster':
                if oyster in fishinv:
                    fishinv.remove(oyster)
                    coins = coins + 4
                    coins_stat = coins_stat + 4
                    print('You sold your oyster')
                    print('+4 coins')
                else:
                    print('\033[31mYou do not have that fish...\033[0m')
            print('\n-------------------------------------------------')
        
        if choice.lower() == 'b':
            print('Available baits:')
            print('\n[C]ricket 🦗 - 10 coins\n[F]ly 🪰 - 8 coins\n[W]orm 🪱 - 6 coins')
            print('\033[2m(Bait is used immediately after purchase)\033[0m')
            choice = input('')
            print('\n-------------------------------------------------')

            if choice.lower() == 'c':
                if coins >= 10:
                    print('\nHow many would you like to purchase?')
                    purchaseamount = input('')
                    purchaseamount_int = int(purchaseamount)
                    cricketpurchase = 10 * purchaseamount_int
                    if coins >= purchaseamount_int * 10:
                        print('\nAre you sure? [y/n]')
                        print(f'\033[2mThis will cost {cricketpurchase} coins, you have {coins} coins\033[0m')
                        choice = input('')
                        if choice.lower() == 'y':
                            coins = coins - cricketpurchase
                            print(f'\n\033[32mYou have bought {purchaseamount_int} crickets\033[0m')
                            crickets = crickets + purchaseamount_int
                    else:
                        print('\n\033[31mSorry, you cannot afford this many crickets right now...\033[0m')
                        print(f'\033[2mYou have {coins} coins...\033[0m')
                else:
                    print('\033[31mSorry, you cannot afford a cricket right now...\033[0m')
                print('\n-------------------------------------------------')
            
            if choice.lower() == 'f':
                if coins >= 8:
                    print('\nHow many would you like to purchase?')
                    purchaseamount = input('')
                    purchaseamount_int = int(purchaseamount)
                    flypurchase = 8 * purchaseamount_int
                    if coins >= purchaseamount_int * 8:
                        print('\nAre you sure? [y/n]')
                        print(f'\033[2mThis will cost {flypurchase} coins, you have {coins} coins\033[0m')
                        choice = input('')
                        if choice.lower() == 'y':
                            coins = coins - flypurchase
                            print(f'\n\033[32mYou have bought {purchaseamount_int} flies\033[0m')
                            flies = flies + purchaseamount_int
                    else:
                        print('\n\033[31mSorry, you cannot afford this many flies right now...\033[0m')
                        print(f'\033[2mYou have {coins} coins...\033[0m')
                else:
                    print('\033[31mSorry, you cannot afford a fly right now...\033[0m')
                print('\n-------------------------------------------------')

            if choice.lower() == 'w':
                if coins >= 6:
                    print('\nHow many would you like to purchase?')
                    purchaseamount = input('')
                    purchaseamount_int = int(purchaseamount)
                    wormpurchase = 6 * purchaseamount_int
                    if coins >= purchaseamount_int * 8:
                        print('\nAre you sure? [y/n]')
                        print(f'\033[2mThis will cost {wormpurchase} coins, you have {coins} coins\033[0m')
                        choice = input('')
                        if choice.lower() == 'y':
                            coins = coins - wormpurchase
                            print(f'\n\033[32mYou have bought {purchaseamount_int} worm(s)\033[0m')
                            worms = worms + purchaseamount_int
                    else:
                        print('\n\033[31mSorry, you cannot afford this many worms right now...\033[0m')
                        print(f'\033[2mYou have {coins} coins...\033[0m')
                else:
                    print('\033[31mSorry, you cannot afford a worm right now...\033[0m')
                print('\n-------------------------------------------------')
    
    if choice.lower() == 's':
        print('\033[4m\033[1m- Statistics -\033[0m')
        print(f'\nFish Caught - {fishcaught_stat}')
        print(f'Casts - {casts_stat}')
        print(f'Traps Placed - {traps_stat}')
        print(f'Coins Earned - {coins_stat}')
        print('\n-------------------------------------------------')
    
    if choice.lower() == 'h':
        print('\033[1m\033[4m- Fishing -\033[0m')
        print('\nTo fish, type "f" in the main menu.\n')
        print('When fishing, there is a 1/100 chance to catch a fish,')
        print('this chance can be lowered by buying bait.\n')
        print('If you miss a fish, you have to wait between 1 and 2 minutes.\n')
        
        print('\033[1m\033[4m- Fish Traps -\033[0m')
        print('\nTo lay out your fishing traps, type "t" in the main menu.\n')
        print('You have to wait 1 hour after laying out the trap for it to become full,')
        print('it is then automatically pulled out of the water.\n')
        print('There is also a 1/100 chance to catch a fish from a trap.\n')

        print('\033[1m\033[4m- Market -\033[0m')
        print('\nYou can buy bait and upgrades in the market,')
        print('you can also sell fish and junk via the pawn shop\n')

        print('\033[1m\033[4m- Statistics -\033[0m')
        print('\nThis shows statistics from the game.')
        print('\n-------------------------------------------------')

    if choice.lower() == 'i':
        print('\033[4m\033[1m- Inventory -\n\033[0m')
        print('[F]ish - [J]unk')
        choice = input()
        if choice.lower() == 'j':
            print('\n-------------------------------------------------\n')
            print('\n\033[4m\033[1m- Junk Inventory -\n\033[0m')
            for item in sorted(inventory):
                print(item)
        elif choice.lower() == 'f':
            print('\n-------------------------------------------------\n')
            print('\n\033[4m\033[1m- Fish Inventory -\n\033[0m')
            for fish in sorted(fishinv):
                if fish in fishes:
                    fishinv_name = fishes[fish]
                    if fish in fish_prices:
                        fish_price = fish_prices[fish]
                        print(f'{fish} - {fishinv_name.title()} - {fish_price} coins')
        print('\n-------------------------------------------------')
    catchchance = 99

print('Game has ended for some reason')
pygame.quit()