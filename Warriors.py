import random
import sys  # for ASCII art
import matplotlib.pyplot as plt  # for image display
from colorama import init  # for the ASCII art
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint, colored  # for the ASCII art
from pyfiglet import figlet_format  # for the ASCII art

MEDICINE_CATS = 'medicine_cats.txt'
FORAGEABLE_ITEMS = 'forageable_items.txt'
FORAGEABLE_LOCATIONS = 'forageable_locations.txt'
INJURED_WARRIORS = 'injured_warriors.txt'
INJURIES = 'injuries.txt'

LEAFPOOL = 'images/Leafpool.jpg'
CINDERPELT = 'images/Cinderpelt.jpg'
JAYFEATHER = 'images/Jayfeather.jpg'
SPOTTEDLEAF = 'images/Spottedleaf.jpg'



def main():
    cprint(figlet_format('WARRIORS!', font='catwalk', width=100), 'cyan', attrs=['bold'])
    cprint(figlet_format('Medicine Cat', font='standard'), 'yellow', attrs=['bold'])
    display_introduction()
    display_medicine_cats()
    medicine_cats = make_file_list(MEDICINE_CATS)
    medicine_cat = inputNumber("Which cat would you like to be?: ")
    medicine_cat -= 1  # to align input with list
    while 0 > medicine_cat or medicine_cat > (len(medicine_cats)-1):
        medicine_cat = inputNumber("Please select one of the available medicine cats: ")
        medicine_cat -= 1
    medicine_cat = medicine_cats[medicine_cat]
    print("Great! You've chosen " + medicine_cat + "!")
    # should modify the below code to a txt file for expansion
    if medicine_cat == 'Leafpool':
        leafpool = plt.imread(LEAFPOOL)
        show_image(leafpool, medicine_cat)
    elif medicine_cat == 'Jayfeather':
        jayfeather = plt.imread(JAYFEATHER)
        show_image(jayfeather, medicine_cat)
    elif medicine_cat == 'Cinderpelt':
        cinderpelt = plt.imread(CINDERPELT)
        show_image(cinderpelt, medicine_cat)
    elif medicine_cat == 'Spottedleaf':
        spottedleaf = plt.imread(SPOTTEDLEAF)
        show_image(spottedleaf, medicine_cat)
    input("Press Enter To Continue:")
    inventory = [0, 0, 0, 0]
    healed_cats = 0
    # while loop to display options until goal of 3 healed cats is reached
    while healed_cats <= 2:
        print("\nYou have healed " + str(healed_cats) + " Warriors!\n")
        display_choices(medicine_cat)
        choice = inputNumber("Please choose which activity you'd like to do: ")
        if choice >= 0 and choice < 4:
            if choice == 1:
                print("You've chosen to view your inventory.\n")
                show_inventory(inventory)
                input("Press Enter To Continue:")
            elif choice == 2:
                print("You've chosen to forage for medicine.\n")
                forage(inventory)
                input("Press Enter To Continue:")
            elif choice == 3:
                print("You've chosen to heal an injured warrior.\n")
                healed_cats = heal_warriors(inventory, healed_cats)
                input("Press Enter To Continue:")
            else:
                break
    print("You've healed all of the injured Warriors! You are a fantastic Medicine Cat!")
    cprint(figlet_format('YOU WIN!', font='standard'), 'yellow', attrs=['bold'])


def display_introduction():
    print("This is a game of the book series WARRIORS! Written by Erin Hunter. The goal of this game is to heal\n"
          "three warrior cats. You are a medicine cat, a healer in the clan, who take care of the warriors, the cats\n"
          "who hunt and fight. You have three options: Forage for medicines, showing your inventory of medicine\n"
          "you've already collected, and healing wounded warrior cats. In this game you will explore the life of the\n"
          "medicine cat, collect herbs, and find where they grow. All in this game, Warriors: Medicine Cat.\n")


def display_medicine_cats():
    print("Choose which medicine cat you'd like to be: ")
    print("1. Jayfeather \n2. Cinderpelt \n3. Leafpool \n4. Spottedleaf")


def display_choices(medicine_cat):
    print(medicine_cat + " what would you like to do? Show inventory, Forage, or Heal.")
    print("1. Show inventory \n2. Forage for medicine \n3. Heal an injured warrior")


# simple display of inventory list
def show_inventory(inventory):
    forageable_items = make_file_list(FORAGEABLE_ITEMS)
    for i in range(len(forageable_items)):
        print(forageable_items[i],  inventory[i])


# forage function that takes in inventory list and modifies it
def forage(inventory):
    forageable_items = make_file_list(FORAGEABLE_ITEMS)
    forageable_locations = make_file_list(FORAGEABLE_LOCATIONS)
    for i in range(len(forageable_items)):
        print(i+1, ". ", forageable_items[i], sep="")
    selected_medicine = inputNumber("Which medicine would you like to forage? ")
    selected_medicine -= 1
    while 0 > selected_medicine or selected_medicine > (len(forageable_items) - 1):
        selected_medicine = inputNumber("Which medicine would you like to forage? ")
        selected_medicine -= 1
    while True:
        print("You search " + forageable_locations[selected_medicine] + " for " + forageable_items[selected_medicine])
        forageable_image = 'images/' + forageable_items[selected_medicine] + '.jpg'
        # coin flip for result returns either 0 or 1, converts bit to boolean
        random_bit = random.getrandbits(1)
        random_choice = bool(random_bit)
        if random_choice:
            print("Your search was a", colored('success!', 'green'), "You found the " + forageable_items[selected_medicine])
            image = plt.imread(forageable_image)
            show_image(image, forageable_items[selected_medicine])
            inventory[selected_medicine] += 1
            return inventory
        else:
            print("You", colored('failed', 'red'), "to find the " + forageable_items[selected_medicine])
            return inventory


# heal warrior function takes in inventory list and healed_cats variable. result of healing injured warrior deducts from
# inventory and adds to healed_cats
def heal_warriors(inventory, healed_cats):
    warriors = make_file_list(INJURED_WARRIORS)
    injuries = make_file_list(INJURIES)
    forageable_items = make_file_list(FORAGEABLE_ITEMS)
    selected_warrior = random.choice(warriors)
    warrior_image = 'images/' + selected_warrior + '.jpg'
    selected_injury = random.choice(injuries)
    selected_injury_index = injuries.index(selected_injury)
    print(colored(selected_warrior, 'blue') + " has come to you with a " + colored(selected_injury, 'red') + "! What do you do?")
    if inventory[selected_injury_index] == 0:
        print(colored("You don't have enough medicine", 'red'), "to heal " + selected_warrior +
                                                                ". You must forage for medicine first!")
    else:
        print(colored("You use the " + forageable_items[selected_injury_index] + " to heal " + selected_warrior +
                      "!", 'yellow'))
        image = plt.imread(warrior_image)
        show_image(image, selected_warrior)
        inventory[selected_injury_index] -= 1
        healed_cats += 1
    return healed_cats


# returns error if input is not an int, redirects to input message
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       print("Please select a number from the available list!")
       continue
    else:
       return userInput
       break


# image input and display using matplotlib
def show_image(filename, image_title):
    plt.figure(num=image_title)  # set canvas title
    plt.tick_params(
        axis='both',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        left=False,  # ticks along the left edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False,  # labels along the bottom edge are off
        labelleft=False)  # labels along the left edge are off
    plt.imshow(filename)
    plt.pause(3)  # length of time in sec to display image
    plt.close()  # close image


# opens txt file and creates list
def make_file_list(FILE_NAME):
    file_list = []
    file = open(FILE_NAME)
    # always print a data source when you open it for the first time
    for line in file:
        file_list.append(line.strip())
    return file_list


if __name__ == '__main__':
    main()

