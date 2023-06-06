# PiGames
A repo for PyGame games ran on a Raspberry Pi

## Usage 
Inside the repo root folder, start a game using python
```
python run.py <name of game, NOT the path>
```

## Implementation Details
Basically this repo mimicks some of GameMaker's structure (well all games really), but I modularize each major component into a lib file including global variables that can be accessed by any instance. This is supposed to be heavy on the OOP, but the way drawing is handled may be inefficient. Need help regarding optimization. 
