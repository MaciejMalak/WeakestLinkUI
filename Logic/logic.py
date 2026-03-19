class Logic:
    def __init__(self, players: list[str]):
        self._current_player = 0
        self._players = players
        self._overall_score = [0]*len(players)
        self._current_chain = 0
        self._chain = [0,20,50,100,200,300,450,600,800,1000]
        self.bank_val = 0


    def get_current_player(self) -> str:
        """Returns the name of the current player."""

        return self._players[self._current_player]
    
    def get_bank_value(self) -> int:
        """Returns the current bank value."""

        return self.bank_val

    def get_current_chain_value(self) -> int:
        """Returns the value of the current chain."""

        return self._chain[self._current_chain]
    


    def answer_correct(self):
        """Handles the logic for when a player answers correctly."""

        self._overall_score[self._current_player] += self._chain[self._current_chain]
        if self._current_chain < len(self._chain)-1:
            self._current_chain += 1
            self._current_player = (self._current_player + 1) % len(self._players)
        else:
            self._current_chain = 0
            print("Reached the end of the chain, resetting to 0")


    def answer_incorrect(self):
        """Handles the logic for when a player answers incorrectly."""

        self._overall_score[self._current_player] -= self._chain[self._current_chain]
        self._current_chain = 0
        self._current_player = (self._current_player + 1) % len(self._players)

    def bank(self):
        """Handles the logic for when a player decides to bank their current chain."""

        self._overall_score[self._current_player] += (self._chain[self._current_chain]/2)
        self.bank_val += self._chain[self._current_chain]
        self._current_chain = 0
        if self.bank_val >= 1000:
            print("Congratulations! You've reached 1000 points and won the game!")
            self.bank_val = 0
    