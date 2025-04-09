class Game:
    """
    Handles the board state and its logic
    """
def turn_switcher():
    """
    Switches turns when one's turn is over
    :return:
    """
    pass

def game_won():
    """
    Notifies players who won when game is over
    :return:
    """
    pass

def board_state():
    """
    Controls the board setup and it's state when checkers have moved
    :return:
    """
    pass


class CheckerPiece:
    def __init__(self):
        """
        Initalize piece
        """
        pass

    def select_piece(self):
        """
        User clicks the piece, computer registers click
        :return:
        """
        pass

    def move_piece(self):
        """
        Moves the piece after empty grid is selected with checker "in hand"
        :return:
        """
        pass

    def make_piece_king(self):
        """
        Makes piece king when it reaches the opposite side of the board
        :return:
        """
        pass

class Sausage(CheckerPiece):
        def __init__(self):
            super().__init__()
            """
            Inherits all methods from CheckerPiece, is its own type of piece,
            starts on bottom
            """
            pass

class Pepperoni(CheckerPiece):
        def __init__(self):
            super().__init__()
            """
            Inherits all methods from CheckerPiece, is its own type of piece,,
            starts on top
            """
            pass
