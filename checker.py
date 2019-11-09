from dicts import pieces
import copy

def pawn_movement(state, position, player_color):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7
    posibble_moves = []
    if player_color!=color:
        return posibble_moves

    x,y = position[0]+1, position[1]+1

    if y<=7 and x>=0 and x<=7 and y>=0:
        posibble_moves.append([x,y])

    x,y = position[0]-1, position[1]+1

    if y<=7 and x>=0 and x<=7 and y>=0:
        posibble_moves.append([x,y])
    return posibble_moves

def queen_movement(state, position, player_color):
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
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y+=1

    x,y = position[0],position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y-=1 

    x,y = position[0]+1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x+=1

    x,y = position[0]-1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1

    blocked = 0
    x,y = position[0]+1,position[1]+1
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7):
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
            if player_color != (state[y][x][1]//7):
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
            if player_color != (state[y][x][1]//7):
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
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1
        y+=1  
    
    return posibble_moves

def rook_movement(state, position, player_color):
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
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y+=1

    x,y = position[0],position[1]-1
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        y-=1 

    x,y = position[0]+1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x+=1

    x,y = position[0]-1,position[1]
    blocked = 0
    while blocked == 0 and y<=7 and y>=0 and x<=7 and x>=0:
        if state[y][x][1]!=0:
            blocked = 1
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1  
    
    return posibble_moves

def king_movement(state, position, player_color):
    piece_number = state[position[1]][position[0]][1]
    color = piece_number//7
    posibble_moves = []
    if player_color!=color:
        return posibble_moves

    for i in range(-1,2):
        x,y = position[0]+i,position[1]-1
        if y>=0 and x>=0 and x<=7:
            if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color:
                posibble_moves.append([x,y])
            elif state[y][x][1] == 0:
                posibble_moves.append([x,y])

    for i in range(-1,2):
        x,y = position[0]+i,position[1]+1
        if y<=7 and x>=0 and x<=7:
            if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color:
                posibble_moves.append([x,y])
            elif state[y][x][1] == 0:
                posibble_moves.append([x,y])

    x,y = position[0]-1, position[1]

    if y<=7 and x>=0 and x<=7 and y>=0:
        if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color:
            posibble_moves.append([x,y])
        elif state[y][x][1] == 0:
            posibble_moves.append([x,y])

    x,y = position[0]+1, position[1]

    if y<=7 and x>=0 and x<=7 and y>=0:
        if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color:
            posibble_moves.append([x,y])
        elif state[y][x][1] == 0:
            posibble_moves.append([x,y])
    return posibble_moves

def knight_movement(state, position, player_color):
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
            if state[y][x][1]!= 0 and (state[y][x][1]//7)!=color:
                posibble_moves.append([x,y])
            elif state[y][x][1] == 0:
                posibble_moves.append([x,y])

    return posibble_moves

def bishop_movement(state, position, player_color):
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
            if player_color != (state[y][x][1]//7):
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
            if player_color != (state[y][x][1]//7):
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
            if player_color != (state[y][x][1]//7):
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
            if player_color != (state[y][x][1]//7):
                posibble_moves.append([x,y])
        else:
            posibble_moves.append([x,y])
        x-=1
        y+=1
    
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

def get_king_position(potential_state, color):
    target = 0

    if color == 1:
        target = 12
    else:
        target = 6

    for y in range(8):
        for x in range(8):
            if potential_state[y][x][1] == target:
                return [x,y] 

def checking(potential_state, color):
    king_x, king_y = get_king_position(potential_state, color)
    check = 0
    target = ''

    if color == 0:
        target = 7
    else:
        target = 1
    x,y = king_x+1,king_y-1
    if x<=7 and y<=7 and potential_state[y][x][1]==target:
        check = 1
    x,y = king_x-1,king_y-1
    if x>=0 and y<=7 and potential_state[y][x][1]==target:
        check = 1

    if color == 0:
        target = 8
    else:
        target = 2
    moves = knight_movement(potential_state,[king_x,king_y], color)
    for move in moves:
        x,y = move
        if potential_state[y][x][1] == target:
            check = 1

    if color == 0:
        target = 9
    else:
        target = 3
    moves = bishop_movement(potential_state,[king_x,king_y], color)
    for move in moves:
        x,y = move
        if potential_state[y][x][1] == target:
            check = 1

    if color == 0:
        target = 10
    else:
        target = 4
    moves = rook_movement(potential_state,[king_x,king_y], color)
    for move in moves:
        x,y = move
        if potential_state[y][x][1] == target:
            check = 1

    if color == 0:
        target = 11
    else:
        target = 5
    moves = queen_movement(potential_state,[king_x,king_y], color)
    for move in moves:
        x,y = move
        if potential_state[y][x][1] == target:
            check = 1

    if color == 0:
        target = 12
    else:
        target = 6
    moves = king_movement(potential_state,[king_x,king_y], color)
    for move in moves:
        x,y = move
        if potential_state[y][x][1] == target:
            check = 1

    return check

def check_available(c_state, p_moves, position, color):
    x,y = position
    out_moves = []

    for p in p_moves:
        new_state = copy.deepcopy(c_state)
        new_state[p[1]][p[0]][1] = new_state[y][x][1]
        new_state[y][x][1] = 0
        if checking(new_state, color) == 0:
            out_moves.append(p)

    return out_moves