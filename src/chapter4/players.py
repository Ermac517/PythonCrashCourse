players=['charles','martina','michael','florence','eli']
print(players[0:3])  # First three players
print(players[1:4])  # Players from index 1 to 3
print(players[:4])   # First four players
print(players[2:])   # Players from index 2 to the end
print(players[-3:])  # Last three players

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())