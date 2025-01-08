players = {"Suarez": "Uruguay", "Messi": "Argentina", "Coutinho": "Brazil", "Vidal": "Chile", "Rakitic": "Croatia", "Busquets": "Spain", "Roberto": "Spain", "Pique": "Spain", "Lenglet": "France", "Alba": "Spain", "Ter Stegen": "Germany"}

playersSet = set()
for player in players:
  playersSet.add(players[player])
  
print("FC Barcelona has players from " + str(len(playersSet)) + " different countries.")

print("FC Barcelona's players come from:")
for nation in playersSet:
  print(nation)