from espn_api.hockey import League
from dotenv import load_dotenv
from os import getenv

from bots import BpaBot
from draft import Draft



load_dotenv()

LEAGUE_ID = int(getenv('LEAGUE_ID'))
YEAR = int(getenv('YEAR'))
league = League(league_id=LEAGUE_ID, year=YEAR)

draft = Draft(league)
draft.simulate_draft()
for player in draft.players:
    print(player.roster)
