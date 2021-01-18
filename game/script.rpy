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
    e "Let's play chess"
    show screen static_chessboard()
    e "Let me make a crazy move"
    show screen static_chessboard('rnbqkbnr/8/8/pppppppp/8/8/PPPPPPPP/RNBQKBNR')
    e "Done"
    e "Now let's highlight d5 and e6"
    show screen static_chessboard('rnbqkbnr/8/8/pppppppp/8/8/PPPPPPPP/RNBQKBNR', highlighted_squares=['d5', 'e6'])
    e ":D"

    # This ends the game.

    return
