from random import randint


class tic_tac_toe():
    '''TicTacToe playing class, contains board information, and will play against human
       player, will actively try to lose the game, this challenge is difficult, and will
       require understanding object oriented programming in python.
    '''
    def __init__(self):
        '''Constructor, will establish board state, and will determine whether the player
           plays as X or O.
        '''
        if randint(0,1) == 0:
            print("Player is X")
            self.playerSymbol = "X"
            self.AISymbol = "O"
        else:
            print("Player is O")
            self.playerSymbol = "O"
            self.AISymbol = "X"
        self.board = [[" "," "," "],
                      [" "," "," "],
                      [" "," "," "]]
            
    def draw_board(self):
        '''Draws board state to standard output, used by other prompts.
        '''
        for line in self.board:
            print(line)
        return

    def player(self):
        '''Displays board state, and then asks player to make a move, delivers errors
           if player requests an impossible position, and updates board when valid position
           given.
        '''
        self.draw_board()
        move = input("What is your move? (format: x y, from 1,2,3)")
        moveX = int(move[0]) - 1
        moveY = int(move[-1]) - 1
        self.board[moveY][moveX] = self.playerSymbol
        return

    def score_position(self, x, y):
        '''Scores positions by attractiveness, used by AI to determine worst possible
           place to play.
        '''
        return

    def play_AI(self):
        '''Determines worst possible place for the AI to play and then plays it.
        '''
        moveX = randint(0, 2)
        moveY = randint(0, 2)
        while self.board[moveX][moveY] != " ":
            moveX = randint(0, 2)
            moveY = randint(0, 2)
            #break
        print(moveX,moveY)
        self.board[moveY][moveX] = self.AISymbol
        return

    def win_condition(self):
        '''Determines whether or not a player has won, prints winning message to standard
           output and returns boolean for main game engine.
        '''
        win_check = False
        winner = ""
        for i in range(0,2): #check rows
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                win_check = True
                winner = self.board[0][i]
        for i in range(0,2): #check columns
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                win_check = True
                winner = self.board[i][0]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ": #check diagonal
                win_check = True
                winner = self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ": #check diagonal
                win_check = True
                winner = self.board[1][1]
        return (win_check, winner)

    def play_game(self):
        '''Plays the game!, uses move updaters for player and AI until either a win condition
           or a draw condition is reached.
        '''
        while not self.win_condition()[0]:
            self.player()
            self.play_AI()
        self.draw_board()
        print(self.win_condition()[1],self.playerSymbol)
        if self.win_condition()[1] == self.playerSymbol:
            print("You are the WINNER!")
        else:
            print("LOSER")
        return
            
tic_tac_toe().play_game()

