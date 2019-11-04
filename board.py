from PIL import Image, ImageDraw
from dicts import images_pieces,pieces

colors = {
    'black':(0,0,0),
    'white':(255,255,255),
    'red':(255,0,0),
    'green':(0,255,0),
    'blue':(0,0,255),
    'orange':(255,140,0)
}

def draw_board(state, h = 560):

    canvas = Image.new('RGBA',(h,h))
    drawing = ImageDraw.Draw(canvas,'RGBA')
    rect_h = int(h/8)

    for i in range(8):
        y = rect_h*i
        for j in range(8):
            x = rect_h*j
            field = state[i][j]

            if field[0] == 0:
                if (i+j)%2 == 0:
                    drawing.rectangle([(x,y),(x+rect_h,y+rect_h)], fill=colors['white'])
                else:
                    drawing.rectangle([(x,y),(x+rect_h,y+rect_h)], fill=colors['black'])
            elif field[0] == 1:
                drawing.rectangle([(x,y),(x+rect_h,y+rect_h)], outline=colors['black'], fill=colors['blue'])
            elif field[0] == 2:
                drawing.rectangle([(x,y),(x+rect_h,y+rect_h)], outline=colors['black'], fill=colors['green'])
            elif field[0] == 3:
                drawing.rectangle([(x,y),(x+rect_h,y+rect_h)], outline=colors['black'], fill=colors['red'])
            elif field[0] == 4:
                drawing.rectangle([(x,y),(x+rect_h,y+rect_h)], outline=colors['black'], fill=colors['orange'])

            if field[1] != 0:
                piece = Image.open(images_pieces[pieces[field[1]]])
                piece = piece.resize((rect_h,rect_h))
                canvas.paste(piece,(x,y),piece)

    return canvas

if __name__ == "__main__":
    initial_state = [[[0,0] for i in range(8)] for j in range(8)]
    #print(initial_state)
    img = draw_board(initial_state)
    img.show()    