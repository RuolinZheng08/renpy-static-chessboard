# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at right
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
    e "That's a nice move! Now let's resume the game."

    # This ends the game.

    return
