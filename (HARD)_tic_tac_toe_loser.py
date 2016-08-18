class tic_tac_toe():
    '''TicTacToe playing class, contains board information, and will play against human
       player, will actively try to lose the game, this challenge is difficult, and will
       require understanding object oriented programming in python.
    '''
    def __init__(self):
        '''Constructor, will establish board state, and will determine whether the player
           plays as X or O.
        '''
        self.board = [[" "," "," "],
                      [" "," "," "],
                      [" "," "," "]]
            
    def draw_board(self):
        '''Draws board state to standard output, used by other prompts.
        '''
        return

    def player(self):
        '''Displays board state, and then asks player to make a move, delivers errors
           if player requests an impossible position, and updates board when valid position
           given.
        '''
        return

    def score_position(self, x, y):
        '''Scores positions by attractiveness, used by AI to determine worst possible
           place to play.
        '''
        return

    def play_AI(self):
        '''Determines worst possible place for the AI to play and then plays it.
        '''
        return

    def win_condition(self):
        '''Determines whether or not a player has won, prints winning message to standard
           output and returns boolean for main game engine.
        '''
        return

    def play_game(self):
        '''Plays the game!, uses move updaters for player and AI until either a win condition
           or a draw condition is reached.
        '''
        return
            
tic_tac_toe().play_game()
