from Logic.logic import logic

class game_iteration:
    def iteration(self, game_logic: logic, num_iterations: int) -> bool:
        """Handles a single iteration of the game, prompting the user for input and updating the game state accordingly."""

        for _ in range(num_iterations):
            option = input("Choose an option (1: Answer Correctly (C), 2: Answer Incorrectly (I), 3: Bank (B), 4: Quit (Q)): ")
            
            # Process the user's choice and update the game state
            if option == "1" or option.lower() == "c":
                game_logic.answer_correct()
            elif option == "2" or option.lower() == "i":
                game_logic.answer_incorrect()
            elif option == "3" or option.lower() == "b":
                game_logic.bank()
            elif option == "4" or option.lower() == "q":
                print("Quitting the game.")
                return False
            else:
                raise ValueError("Invalid option. Please choose 1, 2, or 3.")
            
            # Print the current game state after processing the user's choice
            print("\nCurrent player:", game_logic.get_current_player())
            print("Current chain value:", game_logic.get_current_chain_value())
            print("Bank value:", game_logic.get_bank_value())
            if game_logic.get_bank_value() >= 1000:
                print("Congratulations! You've reached 1000 points and won the game!")
                return True