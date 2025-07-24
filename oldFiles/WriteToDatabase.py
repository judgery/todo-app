import json
import csv

with open("teams.json") as read_file:
    data = json.load(read_file)

# filtered_data = data['data'][1]
filtered_data = data['data']

import collections
counter = collections.defaultdict(int)

for index, teams in enumerate(filtered_data):
    filter2 = teams
    team_id = filter2['id']
    team = filter2['cleanName']
    founded = filter2['founded']
    allsql = (team_id,team,founded)
    print(allsql)
    #print("'",team_id,"'","',",team,"'","',",founded,"'", sep = '')

with open('teams.csv', 'w', newline ='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerow(allsql)


# server='JUDGE-PC\SQLEXPRESS'
# database='FootballStats'
# username='testuser'
# password='test123'
#
# connectionstring = f'Driver={{ODBC Driver 17 for SQL Server}};server={server}; database={database}; uid={username}; pwd={password}'
#
# conn = pyodbc.connect(connectionstring)
# conn.timeout=60
# conn.autocommit = True
#
# cursor = conn.cursor()
#
# cursor.execute("INSERT INTO dbo.Teams([TEAM_ID],[TEAM_NAME],[STADIUM_NAME] VALUES (?,?,?)", ('team_id', 'team', 'founded'))