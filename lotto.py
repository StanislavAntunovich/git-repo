"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

import random


class Card:

    def __init__(self, name=None, is_computer=False):
        self.name = name
        self.computer_check = is_computer
        self._nums = random.sample(range(1, 91), 15)
        self._card = sorted(self._nums[:5]) + sorted(self._nums[5:10]) + sorted(self._nums[10:])
        self.card_pattern = self._make_card()

    def _sample_string(self):
        example = ['{}', '{}', '{}', '{}', '{}'] + list(' ' * 4)
        random.shuffle(example)
        return ' '.join(example) + '\n'

    def _make_card(self):
        self.s1 = '----------------------\n'
        if self.computer_check:
            self.s0 = 'карточка компьютера:\n'
        else:
            self.s0 = 'карточка игрока {}:\n'.format(self.name)
        return self.s0 + self.s1 + self._sample_string() + self._sample_string() + self._sample_string() + self.s1

    def __str__(self):
        return self.card_pattern.format(*self._card)


class Game:

    def _computer_turn(self):
        if self.barrel in self.player._card:
            for n, i in enumerate(self.player._card):
                if i == self.barrel:
                    self.player._card[n] = '-'
            return True
        else:
            return True

    def _player_turn(self):
        self.choice = input('зачеркнуть? [y/n]: ')
        if self.choice == 'y' and (self.barrel in self.player._card):
            for n, i in enumerate(self.player._card):
                if i == self.barrel:
                    self.player._card[n] = '-'
            return True
        elif self.choice == 'n' and (self.barrel not in self.player._card):
            return True
        else:
            print('{}, вы проиграли'.format(self.player.name))
            return False

    def _player_choice(self, player):
        self.player = player
        if self.player.computer_check:
            return self._computer_turn()
        else:
            return self._player_turn()

    def play(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.barrels = [i for i in range(1, 91)]

        while self.player1._card.count('-') != 15 and self.player2._card.count('-') != 15:
            self.barrel = random.choice(self.barrels)
            print('бочонок номер {}, осталось {}\n'.format(self.barrel, len(self.barrels) - 1))
            print(self.player1)
            print(self.player2)
            if self._player_choice(self.player1):
                pass
            else:
                break
            if self._player_choice(self.player2):
                pass
            else:
                break
            self.barrels.remove(self.barrel)

        if self.player1._card.count('-') == 15 and self.player2._card.count('-') == 15:
            print('ничья')
        elif self.player1._card.count('-') == 15:
            print('подбедил {}'.format(self.player1.name))
        elif self.player2._card.count('-') == 15:
            print('подбедил {}'.format(self.player2.name))
        else:
            pass


player1 = Card('Жорик', is_computer=False)
player2 = Card(is_computer=True)

game = Game()
game.play(player1, player2)
