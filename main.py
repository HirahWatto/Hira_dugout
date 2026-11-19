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

babar = player("P089", "Babar Azam", "BAT", "Peshawar Zalmi", 10.5)
Asif_Ali = player("P055", "Asif Ali", "BAT", "Lahore Qalandars", 6.0)
Saqib_Khan = player("P120", "Saqib Khan", "BOWL", "Multan Sultans", 7.5)
Iftikhar_Ahmed = player("P094", "Iftikhar Ahmed", "AR", "Peshawar Zalmi", 7.5)
Ali_Raza = player("P096", "Ali Raza", "BOWL", "Peshawar Zalmi", 8.5)
Saad_Baig = player("P036", "Saad Baig", "WK", "Hyderabad Kingsmen", 6.0)
Mohammad_Faiq = player("P023", "Mohammad Faiq", "BAT", "Islamabad United", 7.5)
CJ_Green = player("P026", "CJ Green", "AR", "Islamabad United", 7.5)
Usama_Mir = player("P070", "Usama Mir", "BOWL", "Lahore Qalandars", 9.5)
BR_Hampton = player("P116", "BR Hampton", "BOWL", "Multan Sultans", 7.5)
Shahzaib_Khan = player("P127", "Shahzaib Khan", "BAT", "Rawalpindiz", 7.5)

team_players = [
    babar,
    Asif_Ali,
    Saqib_Khan,
    Iftikhar_Ahmed,
    Ali_Raza,
    Saad_Baig,
    Mohammad_Faiq,
    CJ_Green,
    Usama_Mir,
    BR_Hampton,
    Shahzaib_Khan,
]

for selected_player in team_players:
    team.add_player(selected_player)

team.set_captain(babar, Asif_Ali)


def show_pool(players):
    """Print how many players there are per franchise and per role."""
    by_franchise = {}
    by_role = {}

    for pool_player in players:
        by_franchise[pool_player.franchise] = by_franchise.get(pool_player.franchise, 0) + 1
        by_role[pool_player.role] = by_role.get(pool_player.role, 0) + 1

    print("Players by franchise:")
    for franchise in sorted(by_franchise):
        print(f"  {franchise}: {by_franchise[franchise]}")

    print("Players by role:")
    for role in sorted(by_role):
        print(f"  {role}: {by_role[role]}")


def show_team(fantasy_team):
    """Print a team's players, cost and captains."""
    print(f"\nTeam {fantasy_team.team_name} by {fantasy_team.owner}:")
    for team_player in fantasy_team.players:
        print(f"  {team_player}")
    print(f"Total credits: {fantasy_team.total_credits()}")
    print(f"Captain: {fantasy_team.captain.name}, Vice-captain: {fantasy_team.vice_captain.name}")


def main():
    show_pool(team_players)
    show_team(team)
    print("Roles:", team.count_by_role())


if __name__ == "__main__":
    main()








 


        
     