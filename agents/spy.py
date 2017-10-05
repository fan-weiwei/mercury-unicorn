from agents.agent import Agent
from random import randint

class Spy(Agent):

    def __init__(self):
        super().__init__()
        self.is_spy = True

    def __str__(self):
        return 'Basic Spy'

    def assign_mission(self, board):

        number_to_assign = board.number_to_assign()
        board.add_to_mission(self.seating_position)

        while len(board.players_on_mission) < number_to_assign:
            random_index = randint(0, board.number_of_players - 1)
            if random_index not in board.players_on_mission:
                board.add_to_mission(random_index)

    def play_mission(self, board):
        return 'Fail'

    def vote(self, board):

        if board.stall_counter == 4:
            return 1

        return randint(0, 1)
