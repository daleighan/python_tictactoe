class Game:
    def __init__(self):
        
        print("Welcome to two player command line Tic Tac Toe.") 
        print("Moves are measured in rows and columns between 0 and 2.") 
        print("Made by Alex Leigh in 2017.")
        self.player1 = input("Who is player 1?")
        self.player2 = input("Who is player 2?")
        self.won = False
        self.move_count = 0
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.print_board()
        while self.won == False:
            print(self.player1, "moves.")
            row = int(input("What row?"))
            column = int(input("What column?"))
            self.move_count = self.move_count + 1
            self.toggle_place("X", row, column)
            self.check_wins("X", self.player1)
            if self.won == True:
                self.print_board()
                break
            self.print_board()
            print(self.player2, "moves.")
            row = int(input("What row?"))
            column = int(input("What column?"))
            self.move_count = self.move_count + 1
            self.toggle_place("O", row, column)
            self.check_wins("O", self.player2)
            self.print_board()

    def print_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    def toggle_place(self, piece,  i, j):
        valid_move = False
        while valid_move == False:
            if i not in range(0, 3):
                print("Please enter values between 0 and 2 for the row.")
                i = int(input("What row?"))
            elif j not in range(0, 3):
                print("Please enter values between 0 and 2 for the row.")
                j = int(input("What column?"))
            elif self.board[i][j] != ' ':
                print("Please enter a move that has not already been made.")
                i = int(input("What row?"))
                j = int(input("What column?"))
            else:
                valid_move = True
        self.board[i][j] = piece

    def check_wins(self, piece, player):
        if self.board[0][0] == piece and self.board[0][1] == piece and self.board[0][2] == piece:
            self.won = True        
        if self.board[1][0] == piece and self.board[1][1] == piece and self.board[1][2] == piece:
            self.won = True
        if self.board[2][0] == piece and self.board[2][1] == piece and self.board[2][2] == piece:
            self.won = True
        if self.board[0][0] == piece and self.board[1][0] == piece and self.board[2][0] == piece:
            self.won = True
        if self.board[0][1] == piece and self.board[1][1] == piece and self.board[2][1] == piece:
            self.won = True
        if self.board[0][2] == piece and self.board[1][2] == piece and self.board[2][2] == piece:
            self.won = True
        if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
            self.won = True
        if self.board[0][2] == piece and self.board[1][1] == piece and self.board[2][0] == piece:
            self.won = True
        if self.won == True:
            print(player, "wins")
        if self.move_count == 9 and self.won == False:
            print("Unfortunately, there is no winner!")
            quit()

if __name__ == "__main__":
    new_game  = Game() 
