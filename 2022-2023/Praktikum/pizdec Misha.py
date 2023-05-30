print('Начало игры')
print()


def korrert_vvod(m):
    m = m.lower()
    if len(m) == 2 and m[1] in '12345678' and m[0] in 'abcdefgh':
        x = 8 - int(m[1])
        y = m[0]
    else:
        return False
    for i in range(8):
        if y == 'abcdefgh'[i]:
            y = i
            break
    return x, y


def proverka_koord(x0, y0, number_igroka, fig, doska):
    if doska.board[x0][y0] == '·':
        print('На этом месте нет фигуры ')
        print()
    if doska.board[x0][y0].isupper() != number_igroka:
        print('Сейчас ход соперника ')
        print()
    for i in fig:
        if i.x0 == x0 and i.y0 == y0:
            f = i
    for i in range(8):
        for j in range(8):
            if f.hod_figur(i, j, doska) == True:
                return x0, y0

    print('Нельзя ходить этой фигурой ')
    print()


def proverka_koord2(x0, y0, x, y, number_igroka, fig, doska):
    if doska.board[x][y] != '·' and doska.board[x][y].isupper() == number_igroka:
        print('Здесь уже стоит другая фигура ')
        print()
    for i in fig:
        if i.x0 == x0 and i.y0 == y0:
            if i.hod_figur(x, y, doska) == False:
                print('Так нельзя ходить ')
                print()
                return None
    return x0, y0, x, y


class p_peshka():
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "P"
        else:
            self.nazv_figur = "p"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if doska.board[x][y] != '·' and doska.board[x][y].isupper() == self.number_igroka:
            return False
        if self.y0 == y:
            if (self.x0 == 6 and x == 4 and doska.board[5][self.y0] == doska.board[4][
                self.y0] == '·' and self.number_igroka == True) or (
                    self.x0 == 1 and x == 3 and doska.board[2][self.y0] == doska.board[3][
                self.y0] == '·' and self.number_igroka == False):
                return True
            elif doska.board[x][y] == '·' and ((self.number_igroka == True and self.x0 - x == 1) or (
                    self.number_igroka == False and self.x0 - x == -1)):
                return True
        elif abs(y - self.y0) == 1 and doska.board[x][y] != '·' and (
                (self.number_igroka == True and self.x0 - x == 1) or (
                self.number_igroka == False and self.x0 - x == -1)):
            return True
        return False


class n_konya():
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "N"
        else:
            self.nazv_figur = "n"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if doska.board[x][y] != '·' and doska.board[x][y].isupper() == self.number_igroka:
            return False
        if (x - self.x0) ** 2 + (y - self.y0) ** 2 == 5:
            return True
        else:
            return False


class r_ladya():
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "R"
        else:
            self.nazv_figur = "r"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if doska.board[x][y] != '·' and doska.board[x][y].isupper() == self.number_igroka:
            return False
        if self.x0 == x:
            for i in range(min(self.y0, y) + 1, max(self.y0, y)):
                if doska.board[self.x0][i] != '·':
                    return False
            return True
        elif self.y0 == y:
            for i in range(min(self.x0, x) + 1, max(self.x0, x)):
                if doska.board[i][self.y0] != '·':
                    return False
            return True
        return False


class b_slon():
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:

            self.nazv_figur = "B"
        else:
            self.nazv_figur = "b"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if doska.board[x][y] != '·' and doska.board[x][y].isupper() == self.number_igroka:
            return False
        if abs(self.x0 - x) == abs(self.y0 - y) and self.x0 - x != 0:
            step_y = int((y - self.y0) / abs(y - self.y0))
            step_x = int((x - self.x0) / abs(x - self.x0))
            j = self.x0 + step_x
            for i in range(self.y0 + step_y, y, step_y):
                if doska.board[j][i] != '·':
                    return False
                j += step_x
            return True
        return False


class q_fers(r_ladya, b_slon):
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "Q"
        else:
            self.nazv_figur = "q"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if r_ladya.hod_figur(self, x, y, doska) == True or b_slon.hod_figur(self, x, y, doska) == True:
            return True
        else:
            return False


class k_korol():
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "K"
        else:
            self.nazv_figur = "k"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if doska.board[x][y] != '·' and doska.board[x][y].isupper() == self.number_igroka:
            return False
        if abs(x - self.x0) <= 1 and abs(y - self.y0) <= 1:
            return True
        return False


class w_figure1(b_slon, r_ladya):
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "W"
        else:
            self.nazv_figur = "w"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if n_konya.hod_figur(self, x, y, doska) == True or r_ladya.hod_figur(self, x, y, doska) == True:
            return True
        else:
            return False


class u_figure2(k_korol, b_slon):
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "U"
        else:
            self.nazv_figur = "u"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if k_korol.hod_figur(self, x, y, doska) == True or b_slon.hod_figur(self, x, y, doska) == True:
            return True
        else:
            return False


class i_figure3():
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "I"
        else:
            self.nazv_figur = "i"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if doska.board[x][y] != '·' and doska.board[x][y].isupper() == self.number_igroka:
            return False
        if (x - self.x0) ** 2 + (y - self.y0) ** 2 == 8:
            return True
        else:
            return False


class shashki():
    def __init__(self, x, y, number_igroka, doska):
        self.x0 = x
        self.y0 = y
        self.number_igroka = number_igroka
        if number_igroka == True:
            self.nazv_figur = "S"
        else:
            self.nazv_figur = "s"
        doska.board[self.x0][self.y0] = self.nazv_figur

    def hod_figur(self, x, y, doska):
        if doska.board[x][y] != '·' and doska.board[x][y].isupper() == self.number_igroka:
            return False
        if abs(x - self.x0) == 1 and abs(y - self.y0) == 1:
            return True
        else:
            return False


class desk():
    def __init__(self):
        self.board = []
        [self.board.append(["·"] * 8) for i in range(8)]

    def print_board(self):
        print(' | A B C D E F G H |')
        print('─────────────────────')
        for i in range(8):
            print(str(8 - i) + '│', end=' ')
            [print(self.board[i][j], end=' ') for j in range(8)]
            print('│' + str(8 - i))
        print('─────────────────────')
        print(' | A B C D E F G H |')
        print()

    def figur(doska):
        fig = {r_ladya(0, 0, False, doska), r_ladya(0, 7, False, doska), r_ladya(7, 0, True, doska),
               r_ladya(7, 7, True, doska),
               n_konya(0, 1, False, doska), n_konya(0, 6, False, doska), n_konya(7, 1, True, doska),
               n_konya(7, 6, True, doska),
               b_slon(0, 2, False, doska), b_slon(0, 5, False, doska), b_slon(7, 2, True, doska),
               b_slon(7, 5, True, doska),
               q_fers(0, 3, False, doska), q_fers(7, 3, True, doska), k_korol(0, 4, False, doska),
               k_korol(7, 4, True, doska),
               p_peshka(1, 0, False, doska), p_peshka(1, 1, False, doska), p_peshka(1, 2, False, doska),
               p_peshka(1, 3, False, doska), p_peshka(1, 4, False, doska), p_peshka(1, 5, False, doska),
               p_peshka(1, 6, False, doska), p_peshka(1, 7, False, doska),
               p_peshka(6, 0, True, doska), p_peshka(6, 1, True, doska), p_peshka(6, 2, True, doska),
               p_peshka(6, 3, True, doska), p_peshka(6, 4, True, doska), p_peshka(6, 5, True, doska),
               p_peshka(6, 6, True, doska), p_peshka(6, 7, True, doska)}
        return fig

    def figur_dop(doska):
        fig = {w_figure1(0, 0, False, doska), w_figure1(0, 7, False, doska), w_figure1(7, 0, True, doska),
               w_figure1(7, 7, True, doska),
               u_figure2(0, 1, False, doska), u_figure2(0, 6, False, doska), u_figure2(7, 1, True, doska),
               u_figure2(7, 6, True, doska),
               i_figure3(0, 2, False, doska), i_figure3(0, 5, False, doska), i_figure3(7, 2, True, doska),
               i_figure3(7, 5, True, doska),
               q_fers(0, 3, False, doska), q_fers(7, 3, True, doska), k_korol(0, 4, False, doska),
               k_korol(7, 4, True, doska),
               p_peshka(1, 0, False, doska), p_peshka(1, 1, False, doska), p_peshka(1, 2, False, doska),
               p_peshka(1, 3, False, doska), p_peshka(1, 4, False, doska), p_peshka(1, 5, False, doska),
               p_peshka(1, 6, False, doska), p_peshka(1, 7, False, doska),
               p_peshka(6, 0, True, doska), p_peshka(6, 1, True, doska), p_peshka(6, 2, True, doska),
               p_peshka(6, 3, True, doska), p_peshka(6, 4, True, doska), p_peshka(6, 5, True, doska),
               p_peshka(6, 6, True, doska), p_peshka(6, 7, True, doska)}
        return fig

    def figur_shashki(doska):
        fig = {shashki(7, 0, True, doska), shashki(7, 2, True, doska), shashki(7, 4, True, doska),
               shashki(7, 6, True, doska),
               shashki(6, 1, True, doska), shashki(6, 3, True, doska), shashki(6, 5, True, doska),
               shashki(5, 0, True, doska), shashki(5, 2, True, doska), shashki(5, 4, True, doska),
               shashki(5, 6, True, doska),
               shashki(2, 1, False, doska), shashki(2, 3, False, doska), shashki(2, 5, False, doska),
               shashki(1, 0, False, doska), shashki(1, 2, False, doska), shashki(1, 4, False, doska),
               shashki(1, 6, False, doska),
               shashki(0, 1, False, doska), shashki(0, 3, False, doska), shashki(0, 5, False, doska)}
        return fig


def osnov_function(doska, fig):
    count = 1
    while True:
        number_igroka = count % 2
        if number_igroka == True:
            print('Ход заглавных: ', count)
            print()
        else:
            print('Ход маленьких: ', count)
            print()
        doska.print_board()
        hod = input('Введите координаты фигуры: ')
        print()
        if hod == "стоп":
            break
        try:
            x0, y0 = korrert_vvod(hod[2:4])
            x0, y0 = proverka_koord(x0, y0, number_igroka, fig, doska)

        except:
            print('Неверный ход ')
            print()
            continue
        try:
            x, y = korrert_vvod(hod[5:7])
            x0, y0, x, y = proverka_koord2(x0, y0, x, y, number_igroka, fig, doska)
        except:
            print('Неверный ход ')
            print()
            continue
        count += 1
        for i in fig:
            if i.x0 == x0 and i.y0 == y0:
                doska.board[x][y] = doska.board[x0][y0]
                doska.board[x0][y0] = '·'
                i.x0 = x
                i.y0 = y


def func():
    h = input('В какие шахматы сыграем? Обычные (1) или с новыми фигурами (2) или в шашки (3)? ')
    if h == '1':
        doska = desk()
        fig = desk.figur(doska)
        osnov_function(doska, fig)
    elif h == '2':
        doska = desk()
        fig = desk.figur_dop(doska)
        osnov_function(doska, fig)
    elif h == '3':
        doska = desk()
        fig = desk.figur_shashki(doska)
        osnov_function(doska, fig)


func()

