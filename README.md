# Static Chessboard Displayable for Ren'Py

This project provides a static chess displayable for the Ren'Py Visual Novel SDK. Its sole purpose is to render a given chess FEN (Forsyth–Edwards Notation) into a chessboard and highlight any given squares. If, instead of a static display, you are looking for a fully-functional chess engine for Ren'Py, please refer to [my other GitHub repository](https://github.com/RuolinZheng08/renpy-chess).

This project doesn't import any third-party libraries, is self-contained within `game/00-static-chessboard`, and is platform-independent (PC, MacOS, Linux, iOS, Android, web, etc.)

## Demo
The default chessboard is `720x720` pixels and the demo game has resolution `1920x1080`. Read the guide for integration below.

The following code (in `game/script.rpy`) generates the above GIF demo.
```renpy
```

## Guide for Integrating into a Ren'Py Project

The project code and assets are contained within the `game/00-static-chessboard` directory. Therefor, you can directly copy the entire directory into your Ren'Py `game/` directory.
