from ex12.game import Game
from ex12.ai import AI
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image


class App:
    ROWS_SIZE = 6
    COLS_SIZE = 7
    PLAYERS = {1: "red4", 2: "blue4"}
    FONT = "Tex Gyre Schola Math"
    BG = "papaya whip"
    GOLD = "dark goldenrod"
    GAME_TITLE = "four in a row"
    QUIT_TITLE = "Game Over"
    GAME_M = "** FOUR IN A ROW **"
    CHOOSE_M = "CHOOSE PLAYERS:"
    GOODLUCK_M = "GOOD LUCK!"
    DRAW = "IT'S A TIE!"
    PLAY_AGAIN_M = "PLAY AGAIN"
    QUIT_M = "QUIT"
    PLAYER1_M = "PLAYER \n      1"
    PLAYER2_M = "PLAYER \n      2"
    MENU_M = "MAIN MENU"
    COMP_VS_COMP = "ex12/compVsComp.jpg"
    COMP_VS_MAN = "ex12/compVsMan.jpg"
    MAN_VS_MAN = "ex12/manVsMan.jpg"
    MAN_VS_COMP = "ex12/manVsComp.jpg"
    WOOD_BG = "ex12/woodBG.jpg"

    def __init__(self, master):
        """
        Initialize an App object.
        :param master: The main root of the game
        """
        self.__master = master
        self.__master.protocol("WM_DELETE_WINDOW", self.__press_x)
        self.__master.geometry("850x550")
        self.__master.title(self.GAME_TITLE)
        self.__game = Game()

        self.__enter_frame = tk.Frame(self.__master, height=550, width=850,
                                      bg=self.BG)
        self.__game_frame = tk.Frame(self.__master, height=550, width=850,
                                     bg=self.BG)
        self.__board_canvas = tk.Canvas(self.__game_frame, height=450, width=550,
                                        highlightthickness=2,
                                        highlightbackground="black")
        self.__player1_canvas = tk.Canvas(self.__game_frame, height=130,
                                          width=100,
                                          highlightbackground=self.GOLD,
                                          highlightthickness=4, bg=self.BG)
        self.__player2_canvas = tk.Canvas(self.__game_frame, height=130,
                                          width=100, bg=self.BG,
                                          highlightthickness=2,
                                          highlightbackground="black")

        self.__available_rows = {col: self.ROWS_SIZE - 1 for col in
                                 range(self.COLS_SIZE)}
        self.__ai_players = {1: None, 2: None}
        self.__circles_dict = {}
        self.__after_id = ""
        self.__entrance_frame()

    def __entrance_frame(self):
        """
        Adds all the labels and buttons to the entrance frame, in the window
        that opens at the beginning of the game.
        :return: None
        """
        self.__enter_frame.pack(expand=True, fill=tk.BOTH)
        welcome_label = tk.Label(self.__enter_frame, text=self.GAME_M,
                                 bg=self.BG, font=(self.FONT, 55, "bold"))
        welcome_label.place(relx=0.5, rely=0.02, anchor=tk.N)

        choose_label = tk.Label(self.__enter_frame, text=self.CHOOSE_M,
                                bg=self.BG, font=(self.FONT, 35))
        choose_label.place(relx=0.5, rely=0.18, anchor=tk.N)

        goodluck_label = tk.Label(self.__enter_frame, text=self.GOODLUCK_M,
                                  bg=self.BG, font=(self.FONT, 35))
        goodluck_label.place(relx=0.5, rely=0.88, anchor=tk.N)

        comp_vs_comp = Image.open(self.COMP_VS_COMP).resize((220, 140),
                                                            Image.ANTIALIAS)
        comp_vs_comp = ImageTk.PhotoImage(comp_vs_comp)
        cvsc_button = tk.Button(self.__enter_frame, image=comp_vs_comp,
                                bg="black",
                                command=self.__change_to_gamescreen
                                (True, True))
        cvsc_button.photo = comp_vs_comp
        cvsc_button.place(relx=0.18, rely=0.44, anchor=tk.W)

        comp_vs_man = Image.open(self.COMP_VS_MAN).resize((220, 140),
                                                          Image.ANTIALIAS)
        comp_vs_man = ImageTk.PhotoImage(comp_vs_man)
        cvsm_button = tk.Button(self.__enter_frame, image=comp_vs_man,
                                bg="black",
                                command=self.__change_to_gamescreen
                                (False, True))
        cvsm_button.photo = comp_vs_man
        cvsm_button.place(relx=0.18, rely=0.72, anchor=tk.W)

        man_vs_man = Image.open(self.MAN_VS_MAN).resize((220, 140),
                                                        Image.ANTIALIAS)
        man_vs_man = ImageTk.PhotoImage(man_vs_man)
        mvsm_button = tk.Button(self.__enter_frame, image=man_vs_man,
                                bg="black", command=
                                self.__change_to_gamescreen(False, False))
        mvsm_button.photo = man_vs_man
        mvsm_button.place(relx=0.82, rely=0.44, anchor=tk.E)

        man_vs_comp = Image.open(self.MAN_VS_COMP).resize((220, 140),
                                                          Image.ANTIALIAS)
        man_vs_comp = ImageTk.PhotoImage(man_vs_comp)
        mvsc_button = tk.Button(self.__enter_frame, image=man_vs_comp,
                                bg="black", command=
                                self.__change_to_gamescreen(True, False))
        mvsc_button.photo = man_vs_comp
        mvsc_button.place(relx=0.82, rely=0.72, anchor=tk.E)

    def __change_to_gamescreen(self, player1, player2):
        """
        This functions changes the screen from the entrance frame to the game
        frame, and create AI object for every player that supposed to be AI.
        :param player1: True if player 1 supposed to be AI, and False if not.
        :param player2: True if player 2 supposed to be AI, and False if not.
        :return: The function "gamescreen".
        """
        def gamescreen():
            self.__enter_frame.destroy()
            if player1:
                self.__ai_players[1] = AI(self.__game, 1)
            if player2:
                self.__ai_players[2] = AI(self.__game, 2)
            self.game_frame()
        return gamescreen

    def game_frame(self):
        """
        Adds the board canvas, the two players canvases and the "main menu"
        button to the game frame.
        :return: None
        """
        self.__game_frame.pack(expand=True, fill=tk.BOTH)
        game_label = tk.Label(self.__game_frame, text=self.GAME_M,
                              bg=self.BG, font=(self.FONT, 35, "bold"))
        game_label.place(relx=0.5, rely=0.01, anchor=tk.N)

        self.__player1_canvas.place(relx=0.97, rely=0.3, anchor=tk.E)
        self.__player2_canvas.place(relx=0.03, rely=0.3, anchor=tk.W)
        self.__player1_canvas.create_text((57, 30), text=self.PLAYER1_M,
                                          font=(self.FONT, 15, "bold"))
        self.__player1_canvas.create_oval(23, 60, 83, 120, fill=self.PLAYERS[1])
        self.__player2_canvas.create_text((57, 30), text=self.PLAYER2_M,
                                          font=(self.FONT, 15, "bold"))
        self.__player2_canvas.create_oval(23, 60, 83, 120, fill=self.PLAYERS[2])

        self.__board_canvas.place(relx=0.5, rely=0.15, anchor=tk.N)
        wood_bg = Image.open(self.WOOD_BG).resize((560, 460),
                                                  Image.ANTIALIAS)
        wood_bg = ImageTk.PhotoImage(wood_bg)
        self.__board_canvas.photo = wood_bg
        self.__board_canvas.create_image(0, 0, image=wood_bg, anchor=tk.NW)
        self.__make_circles(self.ROWS_SIZE, self.COLS_SIZE)
        restart_button = tk.Button(self.__game_frame, width=11, height=2,
                                   text=self.MENU_M, bg=self.BG,
                                   font=(self.FONT, 10),
                                   command=self.__play_again(self.__game_frame))

        restart_button.place(relx=0.02, rely=0.9, anchor=tk.SW)

        if self.__ai_players[1]:
            self.__put_disk_in_col(self.__ai_players[1].find_legal_move())
        self.__board_canvas.bind("<Motion>", self.__move_cursor)
        self.__board_canvas.bind("<Button-1>", self.__put_disc)

    def __make_circles(self, rows_size, cols_size):
        """
        Adds circles to the board canvas, and to the circles dictionary.
        :param rows_size: The cols' amount in the board.
        :param cols_size: The rows' amount in the board.
        :return: None
        """
        for row in range(rows_size):
            for col in range(cols_size):
                circle = self.__board_canvas.create_oval(35 + col * 70,
                                                         25 + row * 70,
                                                         95 + col * 70,
                                                         85 + row * 70,
                                                         fill=self.BG)
                self.__circles_dict[(row, col)] = circle

    def __play_again(self, trans_root):
        """
        This function cancels the after' if there is one at the time, destroys
        the trans root and the main root (to start the game from the
        beginning).
        :param trans_root: The transport root to destroy
        :return: The "play_again_h" function
        """
        def play_again_h():
            if self.__after_id:
                self.__master.after_cancel(self.__after_id)
            trans_root.destroy()
            self.__master.destroy()
        return play_again_h

    def __move_cursor(self, event):
        """
        Checks if the cursor is on one of the columns. If it is, the function
        will fill the first available circle with the color of the current
        player.
        :param event: The event of the cursor moving on the board canvas
        :return: None
        """
        if not self.__ai_players[self.__game.get_current_player()] \
                and not self.__game.get_winner():
            x_coor, y_coor = event.x, event.y
            # check if it's not in the margins or between the columns.
            if y_coor in range(25, 435) or x_coor % 70 in range(26, 35):
                col = (x_coor - 35) // 70
            else:
                col = -1
            cur_color = self.PLAYERS[self.__game.get_current_player()]
            if col in range(self.COLS_SIZE) and col not in [-1, 7]:
                row = self.__available_rows[col]
                if row >= 0:
                    circ = self.__circles_dict[(row, col)]
                    self.__board_canvas.itemconfig(circ, fill=cur_color)

            # fill all the other circles with the background color.
            for c, av_row in self.__available_rows.items():
                if c != col and av_row >= 0:
                    self.__board_canvas.itemconfig(
                        self.__circles_dict[(av_row, c)],
                        fill=self.BG)

    def __put_disc(self, event):
        """
        If the current player is not an AI player, the function will put the
        disc in the column that was pressed.
        :param event: The event of clicking on the mouse
        :return: None
        """
        if not self.__ai_players[self.__game.get_current_player()]:
            x_coor = event.x
            col = (x_coor - 35) // 70
            if col in range(self.COLS_SIZE) or x_coor % 70 not in \
                    range(26, 35):
                self.__put_disk_in_col(col)

    def __put_disk_in_col(self, col):
        """
        If it's legal to put a disc in the given column, the function will fill
        the first available circle in the given color with the color of the
        current player. If no one won in this turn and the next player is an AI
        player, the function will call itself after 700 ms.
        :param col: The col that the player want to put the disc in
        :return: None
        """
        cur_player = self.__game.get_current_player()
        cur_color = self.PLAYERS[cur_player]
        row = self.ROWS_SIZE - 1
        try:
            while self.__game.get_player_at(row, col):
                row -= 1
            self.__game.make_move(col)
        except:
            return
        self.__board_canvas.itemconfig(self.__circles_dict[(row, col)],
                                       fill=cur_color)
        self.__available_rows[col] -= 1
        self.__check_win()

        cur_player = self.__game.get_current_player()
        self.__current_player(cur_player)
        if self.__ai_players[cur_player]:
            af_id = self.__master.after(700, self.__ai_turn(cur_player))
            self.__after_id = af_id

    def __ai_turn(self, player):
        """
        If there are legal moves (no one won and the board isn't full), the
        function will col the "put_disc_in_col" function with the col the AI
        gave.
        :param player: The current player
        :return: The "ai_helper" function
        """
        def ai_helper():
            try:
                self.__put_disk_in_col(self.__ai_players[player].
                                       find_legal_move())
            except:
                pass
        return ai_helper

    def __current_player(self, player):
        """
        This function markers the canvas of the current player.
        :param player: The current player
        :return: None
        """
        if player == 1:
            self.__player1_canvas.config(highlightbackground=self.GOLD,
                                         highlightthickness=4)
            self.__player2_canvas.config(highlightbackground="black",
                                         highlightthickness=2)
        else:
            self.__player2_canvas.config(highlightbackground=self.GOLD,
                                         highlightthickness=4)
            self.__player1_canvas.config(highlightbackground="black",
                                         highlightthickness=2)

    def __check_win(self):
        """
        Checks if the game is over and if one of the players won, or the board
        is empty. If there is a winner, the function will marker the circles
        that gave the win. After that, it will open the transport window.
        :return: None
        """
        winner = self.__game.get_winner()
        if winner in [0, 1, 2]:
            if winner in self.PLAYERS:
                win_coor = self.__game.get_win_coordinates()
                for coor in win_coor:
                    self.__board_canvas.itemconfig(self.__circles_dict[coor],
                                                   width=3,
                                                   outline=self.GOLD)
            self.__trans_window()

    def __trans_window(self):
        """
        Create a new window, that say why the game is over, and asks the player
        if he want to play again or to quit.
        :return: None
        """
        trans_window = tk.Tk()
        trans_window.protocol("WM_DELETE_WINDOW", trans_window)
        trans_window.geometry("300x150")
        trans_window.title(self.QUIT_TITLE)
        winner = self.__game.get_winner()
        if winner in self.PLAYERS:
            txt = "PLAYER " + str(winner) + " HAS WON!"
            color = self.PLAYERS[winner]
        else:
            txt = self.DRAW
            color = "black"
        trans_frame = tk.Frame(trans_window, width=300, height=200, bg=color)
        trans_frame.pack(expand=True, fill=tk.BOTH)
        trans_label = tk.Label(trans_frame, text=txt, bg=color,
                               font=(self.FONT, 15, "bold"), fg=self.BG)
        trans_label.place(relx=0.5, rely=0.01, anchor=tk.N)
        play_again_button = tk.Button(trans_frame, width=11, height=2,
                                      text=self.PLAY_AGAIN_M,
                                      bg=self.BG, font=(self.FONT, 10),
                                      command=self.__play_again(trans_window))

        quit_button = tk.Button(trans_frame, width=11, height=2,
                                text=self.QUIT_M,
                                bg=self.BG, font=(self.FONT, 10), command=quit)
        play_again_button.place(relx=0.45, rely=0.8, anchor=tk.SE)
        quit_button.place(relx=0.55, rely=0.8, anchor=tk.SW)

    def __press_x(self):
        """
        Create a new window that asks the player if he is sure he want to exit
        the game.
        :return: None
        """
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            exit()
