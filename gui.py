import customtkinter as ctk
from Logic.logic import Logic

class WeakestLinkGUI:
    def __init__(self, root, game_logic: Logic):
        self.root = root
        self.logic = game_logic
        
        self.root.title("Wekeast Link")
        self.root.geometry("600x400")
        
        self.player_label = ctk.CTkLabel(
            self.root, 
            text="Current Player: " + self.logic.get_current_player(), 
            font=("Arial", 20, "bold")
        )
        self.player_label.pack(pady=10)
        
        self.bank_label = ctk.CTkLabel(
            self.root, 
            text="Bank Value: " + str(self.logic.get_bank_value()), 
            font=("Arial", 20, "bold")
        )
        self.bank_label.pack(pady=10)
        
        self.chain_label = ctk.CTkLabel(
            self.root, 
            text="Current Chain Value: " + str(self.logic.get_current_chain_value()), 
            font=("Arial", 20, "bold")
        )
        self.chain_label.pack(pady=10)
        
        self.correct_button = ctk.CTkButton(
            self.root, 
            text="Correct Answer", 
            fg_color="green", hover_color="darkgreen",
            command=self.handle_correct
        )
        self.correct_button.pack(pady=10)

        self.incorrect_button = ctk.CTkButton(
            self.root, 
            text="Incorrect Answer", 
            fg_color="red", hover_color="darkred",
            command=self.handle_incorrect
        )
        self.incorrect_button.pack(pady=10)

        self.bank_button = ctk.CTkButton(
            self.root, 
            text="Bank", 
            fg_color="grey", hover_color="yellow",
            command=self.handle_bank
        )
        self.bank_button.pack(pady=10)

        self.stats_button = ctk.CTkButton(
            self.root,
            text="Show Stats",
            fg_color="blue", hover_color="darkblue",
            command=self.handle_stats
        )
        self.stats_button.pack(pady=10)

    
    def handle_stats(self):
        print("\nCurrent player: ", self.logic._players)
        print("Overall scores: ", self.logic._overall_score)

    def handle_correct(self):
        self.logic.answer_correct()
        self.update_ui() 

    def handle_incorrect(self):
        self.logic.answer_incorrect()
        self.update_ui()

    def handle_bank(self):
        self.logic.bank()
        self.update_ui()
        
    def update_ui(self):
        self.player_label.configure(text=f"Current Player: {self.logic.get_current_player()}")
        self.bank_label.configure(text=f"Bank Value: {self.logic.get_bank_value()}")
        self.chain_label.configure(text=f"Current Chain Value: {self.logic.get_current_chain_value()}")