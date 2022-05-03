import random


random.seed()


def current_result(card, player_score, casino):
    if not casino:
        print(f'У игрока {card}, всего {player_score} очков.')
    else:
        print(f'У казино {card}, всего {player_score} очков')


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
        self.player_score = 0
        self.casino_score = 0

    def random_card(self, player_score, casino):
        current = self.deck.pop()
        if type(current) is int:
            player_score += current
        elif current == 'A':
            if player_score <= 10:
                player_score += 11
            else:
                player_score += 1
        else:
            player_score += 10
        current_result(current, player_score, casino)
        return player_score

    def choice(self):
        player_score = self.random_card(self.player_score, False)
        casino_score = self.random_card(self.casino_score, True)

        while True:
            answer = input('Взять карту? y/n: ')
            answer.lower()

            if answer == 'y':
                player_score = self.random_card(player_score, False)
                if casino_score < 19 and player_score <= 21:
                    casino_score = self.random_card(casino_score, True)
                if player_score > 21 or casino_score == 21:
                    print('Выиграло казино!')
                    break
                elif player_score == 21 and casino_score == 21:
                    print('ничья')
                elif player_score == 21 or casino_score > 21:
                    print('Выиграл игрок!')
                    break

            elif answer == 'n':
                if player_score > casino_score and casino_score < 19:
                    while casino_score < 19:
                        casino_score = self.random_card(casino_score, True)
                if player_score < casino_score <= 21:
                    print(f'Игрок проиграл! У игрока {player_score} очков, у казино {casino_score} очков')
                else:
                    print(f'Игрок выиграл, у игрока {player_score} очков, у казино {casino_score} очков')

                break

    def start(self):
        random.shuffle(self.deck)
        print('BlackJack')
        self.choice()
        print('До новых встреч!')


game = BlackJack()
game.start()
