from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import copy
from board import draw_board
from pieces import order_white, movement, pieces
from checker import checking
import time

class Window(Frame):

    def __init__(self, state = [], color = 0):
        self.color = color
        self.checmate_msg_up = 0
        self.state = state
        self.rect_h = 0
        self.leng = 0
        self.selected = []
        self.is_selected = 0
        self.possible_moves = []
        self.possible_castling = []
        self.last_move = []
        self.long_castling_white = 1
        self.short_castling_white = 1
        self.long_castling_black = 1
        self.short_castling_black = 1
        self.prom = IntVar()
        super().__init__()
        self.init_window()

    def change_player(self):
        copy_state = copy.deepcopy(self.state)
        changed_copy = [[[0,0] for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                changed_copy[i][j] = copy_state[7-i][7-j]
                changed_copy[i][j][0] = 0

        self.last_move = [[7-lm[0], 7-lm[1]] for lm in self.last_move]
        for lm in self.last_move:
            x,y = lm
            changed_copy[y][x][0] = 4

        self.state = changed_copy
        self.color = (self.color+1)%2

    def checkmate_window_popup(self, text):
        top = Toplevel()
        top.title("Checkmate")

        msg = Message(top, text=text, font = ("Courier", 44))
        msg.pack()

    def checkmate(self):
        possibs = []
        for y in range(8):
            for x in range(8):
                p_number = copy.deepcopy(self.state[y][x][1])
                if p_number!=0:
                    p_color = (self.state[y][x][1]//7)
                    if p_color == self.color:
                        c_copy = copy.deepcopy(self.state)
                        move = movement[p_number](c_copy,[x,y],self.color)
                        if move!=[]:
                            possibs.append(move)
        
        if possibs==[]:
            self.checmate_msg_up = 1
            if checking(self.state,self.color):
                msg = ''
                if self.color == 1:
                    msg = 'Checkmate! Wygrama bialych!'
                else:
                    msg= 'Chackmate! Wygrana czarnych!'
                self.checkmate_window_popup(msg)
            else:
                msg = 'PAT!'
                self.checkmate_window_popup(msg)

    def check_for_castlings(self):
        if self.color == 0:
            possible_long = 0
            if self.long_castling_white:
                possible_long = 1
                if self.state[7][1][1]!=0 or self.state[7][2][1]!=0 or self.state[7][3][1]!=0:
                    possible_long =  0

                c_state = copy.deepcopy(self.state)
                if checking(c_state,self.color):
                    possible_long = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][2][1] = c_state[7][4][1]
                c_state[7][4][1] = 0
                if checking(c_state,self.color):
                    possible_long = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][3][1] = c_state[7][4][1]
                c_state[7][4][1] = 0
                if checking(c_state,self.color):
                    possible_long = 0

            possible_short = 0
            if self.short_castling_white:
                possible_short = 1
                if self.state[7][5][1]!=0 or self.state[7][6][1]!=0:
                    possible_short =  0

                c_state = copy.deepcopy(self.state)
                if checking(c_state,self.color):
                    possible_short = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][5][1] = c_state[7][4][1]
                c_state[7][4][1] = 0
                if checking(c_state,self.color):
                    possible_short = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][6][1] = c_state[7][4][1]
                c_state[7][4][1] = 0
                if checking(c_state,self.color):
                    possible_short = 0

            return [possible_short,possible_long]
        else:
            possible_long = 0
            if self.long_castling_black:
                possible_long = 1
                if self.state[7][5][1]!=0 or self.state[7][6][1]!=0 or self.state[7][4][1]!=0:
                    possible_long =  0

                c_state = copy.deepcopy(self.state)
                if checking(c_state,self.color):
                    possible_long = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][5][1] = c_state[7][3][1]
                c_state[7][3][1] = 0
                if checking(c_state,self.color):
                    possible_long = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][4][1] = c_state[7][3][1]
                c_state[7][3][1] = 0
                if checking(c_state,self.color):
                    possible_long = 0

            possible_short = 0
            if self.short_castling_black:
                possible_short = 1
                if self.state[7][1][1]!=0 or self.state[7][2][1]!=0:
                    possible_short =  0

                c_state = copy.deepcopy(self.state)
                if checking(c_state,self.color):
                    possible_short = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][2][1] = c_state[7][3][1]
                c_state[7][3][1] = 0
                if checking(c_state,self.color):
                    possible_short = 0

                c_state = copy.deepcopy(self.state)
                c_state[7][1][1] = c_state[7][3][1]
                c_state[7][3][1] = 0
                if checking(c_state,self.color):
                    possible_short = 0

            return [possible_short,possible_long]

    def on_click_button(self,root, figure):
        if self.color == 0:
            self.prom.set(figure)
        else:
            self.prom.set(figure+6)
        root.destroy()

    def promotion(self):
        top = Toplevel()
        top.title("Promotion!")

        msg = Message(top, text="Twoj pionek awansuje. Jaka figura ma mo zastapic?(Domyslnie hetman)", font = ("Courier", 44))
        msg.pack()

        kon = Button(top, text="Kon", command=lambda:self.on_click_button(top,2), font = ("Courier", 44))
        kon.pack()
        goniec = Button(top, text="Goniec", command=lambda:self.on_click_button(top,3), font = ("Courier", 44))
        goniec.pack()
        wieza = Button(top, text="Wieza", command=lambda:self.on_click_button(top,4), font = ("Courier", 44))
        wieza.pack()
        hetman = Button(top, text="Hetman", command=lambda:self.on_click_button(top,5), font = ("Courier", 44))
        hetman.pack()

    def update_state(self, b_x, b_y):
        self.state[b_y][b_x][0] = 1
        self.possible_moves = movement[self.state[b_y][b_x][1]](self.state,[b_x,b_y],player_color = self.color)
        self.selected =[b_x,b_y]

        if self.state[b_y][b_x][1] == 6 or self.state[b_y][b_x][1] == 12:
            short_castling, long_castling = self.check_for_castlings()

            if self.color == 0:
                if short_castling:
                    self.state[7][6][0]=2
                    self.possible_castling.append([6,7])

                if long_castling:
                    self.state[7][2][0]=2
                    self.possible_castling.append([2,7])
            else:
                if short_castling:
                    self.state[7][1][0]=2
                    self.possible_castling.append([1,7])

                if long_castling:
                    self.state[7][5][0]=2
                    self.possible_castling.append([5,7])

    def reverse_selection(self):
        if self.selected != []:
            self.state[self.selected[1]][self.selected[0]][0] = 0
        self.selected = []

    def reverse_possible_moves(self):
        for p in self.possible_moves:
            if p in self.last_move:
                self.state[p[1]][p[0]][0] = 4
            else:
                self.state[p[1]][p[0]][0] = 0
        self.possible_moves = []

    def reverse_castling(self):
        for p in self.possible_castling:
            if p in self.last_move:
                self.state[p[1]][p[0]][0] = 4
            else:
                self.state[p[1]][p[0]][0] = 0
        self.possible_castling = []

    def reverse_last_move_marker(self):
        for p in self.last_move:
            self.state[p[1]][p[0]][0]=0
        self.last_move = []

    def update_image(self, event):
        new_board = draw_board(self.state, self.leng)
        new_board = ImageTk.PhotoImage(new_board)
        event.widget.configure(image = new_board)
        event.widget.image = new_board

    def mark(self, event):
        b_x = int(event.x/self.rect_h)
        b_y = int(event.y/self.rect_h)
        if self.state[b_y][b_x][1] != 0 :
            self.reverse_selection()
            self.update_state(b_x,b_y)
            self.update_image(event)
            self.is_selected = 1

    def move(self, event):
        b_x = int(event.x/self.rect_h)
        b_y = int(event.y/self.rect_h)

        if [b_x,b_y] in self.possible_moves:

            if self.state[self.selected[1]][self.selected[0]][1] == 6:
                self.long_castling_white = 0
                self.short_castling_white = 0

            if self.state[self.selected[1]][self.selected[0]][1] == 12:
                self.long_castling_black = 0
                self.short_castling_black = 0

            if self.selected == [0,7]:
                if self.color == 0:
                    self.long_castling_white = 0
                else:
                    self.short_castling_black = 0

            if self.selected == [7,7]:
                if self.color == 0:
                    self.short_castling_white = 0
                else:
                    self.long_castling_black = 0

            if (self.state[self.selected[1]][self.selected[0]][1] == 1 or self.state[self.selected[1]][self.selected[0]][1] == 7) and b_y == 0:
                self.close = 0
                self.promotion()
                self.wait_variable(self.prom)
                self.state[self.selected[1]][self.selected[0]][1] = self.prom.get()

            self.state[b_y][b_x][1] = self.state[self.selected[1]][self.selected[0]][1]
            self.state[self.selected[1]][self.selected[0]][1] = 0
            
            self.last_move = [[b_x,b_y], copy.deepcopy(self.selected)]

            self.change_player()

        if [b_x,b_y] in self.possible_castling:
            if self.color == 0:
                if [b_x,b_y] == [6,7]:
                    self.state[7][6][1]=6
                    self.state[7][4][1]=0
                    self.state[7][5][1]=4
                    self.state[7][7][1]=0

                if [b_x,b_y] == [2,7]:
                    self.state[7][2][1]=6
                    self.state[7][4][1]=0
                    self.state[7][3][1]=4
                    self.state[7][0][1]=0

                self.long_castling_white = 0
                self.short_castling_white = 0

                self.last_move = [[b_x,b_y], copy.deepcopy(self.selected)]

                self.change_player()
            elif self.color == 1:
                if [b_x,b_y] == [5,7]:
                    self.state[7][5][1]=12
                    self.state[7][3][1]=0
                    self.state[7][4][1]=10
                    self.state[7][7][1]=0

                if [b_x,b_y] == [1,7]:
                    self.state[7][1][1]=12
                    self.state[7][3][1]=0
                    self.state[7][2][1]=10
                    self.state[7][0][1]=0

                self.last_move = [[b_x,b_y], copy.deepcopy(self.selected)]
                
                self.long_castling_black = 0
                self.short_castling_black = 0
                self.change_player()

        self.reverse_selection()
        self.reverse_possible_moves()
        self.reverse_castling()
        self.is_selected = 0
        self.update_image(event)

    def initial_state(self):
        self.state = [[[0,0] for i in range(8)] for j in range(8)]
        if self.color == 0:
            for n in range(8):
                self.state[1][n][1] = 7
                self.state[6][n][1] = 1
                self.state[0][n][1] = order_white[str([0,n])]
                self.state[7][n][1] = order_white[str([7,n])]           

    def select(self,event):
        if self.is_selected == 0:
            self.mark(event)
        else:
            self.move(event)
        if self.checmate_msg_up == 0:
            self.checkmate()
    
    def init_window(self):
        self.master.title('Krogulec')
        self.pack(fill = BOTH, expand = 1)
        self.columnconfigure(0, weight = 6)
        #self.columnconfigure(1, weight = 1)
        self.rowconfigure(0,weight = 1)

        main_f = Frame(self, bg = "GREY")
        main_f.grid(column = 0, row = 0, sticky = (N,S,E,W))
        self.update()

        leng, wid = main_f.winfo_height(), main_f.winfo_width()
        self.leng = leng
        self.rect_h = leng/8

        if self.state == []:
            self.initial_state()

        board_img = draw_board(state = self.state, h=leng)
        board_handle = ImageTk.PhotoImage(board_img)
        b_board = Label(main_f, image = board_handle)
        b_board.image = board_handle
        b_board.bind("<Button-1>", self.select)
        b_board.place(x=(wid-leng)/2,y=0)
        
        #recordframe = Frame(self, bg="BLACK")
        #recordframe.grid(column = 1, row = 0, sticky = (N,S,E,W))
