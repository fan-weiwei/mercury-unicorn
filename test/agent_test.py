import unittest
from agents.antifa import Antifa
from agents.spy import Spy
from settings import Settings
from board import Board

class AgentTest(unittest.TestCase):

    def setUp(self):
        self.agent_list = [Antifa(), Spy()]
        settings = Settings(5)
        self.board = Board(settings)

    def test_mission_is_pass_or_fail(self):
        for agent in self.agent_list:
            result = agent.play_mission(self.board)
            self.assertIn(result, ['Pass', 'Fail'])



if __name__ == '__main__':
    unittest.main()
