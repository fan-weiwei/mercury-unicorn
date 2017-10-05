class Settings:

    spy_count_lookup = { 5: 2,
                         6: 2,
                         7: 3,
                         8: 3,
                         9: 3,
                        10: 4}

    missions_lookup = { 5:  [2, 3, 2, 3, 3],
                        6:  [2, 3, 4, 3, 4],
                        7:  [2, 3, 3, 4, 4],
                        8:  [3, 4, 4, 5, 5],
                        9:  [3, 4, 4, 5, 5],
                       10:  [3, 4, 4, 5, 5]}


    def __init__(self, number_of_players):

        if number_of_players < 5 or number_of_players > 10:
            raise ValueError

        self.number_of_players    = number_of_players
        self.number_of_spies      = Settings.spy_count_lookup[number_of_players]
        self.missions             = Settings.missions_lookup[number_of_players]
        self.special_fourth_round = number_of_players >= 7


    def __str__(self):

        title    = '\n*** Current Settings ***\n\n'
        players  = 'Number of players   : {}\n'.format(self.number_of_players)
        spies    = 'Number of spies     : {}\n'.format(self.number_of_spies)
        missions = 'Players per mission : {}\n'.format(self.missions)
        fourth   = 'Two fails required on the fourth round? : {}\n'.format(self.special_fourth_round)

        return title + players + spies + missions + '\n' + fourth



