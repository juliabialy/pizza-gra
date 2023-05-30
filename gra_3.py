
import os
from colorama import Fore, Style

pizza_size = {
    '1': 'Mała',
    '2': 'Średnia',
    '3': 'Duża'
}

pizza_sauces = {
    '1': (Fore.RED, 'Pomidorowy'),
    '2': (Fore.LIGHTRED_EX, 'BBQ'),
    '3': (Fore.GREEN, 'Czosnkowy')
}

pizza_toppings = {
    '1': 'Pepperoni',
    '2': 'Grzyby',
    '3': 'Cebula',
    '4': 'Oliwki',
    '5': 'Papryka'
}

topping_emojis = {
    'Pepperoni': '🥓',
    'Grzyby': '🍄',
    'Cebula': '🧅',
    'Oliwki': '🫒',
    'Papryka': '🌶️'
}

sauce_colors = {
    '1': Fore.RED,
    '2': Fore.LIGHTRED_EX,
    '3': Fore.GREEN
}


def display_options(options):
    for key, value in options.items():
        print(f'{key}. {value}')


def create_pizza():
    print('Zrób swoją pizzę!')
    print(Fore.YELLOW + 'Wybierz rozmiar:' + Fore.RESET)
    display_options(pizza_size)
    size_choice = input(Fore.YELLOW + 'Podaj numer: ' + Fore.RESET)

    print(Fore.GREEN + 'Wybierz sos do pizzy:')
    display_options(sauce_colors)
    sauce_color_choice = input(Fore.GREEN + 'Podaj numer: ' + Fore.RESET)

    selected_sauce = pizza_sauces.get(sauce_color_choice)
    sauce_color = selected_sauce[0]
    sauce_name = selected_sauce[1]

    toppings = []
    while True:
        print(Fore.BLUE + 'Wybierz dodatki (Wpisz 0, aby zakończyć wybór):' + Fore.RESET)
        display_options(pizza_toppings)
        topping_choice = input(Fore.BLUE + 'Wpisz numer: ' + Fore.RESET)

        if topping_choice == '0':
            break

        toppings.append(pizza_toppings.get(topping_choice))

    pizza_base = '   _____\n'
    pizza_base += '  /     \\\n'
    pizza_base += ' /       \\\n'
    pizza_base += '|         |\n'
    pizza_base += '|' + sauce_color

    for topping in toppings:
        pizza_base += f' {topping_emojis.get(topping)}'
    pizza_base += ' ' * (9 - len(toppings) * 3)

    pizza_base += '|\n'
    pizza_base += ' \\       /\n'
    pizza_base += '  \\_____/'

    print(Fore.MAGENTA + '\nTwoja pizza jest gotowa!')
    print('Rozmiar: ' + pizza_size.get(size_choice))
    print('Sos: ' + sauce_color + sauce_name + Style.RESET_ALL)
    print('Dodatki:')
    for topping in toppings:
        print(topping_emojis.get(topping) + ' ' + topping)

    print(Fore.RESET + f'{sauce_color}{pizza_base}' + Style.RESET_ALL)


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def play_again():
    while True:
        print(Fore.YELLOW + 'Czy chcesz zagrać ponownie? TAK/NIE:' + Fore.RESET)
        choice = input().upper()

        if choice == 'TAK':
            clear()
            create_pizza()
        elif choice == 'NIE':
            break


def main():
    print(Fore.CYAN +
          "┌─────────────────────────────────────────────────────────────────────────────────┐")
    print("│                                                                                 │")
    print("│                              " + Fore.YELLOW + "_____ _              " + Fore.CYAN + "                              │")
    print("│                             " + Fore.YELLOW + "|  __ (_)             " + Fore.CYAN + "                              │")
    print("│                             " + Fore.YELLOW + "| |__) | __________ _  " + Fore.CYAN + "                             │")
    print("│                             " + Fore.YELLOW + "|  ___/ |_  /_  / _  | " + Fore.CYAN + "                             │")
    print("│                             " + Fore.YELLOW + "| |   | |/ / / / (_| | " + Fore.CYAN + "                             │")
    print("│                             " + Fore.YELLOW + "|_|   |_/___/___\__,_|" + Fore.CYAN + "                              │")
    print("│                          ────────────────────────────────                       │")
    print("│                                                                                 │")
    print("│   " + Fore.RED + "                         1. Wybierz rozmiar pizzy   " + Fore.CYAN + "                          │")
    print("│   " + Fore.RED + "                         2. Wybierz sos             " + Fore.CYAN + "                          │")
    print("│   " + Fore.RED + "                         3. Wybierz składniki      " + Fore.CYAN + "                           │")
    print("│                                                                                 │")
    print("│                                                                                 │")
    print("│                                 Zobacz ofertę :))                               │")
    print("│                                                                                 │")
    print("│         ┌──────── Pizza rozmiar ──────────┐ ┌──────────── Sosy ───────────┐     │")
    print("│         │ 1. " + Fore.MAGENTA + "Mała" + Fore.CYAN + "                         │ │  1. " + Fore.MAGENTA + "Pomidorowy" + Fore.CYAN + "              │     │")
    print("│         │ 2. " + Fore.CYAN + "Średnia" + Fore.CYAN + "                      │ │  2. BBQ                     │     │")
    print("│         │ 3. " + Fore.MAGENTA + "Duża" + Fore.CYAN + "                         │ │  3. " + Fore.MAGENTA + "Czosnkowy" + Fore.CYAN + "               │     │")
    print("│         └─────────────────────────────────┘ └─────────────────────────────┘     │")
    print("│       ┌─────────────────────────── Składniki ───────────────────────────────┐   │")
    print("│       │     1.Pepperoni             2.Grzyby             3.Cebula           │   │")
    print("│       │                 4.Oliwki              5.Papryka                     │   │")
    print("│       └─────────────────────────────────────────────────────────────────────┘   │")
    print(Fore.CYAN + "└─────────────────────────────────────────────────────────────────────────────────┘" + Style.RESET_ALL)
    create_pizza()
    play_again()
if __name__ == '__main__':
    main()


