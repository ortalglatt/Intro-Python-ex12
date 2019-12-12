from ex12.board import Board


class Game:
    ERROR_MOVE_MSG = "illegal move"

    def __init__(self):
        """
        Initialize a Game object.
        """
        self.__board = Board()
        self.__moves_counter = {1: 0, 2: 0}

    def make_move(self, column):
        """
        If the game isn't over and the given column isn't full, the function
        will put the disc of the current player in the column. Else, it will
        raise an exception.
        :param column: The column the player chose to put the disc in.
        :return: None
        """
        if column < 0 or column > 6:
            raise Exception(self.ERROR_MOVE_MSG)
        if self.get_winner() is not None:
            raise Exception(self.ERROR_MOVE_MSG)
        player = self.get_current_player()
        try:
            self.__board.add_disc(player, column)
            self.__moves_counter[player] += 1
        except (ValueError, IndexError):
            raise Exception(self.ERROR_MOVE_MSG)

    def get_winner(self):
        """
        If there is a winner - the function will return his number, if there is
        a draw - it will return 0, and if the game isn't over - it will return
        None.
        :return: The winner number, 0 or None
        """
        return self.__board.check_win()

    def get_player_at(self, row, col):
        """
        If the coordinates are not legal, the function will raise an exception.
        :param row: The row coordinate
        :param col: The column coordinate
        :return: The player in the given coordinates or None (if thw cell is
        empty).
        """
        try:
            return self.__board.player_in_coor(row, col)
        except IndexError:
            raise IndexError(self.ERROR_MOVE_MSG)

    def get_current_player(self):
        """
        :return: The number of the current player in the game
        """
        player1_counter = self.__moves_counter[1]
        player2_counter = self.__moves_counter[2]
        if player1_counter == player2_counter:
            return 1
        return 2

    def get_win_coordinates(self):
        """
        :return: The coordinates of the circles that gave the win
        """
        return self.__board.get_win_coor()
