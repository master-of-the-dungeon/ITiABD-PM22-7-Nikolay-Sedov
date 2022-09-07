print('Крестики нолики, для того, чтобы поставить фигурку, введите цифру, соотвествующую координате')

pole = list(range(1, 10))


def Risuempole(pole):
    print("-" * 13)
    for i in range(3):
        print("|", pole[0 + i * 3], "|", pole[1 + i * 3], "|", pole[2 + i * 3], "|")
        print("-" * 13)


def vvod(player_token):
    valid = False
    while not valid:
        otvet = input("Товарищ, поставь значок пожалуйста " + player_token+" ")
        try:
            otvet = int(otvet)
        except:
            print("Неправильные данные, выберите цифру от 1 до 9")
            continue
        if otvet >= 1 and otvet <= 9:
            if (str(pole[otvet - 1]) not in "XO"):
                pole[otvet - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Неправильные данные, выберите цифру от 1 до 9")


def check_win(pole):
    win_true = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_true:
        if pole[each[0]] == pole[each[1]] == pole[each[2]]:
            return pole[each[0]]
    return False


def Baza(pole):
    counter = 0
    win = False
    while not win:
        Risuempole(pole)
        if counter % 2 == 0:
            vvod("X")
        else:
            vvod("O")
        counter += 1
        if counter > 4:
            tmp = check_win(pole)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    Risuempole(pole)


Baza(pole)

input("Нажмите Enter для выхода!")
