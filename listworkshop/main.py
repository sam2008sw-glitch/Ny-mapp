
from data import get_games

# Mina temperaturer
temperatures = [12, 15, 18, 14, 11]

print("Temperaturer:", temperatures)
print("Antal temperaturer:", len(temperatures))


cities = ["Göteborg", "Malmö", "Stockholm", "Uppsala", "Lund"]

print("Mina städer:", cities)
print("Antal städer:", len(cities))


print("Första staden:", cities[0])
print("Tredje staden:", cities[2])
print("Sista staden:", cities[-1])


cities[1] = "Örebro"

print("Städer efter ändringen:", cities)


games = get_games()

print("Mina favoritspel:", games)
print("Antal spel:", len(games))
