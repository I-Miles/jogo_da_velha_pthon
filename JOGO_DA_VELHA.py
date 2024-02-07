import tkinter as tk
from tkinter import messagebox

board = [' ' for _ in range(9)]
counter =  0
score = {'X':  0, 'O':  0}

def checkline(char, spot1, spot2, spot3):
    return board[spot1] == board[spot2] == board[spot3] == char

def checkAll(char):
    return any([
        checkline(char,  0,  1,  2),
        checkline(char,  3,  4,  5),
        checkline(char,  6,  7,  8),
        checkline(char,  0,  3,  6),
        checkline(char,  1,  4,  7),
        checkline(char,  2,  5,  8),
        checkline(char,  0,  4,  8),
        checkline(char,  2,  4,  6)
    ])

def click(index, buttons, button, score_label):
    global counter
    player = 'X' if counter %  2 ==  0 else 'O'
    if board[index] == ' ':
        board[index] = player
        button['text'] = player
        if checkAll(player):
            messagebox.showinfo('You win', f"'{player}' wins the game!")
            score[player] +=  1
            score_label.config(text=f"Placar: X - {score['X']} : O - {score['O']}")
            reset(buttons, score_label)
        counter +=  1
        return True
    return False

def reset(buttons, score_label):
    global board, counter, score
    for button in buttons:
        button.config(state='disabled')
    board = [' ' for _ in range(9)]
    counter =  0
    score = {'X':  0, 'O':  0}
    for button in buttons:
        button.config(text=" ", state='normal')
    score_label.config(text=f"Placar: X - {score['X']} : O - {score['O']}")

def main():
    window = tk.Tk()
    score_label = tk.Label(window, text=f"Placar: X - {score['X']} : O - {score['O']}")
    score_label.grid(row=0, column=0, columnspan=3)
    buttons = [tk.Button(window, width=10, height=3, command=lambda index=index: click(index, buttons, buttons[index], score_label)) for index in range(9)]
    count =  0
    for r in range(1,  4):
        for c in range(3):
            buttons[count].grid(row=r, column=c)
            count +=  1
    reset_button = tk.Button(window, text="Reiniciar", command=lambda: reset(buttons, score_label))
    reset_button.grid(row=4, column=0, columnspan=3)

main()
