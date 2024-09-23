"""
Given the following inputs:
- <game_data> is a list of dictionaries, with each dictionary representing a player's shot attempts in a game. The list can be empty, but any dictionary in the list will include the following keys: gameID, playerID, gameDate, fieldGoal2Attempted, fieldGoal2Made, fieldGoal3Attempted, fieldGoal3Made, freeThrowAttempted, freeThrowMade. All values in this dictionary are ints, except for gameDate which is of type str in the format 'MM/DD/YYYY'
- <true_shooting_cutoff> is the minimum True Shooting percentage value for a player to qualify in a game. It will be an int value >= 0.
- <player_count> is the number of players that need to meet the <true_shooting_cutoff> in order for a gameID to qualify. It will be an int value >= 0.

Implement find_qualified_games to return a list of unique qualified gameIDs in which at least <player_count> players have a True Shooting percentage >= <true_shooting_cutoff>, ordered from most to least recent game.
"""

from datetime import datetime

def find_qualified_games(game_data: list[dict], true_shooting_cutoff: int, player_count: int) -> list[int]:
    qualified_games = {}
    
    for player in game_data:
        points_scored = (2 * player['fieldGoal2Made']) + (3 * player['fieldGoal3Made']) + player['freeThrowMade']
        
        total_attempts = (player['fieldGoal2Attempted'] + player['fieldGoal3Attempted']) + 0.44 * player['freeThrowAttempted']
        
        if total_attempts > 0:
            true_shooting_percentage = (points_scored / (2 * total_attempts)) * 100
        else:
            true_shooting_percentage = 0
        
        if true_shooting_percentage >= true_shooting_cutoff:
            game_id = player['gameID']
            
            if game_id not in qualified_games:
                qualified_games[game_id] = {'date': player['gameDate'], 'qualified_count': 0}
            qualified_games[game_id]['qualified_count'] += 1
    
    result = [
        game_id for game_id, info in qualified_games.items() if info['qualified_count'] >= player_count
    ]
    
    result.sort(key=lambda game_id: datetime.strptime(qualified_games[game_id]['date'], '%m/%d/%Y'), reverse=True)
    
    return result

