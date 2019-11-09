import copy
import time
import random
from pieces import movement, pieces, pieces_value

def evaluate_state(state, color):
    value = 0
    for y in range(8):
        for x in range(8):
            p_number = state[y][x][1]
            if p_number!=0:
                p_color = (p_number//7)
                s_value = pieces_value[p_number]

                if p_color == color:
                    value-=s_value
                else:
                    value+=s_value

    return value

def all_the_moves(state, color):
    possibs = []
    for y in range(8):
        for x in range(8):
            if state[y][x][1]!=0:
                p_number = state[y][x][1]

                if (p_number//7) == color:
                    p_moves = movement[p_number](state,[x,y],color)
                    for p in p_moves:
                        possibs.append([[x,y], p])

    return possibs

def best_move(state, ai_color, depth, current_depth, primal_move = 0):
    player_color = (ai_color+1)%2
    
    #Get all the possible moves of ai in the current state
    ai_moves = all_the_moves(state, ai_color)

    #All the states which came out of the ai_moves. Pairs [state, move]
    states_after_ai = []

    for move in ai_moves:
        c_state = copy.deepcopy(state)
        #Apply_move
        from_m, to_m = move
        c_state[to_m[1]][to_m[0]][1] = c_state[from_m[1]][from_m[0]][1]
        c_state[from_m[1]][from_m[0]][1] = 0
        states_after_ai.append([c_state, move])

    states_after_enemy = []

    for enemy_state in states_after_ai:
        c_state, move = enemy_state
        player_moves = all_the_moves(c_state, player_color)
        current_move = []
        minimal_value = 10000000

        for move_e in player_moves:
            from_m, to_m = move_e
            e_state = copy.deepcopy(c_state)
            e_state[to_m[1]][to_m[0]][1] = e_state[from_m[1]][from_m[0]][1]
            e_state[from_m[1]][from_m[0]][1] = 0
            value = evaluate_state(e_state, ai_color)
            if minimal_value>value:
                minimal_value = value
            current_move.append([e_state, move, value])
        
        current_move = [c for c in current_move if c[2] == minimal_value]

        for c in current_move:
            states_after_enemy.append(c)

    if depth == current_depth:
        maximum_value = -100000
        for s in states_after_enemy:
            _, _, value = s
            if value>=maximum_value:
                maximum_value = value
        states_after_enemy = [s for s in states_after_enemy if s[2] == maximum_value]
        if primal_move!=0:
            print("Lowest point")
            return [primal_move, maximum_value]
        else:
            s = random.choice(states_after_enemy)
            _, primal_move, value = s
            print("Lowest point")
            return [primal_move, value]
    else:
        results = []
        if primal_move == 0:
            results = [best_move(s[0], ai_color, depth, current_depth+1, s[1]) for s in states_after_enemy]
        else:
            results = [best_move(s[0], ai_color, depth, current_depth+1, primal_move) for s in states_after_enemy]
        print(results)
        return results

def ai_turn(state, ai_color):
    #Copy the state, initialy you got a pointer
    c_state = copy.deepcopy(state)

    #To be returned
    last_move = []
    checkmate = 0
    #print("In on this")

    #Find the best move in current situation
    move = best_move(c_state, ai_color,1,0)
    move_max = max([m[1] for m in move])
    move = [m for m in move if m[1] == move_max]
    move = random.choice(move)

    if move == []:
        #None moves available, checkmate
        if ai_color == 0:
            checkmate = 1
        else:
            checkmate = 2
    else:
        #Apply best move
        #print(move)
        move, _ = move
        f, t = move
        state[t[1]][t[0]][1] = state[f[1]][f[0]][1]
        state[f[1]][f[0]][1] = 0
        last_move = [f,t]

    print("AI turn done!")

    return state, last_move, checkmate
