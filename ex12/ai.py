import random


class AI:
    NO_MOVES_MSG = "no possible AI moves"
    WRONG_PLAYER_MSG = "wrong player"
    COL_NUM = 7

    def __init__(self, game, player):
        """
        Initialize an AI object.
        :param game: The game object of the app
        :param player: The number of the AI player (1, 2)
        """
        self.__game = game
        self.__player = player

    def find_legal_move(self, timeout=None):
        """
        If the game is not over, thw function will choose randomly one of the
        columns that are not full, so the AI player will put the disc in.
        :return: A legal col
        """
        if self.__game.get_winner() is not None:
            raise Exception(self.NO_MOVES_MSG)
        pos_moves = []
        for col in range(self.COL_NUM):
            if not self.__game.get_player_at(0, col):
                pos_moves.append(col)
        return random.choice(pos_moves)

    def get_last_found_move(self):
        pass


