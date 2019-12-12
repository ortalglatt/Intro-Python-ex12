class Board:
    ROW_NUM = 6
    COL_NUM = 7
    EMPTY = "_"
    PLAYERS = {1: "1", 2: "2"}
    WIN_NUM = 4
    DRAW = 0

    def __init__(self):
        """
        constructor of a board
        """
        self.__board = [[[self.EMPTY, (row, col)] for row in
                         reversed(range(self.ROW_NUM))]
                        for col in range(self.COL_NUM)]
        self.win_coors = []

    def __str__(self):
        """
        just for following the progress. not in use.
        :return:
        """
        string_to_print = ""
        for row in reversed(range(self.ROW_NUM)):
            for col in range(self.COL_NUM):
                string_to_print += self.__board[col][row][0] + " "
            string_to_print += "\n"
        return string_to_print

    def add_disc(self, player_num, col):
        """
        the board adds a player's disc in a given col
        :param player_num: an integer representing a player.
        :param col: an integer representing a column
        :return: none
        """
        col_list = [sublist[0] for sublist in self.__board[col]]
        row = col_list.index(self.EMPTY)
        self.__board[col][row][0] = self.PLAYERS[player_num]

    def check_win(self):
        """
        This function checks if someone on the board wins
        :return:
        """
        for player, color in self.PLAYERS.items():
            # for every player, does all checks
            if self.__color_won(color, self.__board) or \
                    self.__color_won(color, self.__transpose()) \
                    or self.__color_won(color, self.__diagonals(self.__board)) \
                    or self.__color_won(color,
                                        self.__diagonals(self.__reverse())):
                return player
        for col in self.__board:
            # creating a list of all board to check if _ exists
            col_list = [sublist[0] for sublist in col]
            if self.EMPTY in col_list:
                return None
        return self.DRAW

    def __color_won(self, color, list_of_lists):
        """
        checks if the color won and keeping it's indexes
        :param color: a player's color to check on board
        :param list_of_lists: list of lists
        :return: false or true if the player won
        """
        for lst in list_of_lists:
            new_list = [sublist[0] for sublist in lst]
            str_to_check = ''.join(new_list)
            if color * self.WIN_NUM in str_to_check:
                # keeping the index and creating a range
                idx = str_to_check.find(color * self.WIN_NUM)
                if idx > 3:
                    rng = range(idx - self.WIN_NUM + 1, idx + 1)
                else:
                    rng = range(idx, idx + self.WIN_NUM)
                for i in rng:
                    # changing wins coordinates
                    self.win_coors.append(lst[i][1])
                return True
        return False

    def __transpose(self):
        """
        transposing a matrix
        :return:
        """
        transpose = []
        for row in range(self.ROW_NUM):
            new_row = []
            for col in range(self.COL_NUM):
                new_row.append(self.__board[col][row])
            transpose.append(new_row)
        return transpose[::-1]

    def __reverse(self):
        """
        reversing a matrix
        :return:
        """
        reverse_board = []
        for col in self.__board:
            new_col = col[::-1]
            reverse_board.append(new_col)
        return reverse_board

    def __diagonals(self, board_list):
        """
        creating strings from the diagonal of a matrix
        :param board_list: list of lists
        :return: list of strings
        """
        diagonals = []
        # creating strings of the upper triangle
        for i in range(len(board_list[0]) - self.WIN_NUM + 1):
            row = i
            col = 0
            new_lst = []
            while row < len(board_list[0]) and col < len(board_list):
                new_lst.append(board_list[col][row])
                col += 1
                row += 1
            diagonals.append(new_lst)

        # creating strings of the lower triangle
        for i in range(1, len(board_list) - self.WIN_NUM + 1):
            col = i
            row = 0
            new_lst = []
            while col < len(board_list) and row < len(board_list[0]):
                new_lst.append(board_list[col][row])
                col += 1
                row += 1
            diagonals.append(new_lst)
        return diagonals

    def player_in_coor(self, row, col):
        """
        checks who is located in the given location on board
        :param row: integer
        :param col: integer
        :return: None if empty, the player's number otherwise
        """
        player = self.__transpose()[row][col][0]
        if player == self.EMPTY:
            return None
        return int(player)

    def get_win_coor(self):
        """
        getter of the class
        :return: the winning coordinates
        """
        return self.win_coors

