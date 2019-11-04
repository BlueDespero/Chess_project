
    '''
    def evaluate_state(self,state):
        value = 0
        for y in range(8):
            for x in range(8):
                p_number = state[y][x][1]
                if p_number!=0:

                    s_value = pieces_value[p_number]

                    if (p_number//7) != (self.player_color+1)%2:
                        value-=s_value
                    else:
                        value+=s_value

        return value

    def parent_moves_state(self, state, color):
        possibs = []
        for y in range(8):
            for x in range(8):
                if state[y][x][1]!=0:
                    p_number = state[y][x][1]


                    if p_number//7 == color:
                        p_moves = movement[p_number](state,[x,y],color)

                        for move in p_moves:
                            new_state = copy.deepcopy(state)
                            new_state[move[1]][move[0]][1] = new_state[y][x][1]
                            new_state[y][x][1] = 0

                            possibs.append([[x,y],move, new_state])

        return possibs

    def childern_moves(self, parents):
        parent_value = []
        new_generation = []
        
        for parent in parents:
            f, t, state = parent
            new_color = (self.color + 1)%2
            parent_minimum = 1000000
            possible_children = []

            for y in range(8):
                for x in range(8):
                    p_number = state[y][x][1]
                    if p_number != 0:

                        if p_number//7 == new_color:
                            moves = movement[p_number](state,[x,y],new_color)

                            for move in moves:
                                new_state = copy.deepcopy(state)
                                new_state[move[1]][move[0]][1] = new_state[y][x][1]
                                new_state[y][x][1] = 0
                                value = self.evaluate_state(new_state)
                                parent_minimum = min(parent_minimum,value)
                                possible_children.append([new_state, value])

            possible_children = [[parent, p] for p in possible_children if p[1]==parent_minimum]
            new_generation+=possible_children
            parent_value.append([parent, parent_minimum])

        return parent_value, new_generation

    def grandchildren_moves(self, children):
        parent_value = []
        new_generation = []
        
        for child_p in children:
            parent, child = child_p
            #print(child)
            moves = self.parent_moves_state(child[0], (self.player_color+1)%2)
            p_pack = []
            p_pack_minimum = 10000000
            for move in moves:
                f, t, state = move
                new_moves = self.parent_moves_state(state, self.player_color)
                if new_moves == []:                    
                    p_pack_minimum = min(p_pack_minimum, 10000)
                    p_pack.append([state, 10000])

                for n_move in new_moves:
                    f, t, n_state = n_move
                    value = self.evaluate_state(n_state)
                    p_pack_minimum = min(p_pack_minimum, value)
                    p_pack.append([n_state,value])

            if moves == []:
                parent_value.append([parent, -10000])
                p_pack.append([parent, [child[0], -10000]])
                new_generation+=p_pack
            else:
                p_pack = [[parent,p] for p in p_pack if p[1] == p_pack_minimum]
                parent_value.append([parent,p_pack_minimum])
                new_generation+=p_pack

        return parent_value, new_generation

    def best_move(self, state, c_depth, depth, color):
        #initial_value = self.evaluate_state(state)

        parent_possibs = self.parent_moves_state(state, self.color)
        #print(parent_possibs)
        parent_value, children_possibs = self.childern_moves(parent_possibs)

        #print(parent_value)
        start = time.time()

        for _ in range(2):
            parent_value, children_possibs =  self.grandchildren_moves(children_possibs)
            print("LOOOOOOOOOOOOOOL")

        maximum = max([p[1] for p in parent_value])
        chosen = random.choice([p[0] for p in parent_value if p[1] == maximum])

        print("Time = %.4f" % (time.time() - start))

        if parent_possibs == []:
            return parent_possibs

        return chosen

    def ai_turn(self, event):
        self.grab_set()
        c_state = copy.deepcopy(self.state)
        move = self.best_move(c_state, 0,1,self.color)

        if move == []:
            msg = ''
            if self.color == 0:
                msg = "Checkmate! Wygrana bialych!"
            else:
                msg = "Checkmate! Wygrana czarnych!"
            self.checkmate_window_popup(msg)
        else:
            f, t, _ = move
            self.state[t[1]][t[0]][1] = self.state[f[1]][f[0]][1]
            self.state[f[1]][f[0]][1] = 0
            self.last_move = [f,t]

        self.change_player()
        self.update_image(event)
        print("AI turn done!")
        self.grab_release()

    def ai_first_turn(self, parent):
        self.grab_set()
        c_state = copy.deepcopy(self.state)
        move = self.best_move(c_state, 0,1,self.color)
        #print(move)
        f, t, _ = move
        self.state[t[1]][t[0]][1] = self.state[f[1]][f[0]][1]
        self.state[f[1]][f[0]][1] = 0
        self.last_move = [f,t]
        self.change_player()
        self.ai_update_image(parent)
        print("AI turn done!")
        self.grab_release()
    '''