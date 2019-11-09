
images_pieces = {
    'white_pawn':'pieces/white_pawn.png',
    'white_knight':'pieces/white_knight.png',
    'white_rook':'pieces/white_rook.png',
    'white_queen':'pieces/white_queen.png',
    'white_bishop':'pieces/white_bishop.png',
    'white_king':'pieces/white_king.png',
    'black_pawn':'pieces/black_pawn.png',
    'black_knight':'pieces/black_knight.png',
    'black_rook':'pieces/black_rook.png',
    'black_queen':'pieces/black_queen.png',
    'black_bishop':'pieces/black_bishop.png',
    'black_king':'pieces/black_king.png'    
}

pieces = {
    0:'empty',
    1:'white_pawn',
    2:'white_knight',
    4:'white_rook',
    5:'white_queen',
    3:'white_bishop',
    6:'white_king',
    7:'black_pawn',
    8:'black_knight',
    10:'black_rook',
    11:'black_queen',
    9:'black_bishop',
    12:'black_king'    
}

order_white = {
    '[7, 1]':2,
    '[7, 6]':2,
    '[7, 0]':4,
    '[7, 7]':4,
    '[7, 3]':5,
    '[7, 2]':3,
    '[7, 5]':3,
    '[7, 4]':6,
    '[0, 1]':8,
    '[0, 6]':8,
    '[0, 7]':10,
    '[0, 0]':10,
    '[0, 3]':11,
    '[0, 2]':9,
    '[0, 5]':9,
    '[0, 4]':12   
}

order_black = {
    '[0, 1]':2,
    '[0, 6]':2,
    '[0, 0]':4,
    '[0, 7]':4,
    '[0, 3]':5,
    '[0, 2]':3,
    '[0, 5]':3,
    '[0, 4]':6,
    '[7, 1]':8,
    '[7, 6]':8,
    '[7, 7]':10,
    '[7, 0]':10,
    '[7, 3]':11,
    '[7, 2]':9,
    '[7, 5]':9,
    '[7, 4]':12   
}

pieces_value = {
    1:10,
    2:30,
    4:50,
    5:90,
    3:32,
    6:900,
    7:10,
    8:30,
    10:50,
    11:90,
    9:32,
    12:900
}