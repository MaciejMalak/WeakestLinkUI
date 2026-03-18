from Logic.logic import Logic
from Logic.iterate import GameIteration

if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie"]
    game_logic = Logic(players)

    game_iter = GameIteration()
    game_iter.iteration(game_logic, 100)  # Run the game for a maximum of 100 iterations