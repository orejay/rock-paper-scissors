import random


def game():
    options = ['R', 'P', 'S']
    player_pick = (
        input('Input (R) for Rock, (P) for Paper and (S) for Scissors?')).upper()
    while player_pick not in options:
        print('Please enter a valid option')
        player_pick = (
            input('Input (R) for Rock, (P) for Paper and (S) for Scissors?')).upper()
    cpu_pick = random.choice(options)
    print(ui(player_pick, cpu_pick))
    if ((player_pick == options[0] and cpu_pick == options[2]) or
        (player_pick == options[1] and cpu_pick == options[0]) or
            (player_pick == options[2] and cpu_pick == options[1])):
        print('Player wins!')
    elif ((player_pick == options[0] and cpu_pick == options[1]) or
          (player_pick == options[1] and cpu_pick == options[2]) or
          (player_pick == options[2] and cpu_pick == options[0])):
        print('CPU wins!')
    else:
        print("That's a tie! \n Play again")
        game()


def ui(player_pick, cpu_pick):
    if (player_pick == 'R'):
        player_ui = 'Rock'
    elif (player_pick == 'P'):
        player_ui = 'Paper'
    else:
        player_ui = 'Scissors'

    if (cpu_pick == 'R'):
        cpu_ui = 'Rock'
    elif (cpu_pick == 'P'):
        cpu_ui = 'Paper'
    else:
        cpu_ui = 'Scissors'

    return 'Player (' + player_ui + ') : ''CPU (' + cpu_ui + ')'


game()
