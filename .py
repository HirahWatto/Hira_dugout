class player:
     """ One real cricketer in the PSL player list."""
    
     def __init__(self, player_id, name,role,franchise, credits):
        self.player_id= player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits

     def __str__(self):
        return f"{self.name} ({self.franchise}, {self.role}, {self.credits} cr)"

class FantasyTeam:
    """A fantasy XI picked by one person."""
 
    def __init__(self, team_name, owner):
        self.team_name = team_name
        self.owner = owner
        self.players = []
        self.captain = None
        self.vice_captain = None
 
    def add_player(self, player):
        self.players.append(player)

    def total_credits(self):
            total = 0
            for player in self.players:
                total = total + player.credits
            return total
    
    def count_by_role(self):
            counts = {"WK": 0, "BAT": 0, "AR": 0, "BOWL": 0}
            for player in self.players:
                counts[player.role] = counts[player.role] + 1
            return counts

    def set_captain(self, captain, vice_captain):
        self.captain = captain
        self.vice_captain = vice_captain
 
    def __str__(self):
        size = len(self.players)
        cost = self.total_credits()
        return f"{self.team_name} (owner: {self.owner}, {size} players, {cost} cr)"

team = FantasyTeam("Dugout Demo XI", "Hirah")   
babar = player("P089", "Babar Azam", "Peshawar Zalmi", "BAT", 10.5)
Asif_Ali  = player("P055","Asif Ali","Batter","Lahore Qalandars",6.0)
Saqib_Khan = player("P120","Saqib Khan","Bowller", "Multan Sultans",7.5)
Iftikhar_Ahmed = player("P094","Iftikhar Ahmed","All Rounder", "Peshawar Zalmi", 7.5)
Ali_Raza = player("P096","Ali Raza", "Bowller", "Peshawar Zalmi", 8.5)
Saad_Baig = player("P036","Saas Baig","WK","Hyderabad Kingsmen", 6.0)
Mohammad_Faiq = player("P023","Mohammad Faiq","Batter","Islamabad United",7.5)
CJ_Green = player("P026", "CJ Green", "All Rounder", "Islamabad United",7.5)
Usama_Mir = player("P070","Usama Mir", "Bowller", "Lahore Qalandars",9.5)
BR_Hampton = player("P116","BR Hampton","Bowller", "Multan Sultans", 7.5)
Shahzaib_Khan = player("P127","Shahzaib Khan","Batter","Rawalpindiz", 7.5)



for player in [babar, Asif_Ali, Saqib_Khan, Iftikhar_Ahmed, Ali_Raza, Saad_Baig, Mohammad_Faiq, CJ_Green, Usama_Mir, BR_Hampton, Shahzaib_Khan]:
    team.set_captain(babar, Asif_Ali)

print(team)
print("Roles:", team.count_by_role())
print("Captain:", team.captain)
print("Vice-captain:", team.vice_captain)







 


        
     