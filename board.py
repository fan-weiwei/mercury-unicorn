class Board:

    def __init__(self, settings):

        self.number_of_players = settings.number_of_players
        self.number_to_pass = settings.number_to_pass
        self.missions = settings.missions
        self.spy_score = 0
        self.antifa_score = 0
        self.current_mission = 0
        self.stall_counter = 0
        self.players_on_mission = []
        self.win = None

        print('Settings player 0 as leader\n')
        self.leader_index = 0

    def number_to_assign(self):
        return self.missions[self.current_mission]


    def add_to_mission(self, index):
        """ Add a player index to mission, must be unique players """

        if index < 0 or index >= self.number_of_players:
            raise IndexError

        if index in self.players_on_mission:
            raise ValueError

        if len(self.players_on_mission) >= self.number_to_assign():
            raise OverflowError

        self.players_on_mission += [index]

    def increment_stall_counter(self):
        """ Increment stall counter, if it reaches 5 automatic loss """
        if self.stall_counter >=5:
            raise OverflowError

        self.stall_counter += 1

        if self.stall_counter >= 5:
            self.win = False

    def failed_vote(self):
        print('Vote Failed!\n')
        self.increment_stall_counter()
        self.reset_mission()

    def successful_vote(self):
        print('Vote Successful!')
        self.stall_counter = 0

    def reset_mission(self):
        self.leader_index = (self.leader_index + 1) % self.number_of_players
        self.players_on_mission = []

    def record_is_mission_success(self, is_success):
        if is_success:
            self.antifa_score += 1
        else:
            self.spy_score +=1

        print('Spies: {} Resistance: {}\n'.format(self.spy_score, self.antifa_score))

        if self.antifa_score == 3:
            self.win = True
            return

        if self.spy_score == 3:
            self.win = False
            return

        self.current_mission += 1
        self.reset_mission()






