from Logic.logic import logic

if __name__ == "__main__":
    players = ["Alice", "Bob", "Charlie"]
    game_logic = logic(players)

    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())

    game_logic.answer_correct()
    print("\nAfter answering correctly:")
    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())

    game_logic.answer_incorrect()
    print("\nAfter answering incorrectly:")
    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())

    game_logic.bank()
    print("\nAfter banking:")
    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())

    game_logic.answer_correct()
    print("\nAfter answering correctly:")
    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())

    game_logic.answer_correct()
    print("\nAfter answering correctly:")
    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())

    game_logic.answer_correct()
    print("\nAfter answering correctly:")
    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())

    game_logic.bank()
    print("\nAfter banking:")
    print("Current player:", game_logic.get_current_player())
    print("Current chain value:", game_logic.get_current_chain_value())
    print("Bank value:", game_logic.get_bank_value())