from settings import Settings
from agents.spy import Spy
from agents.antifa import Antifa
from agents.agent import Agent
from random import shuffle
from board import Board
from typing import List

def generate_players(settings : Settings) -> list:

    print('*** Generating players ***')

    spy_count = settings.number_of_spies
    antifa_count = settings.number_of_antifa

    players: List[Agent] = []
    players += [Spy()    for _ in range(spy_count)]
    players += [Antifa() for _ in range(antifa_count)]

    shuffle(players)

    for index, player in enumerate(players):
        player.seating_position = index
        player.number_of_players = settings.number_of_players

    for player in players:
        print('Player {} : {}'.format(player.seating_position, player))
    print('')

    return players


def run():

    settings = Settings(number_of_players=6)

    players = generate_players(settings)
    board = Board(settings)

    while board.win == None:

        current_leader = board.leader_index
        players[current_leader].assign_mission(board)
        votes =  list(map(lambda player: player.vote(board), players))
        total_passes = sum(votes)
        ratified = total_passes >= board.number_to_pass
        print('Total Passes {}'.format(total_passes))

        if not ratified:
            board.failed_vote()
        else:
            board.successful_vote()
            indexes = board.players_on_mission
            mission_players = list(map(lambda x : players[x], indexes))
            votes = list(map(lambda x : x.play_mission(board), mission_players))

            if 'Fail' not in votes:
                mission_success = True
                print('Mission Success!')
            else:
                mission_success = False

                print('Mission Failed.')

            board.record_is_mission_success(mission_success)


    if board.win:
        print('*** Resistance wins ***')
    else:
        print('*** Spies win ***')





