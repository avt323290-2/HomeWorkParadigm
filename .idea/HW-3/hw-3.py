"""
Крестики-нолики
● Контекст
Вероятнее всего, вы с детства знакомы с этой игрой. Пришло
время реализовать её. Два игрока по очереди ставят крестики
и нолики на игровое поле. Игра завершается когда кто-то
победил, либо наступила ничья, либо игроки отказались
играть.
● Задача
Написать игру в “Крестики-нолики”. Можете использовать
любые парадигмы, которые посчитаете наиболее
подходящими. Можете реализовать доску как угодно - как
одномерный массив или двумерный массив (массив массивов).
Можете использовать как правила, так и хардкод, на своё
усмотрение. Главное, чтобы в игру можно было поиграть через
терминал с вашего компьютера.
"""

# Для решения задачи воспользуемся процедурным стилем программирования на Python.
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves = 0

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}")
        row, col = map(int, input("Введите номер строки и столбца (например, '1 2'): ").split())

        if board[row - 1][col - 1] == " ":
            board[row - 1][col - 1] = current_player
            moves += 1

            if check_winner(board, current_player):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif moves == 9:
                print_board(board)
                print("Ничья!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Эта клетка уже занята. Попробуйте снова.")

if __name__ == "__main__":
    play_game()
