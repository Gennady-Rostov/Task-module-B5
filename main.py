def greeting():
    print("Здравствуйте дорогие гости, предлагаю сыграть "
          "вам в консольное приложение 'крестики нолики'.")
    print("В данном приложении формат ввода осуществляется "
          "методом:x y, где x - номер строки, а y - номер столбца.")

def playing_field(f):
    num ='  0 1 2'
    print(num)
    for row, i in zip(f, num.split()):
        print (f"{i} {' '.join(str(j) for j in row)}")

def player_input(f, user):
    while True:
        place = input(f"Ходит игрок {user}. Введите координаты:").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x >= 0 and x < 3 and y >= 0 and  y < 3):
            print('Вышли из диапазона')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x,y


def win_position(f, user):
    f_list = []
    print(f)
    for l in f:
        f_list += l
    print(f_list)
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p))) == 3:
            return True
    return False


def start_play():
    count=0
    while True:
        playing_field(field)
        if count % 2 == 0:
            user = 'x'
        else:
            user = 'o'
        if count < 9:
            x, y = player_input(field, user)
            field[x][y] = user

        elif count == 9:
            print ('У вас ничья')
            break
        if win_position(field, user):
            print(f"Выиграл игрок {user}. Поздравляем!!!")
            break
        count += 1

greeting()

field = [["-"] * 3 for i in range(3) ]
count=0
while True:
    count += 1
    playing_field(field)
    if count % 2 == 0:
        user = '0'
    else:
        user = 'X'
    if count < 9:
        x, y = player_input(field, user)
        field[x][y] = user

    elif count == 9:
        print ('У вас ничья')
        break
    if win_position(field, user):
        print(f"Выиграл игрок {user}. Поздравляем!!!")
        break


stop_console = input()