from checker import check_available
import copy
from dicts import *

def change_state(state, moves):
    for move in moves:
        x,y = move
        if state[y][x][1] == 0:
            state[y][x][0] = 2
        else:
            state[y][x][0] = 3

def pawn_movement(state, position, player_color, tester = 0):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7

    posibble_moves = []
    if player_color!=color:
        return posibble_moves

    blocked = 0
    if position[1] == 6 and tester == 0:
        for i in range(1,3):
            x,y = position[0],position[1]-i
            if state[y][x][1] != 0:
                blocked = 1
            if blocked==0:
                posibble_moves.append([x,y])
    elif tester == 0:
        x,y = position[0],position[1]-1

        if state[y][x][1] == 0:
            posibble_moves.append([x,y])

    x,y = position[0]+1, position[1]-1

    if y<=7 and x>=0 and x<=7 and y>=0:
        if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color and state[y][x][1]!=6 and state[y][x][1]!=12:
            posibble_moves.append([x,y])

    x,y = position[0]-1, position[1]-1

    if y<=7 and x>=0 and x<=7 and y>=0:
        if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color and state[y][x][1]!=6 and state[y][x][1]!=12:
            posibble_moves.append([x,y])
    
    if tester == 1:
        return posibble_moves
    else:
        c_state = copy.deepcopy(state)
        posibble_moves = check_available(c_state, posibble_moves, position, color)
        change_state(state, posibble_moves)
        return posibble_moves

def queen_movement(state, position, player_color, tester = 0):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7

    posibble_moves = []
    if player_color!=color:
        return posibble_moves
    
    blocked = 0
    x,y = position[0],position[1]+1
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y+=1

    x,y = position[0],position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y-=1 

    x,y = position[0]+1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x+=1

    x,y = position[0]-1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1

    blocked = 0
    x,y = position[0]+1,position[1]+1
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y+=1
        x+=1

    x,y = position[0]-1,position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y-=1 
        x-=1

    x,y = position[0]+1,position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x+=1
        y-=1

    x,y = position[0]-1,position[1]+1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1
        y+=1  
    
    if tester == 1:
        return posibble_moves
    else:
        c_state = copy.deepcopy(state)
        posibble_moves = check_available(c_state, posibble_moves, position, color)
        change_state(state, posibble_moves)
        return posibble_moves

def rook_movement(state, position, player_color, tester = 0):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7
    posibble_moves = []
    if player_color!=color:
        return posibble_moves
    
    blocked = 0
    x,y = position[0],position[1]+1
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y+=1

    x,y = position[0],position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y-=1 

    x,y = position[0]+1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x+=1

    x,y = position[0]-1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1  
    
    if tester == 1:
        return posibble_moves
    else:
        c_state = copy.deepcopy(state)
        posibble_moves = check_available(c_state, posibble_moves, position, color)
        change_state(state, posibble_moves)
        return posibble_moves

def king_movement(state, position, player_color, tester = 0):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7
    posibble_moves = []
    if player_color!=color:
        return posibble_moves

    for i in range(-1,2):
        x,y = position[0]+i,position[1]-1
        if y>=0 and x>=0 and x<=7:
            if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
            elif state[y][x][1] == 0:
                posibble_moves.append([x,y])

    for i in range(-1,2):
        x,y = position[0]+i,position[1]+1
        if y<=7 and x>=0 and x<=7:
            if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
            elif state[y][x][1] == 0:
                posibble_moves.append([x,y])

    x,y = position[0]-1, position[1]

    if y<=7 and x>=0 and x<=7 and y>=0:
        if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color and state[y][x][1]!=6 and state[y][x][1]!=12:
            posibble_moves.append([x,y])
        elif state[y][x][1] == 0:
            posibble_moves.append([x,y])

    x,y = position[0]+1, position[1]

    if y<=7 and x>=0 and x<=7 and y>=0:
        if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color and state[y][x][1]!=6 and state[y][x][1]!=12:
            posibble_moves.append([x,y])
        elif state[y][x][1] == 0:
            posibble_moves.append([x,y])

    if tester == 1:
        return posibble_moves
    else:
        c_state = copy.deepcopy(state)
        posibble_moves = check_available(c_state, posibble_moves, position, color)
        change_state(state, posibble_moves)
        return posibble_moves

def knight_movement(state, position, player_color, tester = 0):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7
    posibble_moves = []
    if player_color!=color:
        return posibble_moves
    x,y = position

    combinations = [[x-2,y+1],[x-2,y-1],[x+2,y+1],[x+2,y-1],[x-1,y+2],[x-1,y-2],[x+1,y+2],[x+1,y-2]]

    for c in combinations:
        x,y = c
        if y<=7 and x>=0 and x<=7 and y>=0:
            if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
            elif state[y][x][1] == 0:
                posibble_moves.append([x,y])

    if tester == 1:
        return posibble_moves
    else:
        c_state = copy.deepcopy(state)
        posibble_moves = check_available(c_state, posibble_moves, position, color)
        change_state(state, posibble_moves)
        return posibble_moves

def bishop_movement(state, position, player_color, tester = 0):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7
    posibble_moves = []
    if player_color!=color:
        return posibble_moves
    
    blocked = 0
    x,y = position[0]+1,position[1]+1
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y+=1
        x+=1

    x,y = position[0]-1,position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y-=1 
        x-=1

    x,y = position[0]+1,position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x+=1
        y-=1

    x,y = position[0]-1,position[1]+1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7) and state[y][x][1]!=6 and state[y][x][1]!=12:
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1
        y+=1
    
    if tester == 1:
        return posibble_moves
    else:
        c_state = copy.deepcopy(state)
        posibble_moves = check_available(c_state, posibble_moves, position, color)
        change_state(state, posibble_moves)
        return posibble_moves

movement = {
    1:pawn_movement,
    2:knight_movement,
    4:rook_movement,
    5:queen_movement,
    3:bishop_movement,
    6:king_movement,
    7:pawn_movement,
    8:knight_movement,
    10:rook_movement,
    11:queen_movement,
    9:bishop_movement,
    12:king_movement    
}