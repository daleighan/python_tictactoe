class Game:
    def __init__(self):
        self.player1 = input("Who is player 1?")
        self.player2 = input("Who is player 2?")
        self.won = False
        self.move_count = 0
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.print_board()
        while self.won == False:
            print(self.player1, "moves")
            row = int(input("row?"))
            column = int(input("column"))
            self.toggle_place("X", row, column)
            self.check_wins("X", self.player1)
            if self.won == True:
                self.print_board()
                break
            self.print_board()
            print(self.player2, "moves")
            row = int(input("row?"))
            column = int(input("column"))
            self.toggle_place("O", row, column)
            self.check_wins("O", self.player2)
            self.print_board()

    def print_board(self):
        print(self.board[0])
        print(self.board[1])
        print(self.board[2])

    def toggle_place(self, piece,  i, j):
        if i not in range(0, 3):
            print("please enter values between 0 and 2 for the row")
            i = int(input("row?"))
        if j not in range(0, 3):
            print("please enter values between 0 and 2 for the row")
            j = int(input("column?"))
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

new_game = Game()
