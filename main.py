from Logic.logic import logic
from Logic.iterate import game_iteration

if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie"]
    game_logic = logic(players)

    game_iter = game_iteration()
    game_iter.iteration(game_logic, 100)  # Run the game for a maximum of 100 iterations