from abc import ABC, abstractmethod

class Agent(ABC):
    
    def __init__(self):
        self.is_spy = None
        self.seating_position = None
        self.number_of_players = None

    @abstractmethod
    def vote(self, board):
        pass

    @abstractmethod
    def assign_mission(self, board):
        pass

    @abstractmethod
    def play_mission(self, board):
        pass