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
 
babar = player("P089", "Babar Azam", "Peshawar Zalmi", "BAT", 10.5)
Asif_Ali  = player("P055","Asif Ali","Batter","Lahore Qalandars",6.0)
Saqib_Khan = player("P120","Saqib Khan","Bowller", "Multan Sultans",7.5)
Iftikhar_Ahmed = player("P094","Iftikhar Ahmed","All Rounder", "Peshawar Zalmi", 7.5)
Ali_Raza = player("P096","Ali Raza", "Bowller", "Peshawar Zalmi", 8.5)

for player in [babar, Asif_Ali, Saqib_Khan, Iftikhar_Ahmed, Ali_Raza]:
    print(player)
 


        
     