from ex36_import import prompt

# make a tiny game
# use imports
# use lists
# use functions
def end(message):
    print(message, '\nGame over')
    exit(0)

def beginning():
    print("Welcome to the game!")
    user_name = prompt("What's your name?")
    print(f"Hello, {user_name}!")
    chair = prompt("There are two chairs... Which one do you sit yourself?")
    chair1_list = ['First', 'first', '1', 'left']
    chair2_list = ['Second', 'second', '2', 'right']
    if chair in chair1_list:
        end('You\'ve got beaten to death.')
    elif chair in chair2_list:
        end('You\'ve got enslaved and within one month you starved to death.')
    else:
        print('Exquisite! Well, why don\'t you follow along?')
        hall()

def hall():
    print('This is Equestria, the land of the free. \nYou are welcomed with milk and cookies.')
    print('We\'re going to part ways now. See you soon.')
    exit(0)

def main():
    beginning()

main()