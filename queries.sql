-- select attacking players
SELECT players.name, players.nationality, players.birth_year, 
players.position, players.height, players.weight, 
clubs.name, player_stats.matches, player_stats.goals,
player_stats.assists 
FROM players 
INNER JOIN players_contract
INNER JOIN clubs
INNER JOIN player_stats
    ON players.id = players_contract.id_player
    AND players.id = player_stats.id_player
    AND clubs.id = players_contract.id_club
WHERE 
players.position = 'CF' OR  
players.position = 'SS' OR
players.position = 'AM' OR 
players.position = 'WG' OR 
players.position = 'LM' OR 
players.position = 'RM';

-- select defensors
SELECT players.name, players.nationality, players.birth_year, 
players.position, players.height, players.weight, 
clubs.name, player_stats.matches, player_stats.tackles,
player_stats.clearances, player_stats.clean_sheets
FROM players 
INNER JOIN players_contract
INNER JOIN clubs
INNER JOIN player_stats
    ON players.id = players_contract.id_player
    AND players.id = player_stats.id_player
    AND clubs.id = players_contract.id_club
WHERE 
players.position = 'CB' OR  
players.position = 'RB' OR
players.position = 'LB' OR 
players.position = 'DM' OR 
players.position = 'CM';

-- select goalkeepers
SELECT players.name, players.nationality, players.birth_year, 
players.position, players.height, players.weight, 
clubs.name, player_stats.matches, player_stats.defenses, 
player_stats.goals_conceded, player_stats.clean_sheets
FROM players 
INNER JOIN players_contract
INNER JOIN clubs
INNER JOIN player_stats
    ON players.id = players_contract.id_player
    AND players.id = player_stats.id_player
    AND clubs.id = players_contract.id_club
WHERE 
players.position = 'GK';