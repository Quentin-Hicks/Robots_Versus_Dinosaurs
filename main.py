from battlefield import Battlefield
from fleet import Fleet

battle_one = Battlefield()

fleet_one = Fleet()
print(fleet_one.list)

fleet_one.create_fleet()
print(fleet_one.list)