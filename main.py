class player:
     """ One real cricketer in the PSL player list."""
    
     def __init__(self, player_id, name,role,franchise, credits):
        self.player_id= player_id
        self.name = name
        self.role = role
        self.franchise = franchise
        self.credits = credits
babar = player("P089", "Babar Azam", "Peshawar Zalmi", "BAT", 10.5)
 
print(babar.name)
print(babar.credits)
print(babar)

        
     