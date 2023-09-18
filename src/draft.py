import bots

class Draft:
    def __init__(self, league, roster_settings=None):
        self.roster_settings = roster_settings
        self.league = league
        self.league.fetch_league()
        self.num_rounds = 17 if roster_settings is None else sum(roster_settings.values())
        roster_size = self.num_rounds * len(self.league.teams)
        players = [
            (3, bots.BpaBot),
            (6, bots.BpaBot),
            (9, bots.BpaBot),
            (7, bots.BpaBot),
            (2, bots.BpaBot),
            (12, bots.BpaBot),
            (1, bots.BpaBot),
            (8, bots.BpaBot),
            (5, bots.BpaBot),
            (4, bots.BpaBot),
            (10, bots.BpaBot),
            (11, bots.BpaBot),
        ]
        self.players = [self._get_bot_for_team_id(team_id, bot_cls) for team_id, bot_cls in players]
        self.available_players = self.league.free_agents(size=max(50, roster_size))

    def _get_bot_for_team_id(self, team_id, bot_cls):
        return bot_cls(self.league, self.league.get_team_data(team_id))

    def _simulate_round(self, round_order):
        for player in round_order:
            choice = player.best_player_available(self.available_players)
            self.available_players.remove(choice)
            player.add_to_roster(choice)

    def simulate_draft(self):
        '''simulate draft'''
        for i in range(self.num_rounds):
            round_order = self.players[::] if i%2==0 else self.players[::-1]
            self._simulate_round(round_order)
