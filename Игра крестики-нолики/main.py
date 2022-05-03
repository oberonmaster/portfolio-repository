class GameTable:
    value_X = 'X'
    value_O = 'O'
    value = ' '
    table_data = dict()

    def __init__(self, lines=3, columns=3):
        self.lines = lines
        self.columns = columns

        for current_line in range(self.lines):
            for current_column in range(self.columns):
                self.table_data[(current_line, current_column)] = self.value
        self.move = True

    def show_table(self):
        print('    0   1   2')
        print('0   {} | {} | {}  '.format(self.table_data[(0, 0)], self.table_data[(0, 1)], self.table_data[(0, 2)]))
        print('   -----------')
        print('1   {} | {} | {}  '.format(self.table_data[(1, 0)], self.table_data[(1, 1)], self.table_data[(1, 2)]))
        print('   -----------')
        print('2   {} | {} | {}  '.format(self.table_data[(2, 0)], self.table_data[(2, 1)], self.table_data[(2, 2)]))

    def is_win(self, player):
        # линии
        if self.table_data[(0, 0)] == self.table_data[(0, 1)] == self.table_data[(0, 2)] == player:
            return True
        elif self.table_data[(1, 0)] == self.table_data[(1, 1)] == self.table_data[(1, 2)] == player:
            return True
        elif self.table_data[(2, 0)] == self.table_data[(2, 1)] == self.table_data[(2, 2)] == player:
            return True
        # столбцы
        elif self.table_data[(0, 0)] == self.table_data[(1, 0)] == self.table_data[(2, 0)] == player:
            return True
        elif self.table_data[(0, 1)] == self.table_data[(1, 1)] == self.table_data[(2, 1)] == player:
            return True
        elif self.table_data[(0, 2)] == self.table_data[(1, 2)] == self.table_data[(2, 2)] == player:
            return True
        # диагонали
        elif self.table_data[(0, 0)] == self.table_data[(1, 1)] == self.table_data[(2, 2)] == player:
            return True
        elif self.table_data[(2, 0)] == self.table_data[(1, 1)] == self.table_data[(0, 2)] == player:
            return True
        else:
            return False

    def game(self):
        turn = 1
        while self.move:
            self.show_table()
            if self.is_win('X'):
                print('Поздравляем победителя - X!')
                self.move = False
                break
            if self.is_win('O'):
                print('Поздравляем победителя - O!')
                self.move = False
                break

            while True:
                col_position = int(input('Укажите столбец ячейки: '))
                line_position = int(input('Укажите строку ячейки: '))
                if self.table_data[(line_position, col_position)] != ' ':
                    print('Эта ячейка занята! Выберите другую!')
                else:
                    break

            if turn % 2 != 0:
                turn += 1
                self.table_data[(line_position, col_position)] = 'X'
                print('Игрок X сделал ход. Следующим ходит - O')
            else:
                turn += 1
                self.table_data[(line_position, col_position)] = 'O'
                print('Игрок O сделал ход. Следующим ходит - X')

        print('Игра окончена!')


table = GameTable()
table.game()
