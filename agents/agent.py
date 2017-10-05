from abc import ABC, abstractmethod

class Agent(ABC):

    @abstractmethod
    def is_spy(self):
        pass

    @abstractmethod
    def vote(self):
        pass

    @abstractmethod
    def leader(self):
        pass

    @abstractmethod
    def play_mission(self):
        pass