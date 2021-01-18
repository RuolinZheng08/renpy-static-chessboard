# use loc to mean UI square and distinguish from logical square
define LOC_LEN = 90 # length of one side of a loc

# both file and rank index from 0 to 7
define INDEX_MIN = 0
define INDEX_MAX = 7

define COLOR_HIGHLIGHT = '#afeeeeaa' # PaleTurquoise

# use tuples for immutability
define PIECE_TYPES = ('p', 'r', 'b', 'n', 'k', 'q')

# file paths
define IMAGE_DIR = 'images'
define CHESSPIECE_DIR = 'chesspieces/'
define CHESSBOARD_IMG = 'chessboard.png'

define STARTING_BOARD_FEN= 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

screen static_chessboard(fen=STARTING_BOARD_FEN, highlighted_squares=[]):
    add StaticChessDisplayable(fen=fen, highlighted_squares=highlighted_squares)

init python:

    import re
    import os
    from itertools import chain
    
    def file_rank_to_coord(file_idx, rank_idx):
        assert INDEX_MIN <= file_idx <= INDEX_MAX and INDEX_MIN <= file_idx <= INDEX_MAX
        x = LOC_LEN * file_idx
        y = LOC_LEN * (INDEX_MAX - rank_idx)
        return (x, y)

    def square_to_file_rank_indices(square):
        """
        has promotion if len(square) == 3
        """
        assert len(square) == 2 or len(square) == 3
        square = square[:2] # ignore promotion
        file_idx = ord(square[0]) - ord('a')
        rank_idx = int(square[1]) - 1
        return file_idx, rank_idx

    class StaticChessDisplayable(renpy.Displayable):
        """
        Takes a board FEN and renders it as a Displayable object
        """
        def __init__(self, fen=STARTING_BOARD_FEN, highlighted_squares=[]):
            """
            fen: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
            """
            super(StaticChessDisplayable, self).__init__()

            # load piece images
            # white pieces represented as P, N, K, etc. and black p, n, k, etc.
            self.piece_imgs = {}
            for piece in PIECE_TYPES:
                white_piece, black_piece = piece.upper(), piece
                white_path = os.path.join(IMAGE_DIR, CHESSPIECE_DIR, 'w' + white_piece + '.png')
                black_path = os.path.join(IMAGE_DIR, CHESSPIECE_DIR, 'b' + black_piece + '.png')
                self.piece_imgs[white_piece] = Image(white_path)
                self.piece_imgs[black_piece] = Image(black_path)

            # parse and save fen
            fen_parser = FenParser(fen)
            self.piece_array = fen_parser.parse()

            self.highlighted_squares = [square_to_file_rank_indices(square) for square in highlighted_squares]
            # displayable
            self.highlight_img = Solid(COLOR_HIGHLIGHT, xsize=LOC_LEN, ysize=LOC_LEN)

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            # render chessboard image
            chessboard_path = os.path.join(IMAGE_DIR, CHESSBOARD_IMG)
            chessboard_img = Image(chessboard_path)
            render.place(chessboard_img)
            # render highlighted squares
            for file_idx, rank_idx in self.highlighted_squares:
                square_coord = file_rank_to_coord(file_idx, rank_idx)
                render.place(self.highlight_img, x=square_coord[0], y=square_coord[1])
            # render pieces on board
            for rank_idx, rank in enumerate(self.piece_array): # row
                print(rank_idx, rank)
                for file_idx, piece in enumerate(rank):
                    if piece == ' ':
                        continue
                    piece_img = self.piece_imgs[piece]
                    piece_coord = file_rank_to_coord(file_idx, rank_idx)
                    render.place(piece_img, x=piece_coord[0], y=piece_coord[1])
            return render

    # adapted from https://github.com/tlehman/fenparser
    class FenParser():
        def __init__(self, fen_str):
            self.fen_str = fen_str

        def parse(self):
            ranks = self.fen_str.split(' ')[0].split('/')
            pieces_on_all_ranks = [self.parse_rank(rank) for rank in ranks[::-1]] # reverse ranks
            return pieces_on_all_ranks

        def parse_rank(self, rank):
            rank_re = re.compile(r'(\d|[kqbnrpKQBNRP])')
            piece_tokens = rank_re.findall(rank)
            pieces = self.flatten(map(self.expand_or_noop, piece_tokens))
            return pieces

        def flatten(self, lst):
            return list(chain(*lst))

        def expand_or_noop(self, piece_str):
            """
            represent an empty square with a space
            """
            piece_re = re.compile(r'([kqbnrpKQBNRP])')
            retval = None
            if piece_re.match(piece_str):
              retval = piece_str
            else:
              retval = self.expand(piece_str)
            return retval

        def expand(self, num_str):
            return int(num_str) * ' '
