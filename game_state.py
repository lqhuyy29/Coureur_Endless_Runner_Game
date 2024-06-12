class GameState:
    """
    Represents the state of the game.
    """
    def __init__(self):
        self.obstacles = []
        self.game_speed_rate = 1
        self.score = 0

    def reset(self):
        self.obstacles.clear()
        self.game_speed_rate = 1
        self.score = 0

game_state = GameState()