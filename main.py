"""
Camel Race Simulator
Author: Mohamed Alkarbi
Description: A simple camel racing game using Python classes.
"""
import random
import time
import os

class Camel:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def move(self):
        step = random.randint(1, 5)

        # Boost
        if random.random() < 0.2:
            print(f"⚡ {self.name} got a speed boost!")
            step += 3

        # Stumble
        elif random.random() < 0.15:
            print(f"💥 {self.name} stumbled!")
            step = 0

        self.distance += step


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_name(num):
    while True:
        name = input(f"Enter camel {num} name: ")
        if name.strip() == "" or name.isnumeric():
            print("Invalid name. Try again.")
        else:
            return name


def show_race(camels):
    finish = 30
    for camel in camels:
        track = "-" * camel.distance
        remaining = " " * (finish - camel.distance)
        print(f"{camel.name:12} 🐫{track}|{remaining}🏁")


def show_ranking(camels):
    sorted_camels = sorted(camels, key=lambda c: c.distance, reverse=True)

    print("\n📊 Ranking:")
    for i, camel in enumerate(sorted_camels, 1):
        print(f"{i}. {camel.name} ({camel.distance})")


def get_bet(camels):
    print("\n💰 Choose a camel to bet on:")
    for i, camel in enumerate(camels, 1):
        print(f"{i}. {camel.name}")

    while True:
        choice = input("Enter number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(camels):
            return camels[int(choice)-1]
        else:
            print("Invalid choice.")


def race(camels, bet_camel):
    finish = 30

    messages = [
        "🔥 What a race!",
        "🐫 The camels are flying!",
        "💨 So fast!",
    ]

    print("\n🏁 The race begins!\n")
    time.sleep(1)

    while True:
        clear_screen()

        for camel in camels:
            camel.move()

            if camel.distance >= finish:
                show_race(camels)
                print(f"\n🏆 {camel.name} WINS THE RACE!")

                if camel == bet_camel:
                    print("💰 You WON your bet!")
                else:
                    print("❌ You lost the bet!")

                return

        show_race(camels)
        show_ranking(camels)

        print("\n" + random.choice(messages))
        time.sleep(0.6)


def main():
    print("🐫 Welcome to Camel Race Simulator!\n")

    camels = []

    for i in range(1, 4):
        name = get_name(i)
        camels.append(Camel(name))

    bet_camel = get_bet(camels)

    race(camels, bet_camel)

    again = input("\nPlay again? (y/n): ")
    if again.lower() == "y":
        main()
    else:
        print("Thanks for playing! 👋")


main()