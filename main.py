import mysql.connector

databa_config = {
    "user": "tournament_user",
    "password": "tournament_pass",
    "host": "localhost",
    "database": "football"
}


select_gk = """
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
"""

select_def = """
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
"""

select_at = """
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
"""

conn = mysql.connector.connect(**databa_config)
cursor = conn.cursor()

cursor.execute(select_gk)
goalkeepers = cursor.fetchall()

cursor.execute(select_def)
defensors = cursor.fetchall()

cursor.execute(select_at)
attackers = cursor.fetchall()

with open('goalkeepers.csv', 'w') as f:
    f.write('Name,Nationality,Birth Year,Position,Height,Weight,Club,Matches,Defenses,Goals Conceded,Clean Sheets\n')
    for keepers in goalkeepers:
        for item in enumerate(keepers):
            f.write(str(item[-1]))
            if (item[0]+1) != len(keepers): f.write(',')
        f.write('\n')

with open('defensors.csv', 'w') as f:
    f.write('Name,Nationality,Birth Year,Position,Height,Weight,Club,Matches,Tackles,Clearances,Clean Sheets\n')
    for defensor in defensors:
        for item in enumerate(defensor):
            f.write(str(item[-1]))
            if (item[0]+1) != len(defensor): f.write(',')
        f.write('\n')

with open('attackers.csv', 'w') as f:
    f.write('Name,Nationality,Birth Year,Position,Height,Weight,Club,Matches,Goals,Assists\n')
    for attacker in attackers:
        for item in enumerate(attacker):
            f.write(str(item[-1]))
            if (item[0]+1) != len(attacker): f.write(',')
        f.write('\n')