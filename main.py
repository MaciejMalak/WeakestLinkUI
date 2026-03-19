import customtkinter as ctk
from Logic.logic import Logic
from gui import WeakestLinkGUI

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()

    players = ["Player 1", "Player 2", "Player 3"]
    game_logic = Logic(players)
    gui = WeakestLinkGUI(app, game_logic)

    app.mainloop()