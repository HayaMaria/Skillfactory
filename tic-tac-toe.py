def checking(field):
    for i in range(len(field)):
        if field[i][0] != "-":
            if field[i][0] == field[i][1] and field[i][1] == field[i][2]:
                return False

    for i in range(len(field)):
        if field[0][i] != "-":
            if field[0][i] == field[1][i] and field[1][i] == field[2][i]:
                return False

    if field[0][0] != "-":
        if field[0][0] == field[1][1] and field[1][1] == field[2][2]:
            return False

    if field[0][2] != "-":
        if field[0][2] == field[1][1] and field[1][1] == field[2][0]:
            return False

    if "-" in field[0] or "-" in field[1] or "-" in field[2]:
        return True
    else:
        return False

    return True


def show(field):
    print(" ", 0, "", 1, "", 2)
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(field[i][j], end="  ")
        print("")

def new_move():
    move_1 = int(input("строка: "))
    move_2 = int(input("столбец: "))
    return move_1, move_2

def overwriting(field, player, move1, move2):
    field[move1][move2] = player
    return field


field = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

answer = True
player = "x"

show(field)
while answer:
    print("Ход ", player)
    move_1, move_2 = new_move()
    overwriting(field, player, move_1, move_2)
    answer = checking(field)
    show(field)
    if player == "x":
        player = "o"
    else:
        player = "x"