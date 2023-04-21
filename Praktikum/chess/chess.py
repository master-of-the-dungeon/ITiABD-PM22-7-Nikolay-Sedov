def get_check_coordinates(s):
    s = s.lower()
    s = s.replace(" ", "")


    if len(s) == 2 and s[0] in '12345678' and s[1] in 'abcdefgh':
        x, y = 8 - int(s[0]), s[1]
    elif len(s) == 2 and s[1] in '12345678' and s[0] in 'abcdefgh':
        x, y = 8 - int(s[1]), s[0]
    else:
        return False


    for i in range(8):
        if y == 'abcdefgh'[i]:
            y = i
            break
    return x, y
def error_diagnos_figure(x0, y0, color, figures, board_):
    if board_.board[x0][y0] == '·':
        print("Вы не выбрали фигуру! ", end='')
        return None
    if board_.board[x0][y0].isupper() != color:
        print("Вы не можете ходить фигурой соперника! ", end='')
        return None


    for i in figures:
        if i.x0 == x0 and i.y0 == y0:
            f = i

    for i in range(8):
        for j in range(8):
            if f.is_available(i, j, board_) == True:
                return x0, y0

    print("Эта фигура не может никуда ходить! ", end='')
    return None
def error_diagnos(x0, y0, x, y, color, figures, board_):
    if board_.board[x][y] != '·' and board_.board[x][y].isupper() == color:
        print("Выбранная позиция уже занята вашей фигурой! ", end='')
        return None
    for i in figures:
        if i.x0 == x0 and i.y0 == y0:
            if i.is_available(x, y, board_) == False:
                print("Выбранная фигура так не ходит! ", end='')
                return None
    return x0, y0, x, y
class Knight():
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "N"
        else:
            self.icon = "n"
        board_.board[self.x0][self.y0] = self.icon
    def is_available(self, x, y, board_):
        if board_.board[x][y] != '·' and board_.board[x][y].isupper() == self.color:
            return False
        if (x - self.x0) ** 2 + (y - self.y0) ** 2 == 5:
            return True
        else:
            return False
class Rook():
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "R"
        else:
            self.icon = "r"
        board_.board[self.x0][self.y0] = self.icon
    def is_available(self, x, y, board_):
        if board_.board[x][y] != '·' and board_.board[x][y].isupper() == self.color:
            return False
        # по горизонтали
        if self.x0 == x:
            for i in range(min(self.y0, y) + 1, max(self.y0, y)):
                if board_.board[self.x0][i] != '·':
                    return False
            return True
        # по вертикали
        elif self.y0 == y:
            for i in range(min(self.x0, x) + 1, max(self.x0, x)):
                if board_.board[i][self.y0] != '·':
                    return False
            return True
        return False
class Bishop():
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "B"
        else:
            self.icon = "b"
        board_.board[self.x0][self.y0] = self.icon
    def is_available(self, x, y, board_):
        if board_.board[x][y] != '·' and board_.board[x][y].isupper() == self.color:
            return False
        if abs(self.x0 - x) == abs(self.y0 - y) and self.x0 - x != 0:
            step_y = int((y - self.y0) / abs(y - self.y0))
            step_x = int((x - self.x0) / abs(x - self.x0))
            j = self.x0 + step_x
            for i in range(self.y0 + step_y, y, step_y):
                if board_.board[j][i] != '·':
                    return False
                j += step_x
            return True
        return False
class Pawn():
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "P"
        else:
            self.icon = "p"
        board_.board[self.x0][self.y0] = self.icon

    def is_available(self, x, y, board_):
        if board_.board[x][y] != '·' and board_.board[x][y].isupper() == self.color:
            return False
        # просто ход
        if self.y0 == y:
            # первый ход(длинный)
            if (self.x0 == 6 and x == 4 and board_.board[5][self.y0] == board_.board[4][
                self.y0] == '·' and self.color == True) or \
                    (self.x0 == 1 and x == 3 and board_.board[2][self.y0] == board_.board[3][
                        self.y0] == '·' and self.color == False):
                return True

            elif board_.board[x][y] == '·' and \
                    ((self.color == True and self.x0 - x == 1) or \
                     (self.color == False and self.x0 - x == -1)):
                return True

        elif abs(y - self.y0) == 1 and board_.board[x][y] != '·' and \
                ((self.color == True and self.x0 - x == 1) or \
                 (self.color == False and self.x0 - x == -1)):
            return True
        return False
class Queen(Rook, Bishop):
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "Q"
        else:
            self.icon = "q"
        board_.board[self.x0][self.y0] = self.icon

    def is_available(self, x, y, board_):
        if Rook.is_available(self, x, y, board_) == True or Bishop.is_available(self, x, y, board_) == True:
            return True
        else:
            return False
class King():
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "K"
        else:
            self.icon = "k"
        board_.board[self.x0][self.y0] = self.icon

    def is_available(self, x, y, board_):
        if board_.board[x][y] != '·' and board_.board[x][y].isupper() == self.color:
            return False
        if abs(x - self.x0) <= 1 and abs(y - self.y0) <= 1:
            return True
        return False
class Camel():
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "C"
        else:
            self.icon = "c"
        board_.board[self.x0][self.y0] = self.icon

    def is_available(self, x, y, board_):
        if board_.board[x][y] != '·' and board_.board[x][y].isupper() == self.color:
            return False
        if (x - self.x0) ** 2 + (y - self.y0) ** 2 == 10:
            return True
        else:
            return False
class Centaur(Bishop, Knight):
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "H"
        else:
            self.icon = "h"
        board_.board[self.x0][self.y0] = self.icon

    def is_available(self, x, y, board_):
        if Knight.is_available(self, x, y, board_) == True or Bishop.is_available(self, x, y, board_) == True:
            return True
        else:
            return False
class Dragon(King, Bishop):
    def __init__(self, x, y, color, board_):
        self.x0 = x
        self.y0 = y
        self.color = color
        if color == True:
            self.icon = "D"
        else:
            self.icon = "d"
        board_.board[self.x0][self.y0] = self.icon

    def is_available(self, x, y, board_):
        if King.is_available(self, x, y, board_) == True or Bishop.is_available(self, x, y, board_) == True:
            return True
        else:
            return False
class Board():
    def __init__(self):
        self.board = []
        [self.board.append(["·"] * 8) for i in range(8)]

    def show(self):
        print('   A B C D E F G H')
        print(' ┌─────────────────┐')
        for i in range(8):
            print(str(8 - i) + '│', end=' ')
            [print(self.board[i][j], end=' ') for j in range(8)]
            print('│' + str(8 - i))
        print(' └─────────────────┘')
        print('   A B C D E F G H')
        print()
    def is_figure_under_fight(self, x_p, y_p, figures, color):

        for i in range(8):
            for j in range(8):

                for r in figures:
                    if r.x0 == i and r.y0 == j:

                        if r.is_available(x_p, y_p, self) == True and r.color != color:
                            return True
        return False
    def show_figures_under_fight(self, figures, color):
        print('Фигуры под боем: ')
        print('   A B C D E F G H')
        print(' ┌─────────────────┐')

        for i in range(8):
            print(str(8 - i) + '│', end=' ')

            # если выбранная фигура
            for j in range(8):
                if self.board[i][j] != "·" and self.board[i][j].isupper() == color and self.is_figure_under_fight(i, j,
                                                                                                                  figures,
                                                                                                                  color) == True:
                    print('#', end=' ')
                else:
                    print(self.board[i][j], end=' ')

            print('│' + str(8 - i))

        print(' └─────────────────┘')
        print('   A B C D E F G H')
    def fill(b):
        figures = {
            Rook(0, 0, False, b),
            Rook(0, 7, False, b),
            Rook(7, 0, True, b),
            Rook(7, 7, True, b),

            Knight(0, 1, False, b),
            Knight(0, 6, False, b),
            Knight(7, 1, True, b),
            Knight(7, 6, True, b),

            Bishop(0, 2, False, b),
            Bishop(0, 5, False, b),
            Bishop(7, 2, True, b),
            Bishop(7, 5, True, b),

            Queen(0, 3, False, b),
            Queen(7, 3, True, b),

            King(0, 4, False, b),
            King(7, 4, True, b),

            Pawn(1, 0, False, b),
            Pawn(1, 1, False, b),
            Pawn(1, 2, False, b),
            Pawn(1, 3, False, b),
            Pawn(1, 4, False, b),
            Pawn(1, 5, False, b),
            Pawn(1, 6, False, b),
            Pawn(1, 7, False, b),

            Pawn(6, 0, True, b),
            Pawn(6, 1, True, b),
            Pawn(6, 2, True, b),
            Pawn(6, 3, True, b),
            Pawn(6, 4, True, b),
            Pawn(6, 5, True, b),
            Pawn(6, 6, True, b),
            Pawn(6, 7, True, b)
        }
        return figures
def main_chess(b, figures):
    move_number = 1
    while True:
        color = move_number % 2
        if color == True:
            print(move_number, "Ход белых:")
        else:
            print(move_number, "Ход черных:")

        b.show()

        b.show_figures_under_fight(figures, color)
        # получаем координаты поля
        s1 = input("Введите координаты фигуры: ")
        if s1 == "стоп":
            print("Игра окончена.")
            break
        try:
            x0, y0 = get_check_coordinates(s1)
            x0, y0 = error_diagnos_figure(x0, y0, color, figures, b)

        except:
            print("Попробуйте снова!")
            print()
            continue

        s2 = input("Введите координаты позиции: ")
        if s2 == "стоп":
            print("Игра окончена.")
            break


        try:


            x, y = get_check_coordinates(s2)
            x0, y0, x, y = error_diagnos(x0, y0, x, y, color, figures, b)


        except:
            print("Попробуйте снова!")
            print()
            continue


        move_number += 1
        for i in figures:
            if i.x0 == x0 and i.y0 == y0:
                b.board[x][y] = b.board[x0][y0]
                b.board[x0][y0] = '·'
                i.x0 = x
                i.y0 = y
def main():
    b = Board()
    figures = Board.fill(b)
    main_chess(b, figures)

main()