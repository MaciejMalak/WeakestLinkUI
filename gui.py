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
            text="Poprawna odpowiedź", 
            fg_color="green", hover_color="darkgreen",
            command=self.handle_correct
        )
        self.correct_button.pack(pady=10)

    
    def handle_correct(self):
        self.logic.answer_correct()
        self.update_ui() 
        
    def update_ui(self):
        self.player_label.configure(text=f"Current Player: {self.logic.get_current_player()}")
        self.bank_label.configure(text=f"Bank Value: {self.logic.get_bank_value()}")
        self.chain_label.configure(text=f"Current Chain Value: {self.logic.get_current_chain_value()}")