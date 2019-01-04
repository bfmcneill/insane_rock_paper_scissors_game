from player import Player, Computer

# TODO: Create tests, this program works I think! tests would be better!!
def main():
    print_header()
    player1 = Player(input("What is your player name? --> "))
    player2 = Computer("Computer")
    game_loop(player1, player2)


def print_header():
    print('*' * 20)
    print('RPS GAME')
    print('*' * 20)


def game_loop(player1, player2):
    rounds = 0
    while True:
        rounds += 1
        player1.battle(player2)
        if player1.score == 3 or player2.score == 3:
            break

    print(f"\nYou battled for {rounds} rounds")


if __name__ == '__main__':
    main()
