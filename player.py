import random
from roll import Roll

DRAW=0
WIN=1
LOSE=-1

roll = Roll()
truth_table = roll.truth_table
attack_options = roll.rolls


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def attack(self):
        while True:
            print(f"{self.name}, select an attack:")
            roll.print_attack_options()
            attack = input("------->")
            try:
                attack_id = int(attack)
                attack = attack_options[attack_id]
                print(f"{self.name} chose to attack with {attack}")
                return attack
            except ValueError:
                raise
            except KeyError:
                raise
            except Exception:
                raise

    def battle(self, opponent):
        truth = truth_table.get(self.attack()).get(opponent.attack())

        if truth == 'WIN':
            self.score += 1
            msg = f"{self.score} to {opponent.score}"
            print(f"{self.name} won! {msg}")

        if truth == 'LOSE':
            opponent.score += 1
            msg = f"{self.score} to {opponent.score}"
            print(f"{opponent.name} won! {msg}")

        if truth == 'DRAW':
            msg = f"{self.score} to {opponent.score}"
            print(f"Draw! {msg}")


class Computer(Player):
    def attack(self):
        attack = attack_options[random.choice(range(1,16))]
        print(f"{self.name} chose to attack with {attack}")
        return attack
