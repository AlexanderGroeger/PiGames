import os
gameNames = list(os.listdir("games"))

import argparse
parser = argparse.ArgumentParser(description='Games built in PyGame')
parser.add_argument('game', type=str, help=f"name of existing games: {', '.join(gameNames)}")
args = parser.parse_args()

gameDir = f"games/{args.game.lower()}"

import lib.globals as G
G.init()
G.gameDir = gameDir

from importlib import import_module
gameMod = import_module(gameDir.split('.')[0].replace('/','.').replace('\\','.')+".main")
gameMod.start()
