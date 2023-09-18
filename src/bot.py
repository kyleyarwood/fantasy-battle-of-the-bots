#pylint: disable=missing-module-docstring
class Bot: #pylint: disable=too-few-public-methods
    '''Abstract bot class'''#
    def __init__(self, league, team):
        self.league = league
        self.team = team
        self.roster = []

    def _value_of_player(self, player):
        raise NotImplementedError

    def _value_of_team(self, team):
        return sum(self._value_of_player(player) for player in team)

    def best_player_available(self, available_players):
        '''returns best player available'''
        return max(available_players, key=self._value_of_player)
    
    def add_to_roster(self, player):
        self.roster.append(player)
