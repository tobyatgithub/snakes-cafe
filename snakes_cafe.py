import sys

WIDTH = 96
ORDER = {}

def welcome():
    """
    This is the first called function in our main session that will
    simply print out the welcoming information.
    """

    ln_one = "Welcome to the Snakes Cafe! "
    ln_two = "Please see our menu below."
    ln_three = 'To quit at any time, type "quit"'
    print("*" * WIDTH)
    print("**" + ' ' * (WIDTH-4) + '**')
    print('**' + ' ' * ((WIDTH - 4 - len(ln_one))//2) + ln_one + \
    ' ' * ((WIDTH - 4 - len(ln_one))//2) + '**')
    print("**" + ' ' * (WIDTH-4) + '**')
    print('**' + ' ' * ((WIDTH - 4 - len(ln_two))//2) + ln_two + \
    ' ' * ((WIDTH - 4 - len(ln_two))//2) + '**')
    print("**" + ' ' * (WIDTH-4) + '**')
    print("**" + ' ' * (WIDTH-4) + '**')
    print('**' + ' ' * ((WIDTH - 4 - len(ln_three))//2) + ln_three + \
    ' ' * ((WIDTH - 4 - len(ln_three))//2) + '**')
    print("*" * WIDTH)



def menu():
    """
    Here's the function that just print out the menu contents.
    """
    print("\n\n")
    print("Appetizers")
    print("-" * 15)
    print("Snake Skins \nSnake Tails \nSnake Tongues \n\n")

    print("Entrees")
    print("-" * 15)
    print("Delicous Fired Snake \nHealthy Steamed Snake \nMysterious Snake Legs \n\n")

    print("Desserts")
    print("-" * 15)
    print("Skinny Biscuit \nSnake Cream Smoothie \nDetoxicated Essence\n\n")

    print("Beverages")
    print("-" * 15)
    print("Snake Coffee \nPurpole Herb Tea \nBlood of the Victims \n")

def order():
    """
    This function asks user to input what they want to order.
    Right now the function will accept any input...even the item
    is not on menu. Magic shop!
    """

    ln_order = "What would you like to order? "
    print("*" * WIDTH)
    print("**" + ' ' * (WIDTH-4) + '**')
    print('**' + ' ' * ((WIDTH - 4 - len(ln_order))//2) + ln_order + \
    ' ' * ((WIDTH - 4 - len(ln_order))//2) + '**')
    print("**" + ' ' * (WIDTH-4) + '**')
    print("*" * WIDTH)
    return(input())

def run():
    welcome()
    menu()

    # ordering process
    this_order = order()
    while this_order.lower() != "quit":
        if this_order in ORDER.keys():
            ORDER[this_order] += 1
        else:
            ORDER[this_order] = 1

        print('\n\n** %d order of %s have been added to your meal **\n\n' \
        %(ORDER[this_order], this_order))
        this_order = order()

    # completion of ordering
    ln_complete = "OK! That's it."
    print("*" * WIDTH)
    print("**" + ' ' * (WIDTH-4) + '**')
    print('**' + ' ' * ((WIDTH - 4 - len(ln_complete))//2) + ln_complete + \
    ' ' * ((WIDTH - 4 - len(ln_complete))//2) + '**')
    print("**" + ' ' * (WIDTH-4) + '**')
    print("*" * WIDTH)

    # show users what they have ordered so far. No modification allowed!
    print("Here's your orders: \n\n")
    for i,j in ORDER.items():
        print("%s : %d" %(i,j))
    print("\n\nYour Order is received and on its way!\n")


# def feedback(user_order, ORDER):

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("\n\nQuit!.. See you!\n\n")
        sys.exit()

