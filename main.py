import sqlite3
import pandas
connection = sqlite3.connect("database.sqlite")
#cursor = connection.cursor()
while True:
    print("\n1 Played in 2015\n2 HomeTeam Arsenal\n3 Season 2012-2015\n"
          "4 Team A and M\n5 count\n6 distinct season\n7 min and max\n8 Sum squad players\n9 Average\n10 season 2010 and desc\n11 count home game\n12 matches row 10\n13 Teams_in_Matches,Unique_Teams join(where)\n"
          "14 Teams_in_Matches,Unique_Teams join\n15 Teams join Unique_Teams limit 10\n16 Unique_Teams join Teams LIMIT 5\n17 Max of matches_ID\n")
    choice=int(input("enter a potion : "))
    if(choice==1):
        print(" HomeTeam and AwayTeam in 2015\n")
        print(pandas.read_sql_query("SELECT hometeam,awayteam FROM Matches WHERE date BETWEEN '2015-01-01' and '2015-12-30' and fthg=5",connection))
    elif(choice==2):
        print("HomeTeam='Arsenal' And ftr='A'")
        print(pandas.read_sql_query("SELECT * from matches WHERE hometeam='Arsenal' and ftr='A'", connection))
    elif(choice==3):
        print("season 2012 to 2015")
        print(pandas.read_sql_query("SELECT * from Matches WHERE season BETWEEN '2012' and '2015' and awayteam='Bayern Munich' and ftag>2",connection))
    elif(choice==4):
        print("Team A and M")
        print(pandas.read_sql_query("SELECT * FROM Matches WHERE hometeam LIKE 'A%' AND awayteam LIKE 'M%'", connection))
    elif(choice==5):
        print(pandas.read_sql_query("select count(*) from teams", connection))
    elif(choice==6):
        print(pandas.read_sql_query("select distinct season from teams", connection))
    elif(choice==7):
        print(pandas.read_sql_query("select min(stadiumcapacity),max(stadiumcapacity) from teams", connection))
    elif(choice == 8):
        print(pandas.read_sql_query("SELECt sum(kaderhome) from Teams WHERE season='2014'",connection))
    elif(choice == 9):
        print(pandas.read_sql_query("SELECT avg(fthg) FROM Matches where hometeam='Man United'",connection))
    elif(choice ==10):
        print(pandas.read_sql_query("select hometeam,fthg,ftag from matches where season='2010'and hometeam='Aachen' ORDER BY fthg DESC",connection))
    elif(choice==11):
        print(pandas.read_sql_query("SELECT count(fthg),hometeam FROM Matches  WHERE season='2016' GROUP BY hometeam ORDER by fthg DESC",connection))
    elif(choice ==12):
        print(pandas.read_sql_query("select * from matches LIMIT 10", connection))
    elif(choice == 13):
        print(pandas.read_sql_query("SELECT Teams_in_Matches.match_id,Teams_in_Matches.unique_team_id,Unique_Teams.teamname FROM Teams_in_Matches,Unique_Teams where Teams_in_Matches.Unique_Team_ID=Unique_Teams.Unique_Team_ID",connection))
    elif(choice==14):
        print(pandas.read_sql_query("SELECT Teams_in_Matches.match_id,Teams_in_Matches.unique_team_id,Unique_Teams.teamname FROM Teams_in_Matches inner join Unique_Teams on Teams_in_Matches.Unique_Team_ID=Unique_Teams.Unique_Team_ID",connection))
    elif(choice==15):
        print(pandas.read_sql_query("SELECT * from Teams INNER join Unique_Teams on Teams.teamname=Unique_Teams.TeamName limit 10",connection))
    elif(choice==16):
        print(pandas.read_sql_query("SELECT Unique_Teams.unique_team_id,Unique_Teams.teamname,Teams.avgagehome,Teams.Season,Teams.foreignplayershome from Unique_Teams,Teams LIMIT 5",connection))
    elif(choice == 17):
        print(pandas.read_sql_query("SELECT max(Teams_in_Matches.match_id),Teams_in_Matches.Unique_Team_ID,Unique_Teams.teamname FROM Teams_in_Matches,Unique_Teams where Unique_Teams.teamname LIKE '%y' or Unique_Teams.teamname LIKE '%r' GROUP BY Unique_Teams.TeamName",connection))
    else:
        break