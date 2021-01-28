# Static Chessboard Displayable for Ren'Py

This project provides a static chess displayable for the Ren'Py Visual Novel SDK. Its sole purpose is to render a given chess FEN (Forsyth–Edwards Notation) into a chessboard and highlight any given squares. If, instead of a static display, you are looking for a fully-functional chess engine for Ren'Py, please refer to [my other GitHub repository](https://github.com/RuolinZheng08/renpy-chess).

This project doesn't import any third-party libraries, is self-contained within `game/00-static-chessboard`, and is platform-independent (PC, MacOS, Linux, iOS, Android, web, etc.)

The very basic usage is `show screen static_chessboard(fen, highlighted_squares)`. As an example:

```renpy
show screen static_chessboard('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', highlighted_squares=['e2', 'e4'])
```

## Demo
The default chessboard is `720x720` pixels and the demo game has resolution `1920x1080`.

<img src="https://github.com/RuolinZheng08/renpy-static-chessboard/blob/master/demo.gif" alt="Demo" width=600>

The following code (in `game/script.rpy`) generates the above GIF demo.

```renpy
e "Let's play chess!"
show screen static_chessboard()
e "I will go first. I'll move my pawn forward."
show screen static_chessboard('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR')
e "Let me highlight my previous move for you to see."
show screen static_chessboard('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', highlighted_squares=['e2', 'e4'])
e "Now it's your turn."
e "I'll highlight two moves that you can make. Choose your move:"
show screen static_chessboard('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR', highlighted_squares=['c5', 'c6'])
menu:
    "Move pawn to c6":
        $ fen = 'rnbqkbnr/pp1ppppp/2p5/8/4P3/8/PPPP1PPP/RNBQKBNR'
    "Move pawn to c5":
        $ fen = 'rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR'
show screen static_chessboard(fen)
```

## Guide for Integrating into a Ren'Py Project

The project code and assets are contained within the `game/00-static-chessboard` directory. Therefore, you can directly copy `game/00-static-chessboard` into your Ren'Py `game/` directory.

### Structure of `00-static-chessboard`

```
00-static-chessboard/
    - chesspieces                       # chess piece images
    - chessboard.png                    # chessboard image
    - static_chess_displable.rpy        # Ren'Py screen and displayable definition
```

If you wish to change the size of the chess displayable, you will need to replace the images and redefine `CHESS_BOARD_LEN` in `static_chess_displable.rpy`.

```renpy
# file paths
# name of the current directory
define CURRENT_DIR = '00-static-chessboard'
define CHESSPIECE_DIR = 'chesspieces'
define CHESSBOARD_IMG = 'chessboard.png'

# width of the chessboard, height should be the same
# a multiple of 8 is ideal as there are 8 squares in each file or rank
define CHESS_BOARD_LEN = 720
```
