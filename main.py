from ui.chess_gui import Chess
from engine.engine import create_engine

ENGINE_PATH = r"C:\Users\sansi\Downloads\stockfish\stockfish-windows-x86-64-avx2.exe"

stockfish = create_engine(ENGINE_PATH)

run = Chess(stockfish)
run.run()