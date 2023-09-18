from bot import Bot

SCORING = {
    'G': 3,
    'A': 2,
    'PPP': 1,
    'SHP': 1,
    'SV': 0.2,
    'W': 4,
    'SO': 2,
    'GA': -2,
}

class BpaBot(Bot):
    def __init__(self, league, team):
        super().__init__(league, team)

    def _value_of_player(self, player):
        value = 0
        projections = player.stats['Projected 2024']['total']
        for cat, wgt in SCORING.items():
            value += projections.get(cat, 0)*wgt
        return value
