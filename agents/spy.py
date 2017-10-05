from agents.agent import Agent

class Spy(Agent):

    def __str__(self):
        return 'Basic Spy'

    def is_spy(self):
        return True

    def leader(self):
        pass

    def play_mission(self):
        pass

    def vote(self):
        pass
