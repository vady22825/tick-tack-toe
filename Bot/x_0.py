tabel=[
    ['-','-','-'],
    ['-','-','-'],
    ['-','-','-']
]

def print_doard(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()

def check_win(board, plaer):
    for row in board:
        if row.count(plaer) == 3:
            return True

    for i in range(3):
        if board[0][i] == plaer and board[1][i] == plaer and board[2][2]==plaer:
            return True

    if board[0][0] == plaer and board[1][1] == plaer and board[2][0]==plaer:
        return True
    if board[0][2] == plaer and board[1][1] == plaer and board[2][0]==plaer:
        return True

current_plaer = 'X'

while True:
    print_doard(tabel)
    print('Ход игкрока', current_plaer)
    row=int(input('Введите номер строки: ')) - 1
    col=int(input('Введите номер столбца: ')) - 1

    if tabel[row][col] != '-':
        print('Ячейка занета')
        continue

    tabel[row][col] = current_plaer

    if check_win(tabel, current_plaer):
        print(f'Игрок {current_plaer} Выйграл!!')
        break

    if all([cell != '_' for row in tabel for cell in row]):
        print('Продолжите')


    current_plaer = '0' if current_plaer == 'X' else "X"



















