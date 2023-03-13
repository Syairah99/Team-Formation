def form_team(players) :
    team = []
    team.append(players[0])
    team.append(players[2])
    return team

players = ["Anis","Ida","Hanim","Sarah","Najwa"]
team = form_team(players)
team[0] = "Syairah"
print(team)