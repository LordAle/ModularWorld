import catalogs_city
import building_kind
import catalogs_profession as cp

# Building kinds
house = building_kind.Building_Kind('House', 20)
service = building_kind.Building_Kind('Service', 5)
shop = building_kind.Building_Kind('Shop', 5)
workshop = building_kind.Building_Kind('Workshop', 5)
stronghold = building_kind.Building_Kind('Stronghold', 0)
religious = building_kind.Building_Kind('Religious', 3)
education = building_kind.Building_Kind('Education', 1)
military = building_kind.Building_Kind('Military', 2)
criminal = building_kind.Building_Kind('Criminal', 2)
art = building_kind.Building_Kind('Art', 1)
other = building_kind.Building_Kind('Other', 0)

kinds = [house, service, shop, workshop, stronghold, religious, education, military, criminal, art, other]

# Building subkinds (kind, name, min_city_size, odds)
farmer = building_kind.Building_Subkind(house, 'Farmer', 0, 20, [cp.farmer_house_master, cp.farmer_house_spouse, cp.farmer_house_child])
commoner = building_kind.Building_Subkind(house, 'Commoner', 0, 10, [cp.commoner_house_master, cp.commoner_house_spouse, cp.commoner_house_child])
bourgeois = building_kind.Building_Subkind(house, 'Bourgeois', 0, 2)
noble = building_kind.Building_Subkind(house, 'Noble', 1, 1)
tavern = building_kind.Building_Subkind(service, 'Tavern', 0, 20)
inn = building_kind.Building_Subkind(service, 'Inn', 1, 10)
hospital = building_kind.Building_Subkind(service, 'Hospital', 1, 2)
whorehouse = building_kind.Building_Subkind(service, 'Whorehouse', 1, 10)
bank = building_kind.Building_Subkind(service, 'Bank', 2, 1)
general_store = building_kind.Building_Subkind(shop, 'General', 0, 20)
food = building_kind.Building_Subkind(shop, 'Food', 0, 10)
health = building_kind.Building_Subkind(shop, 'Health', 1, 5)
book = building_kind.Building_Subkind(shop, 'Book', 1, 2)
magic = building_kind.Building_Subkind(shop, 'Magic', 2, 1)
luxury = building_kind.Building_Subkind(shop, 'Luxury', 2, 2)
blacksmith = building_kind.Building_Subkind(workshop, 'Blacksmith', 0, 2)
tailor = building_kind.Building_Subkind(workshop, 'Tailor', 0, 5)
leatherwork = building_kind.Building_Subkind(workshop, 'Leatherwork', 0, 2)
woodwork = building_kind.Building_Subkind(workshop, 'Woodwork', 0, 4)
other_craft = building_kind.Building_Subkind(workshop, 'Other craft', 1, 1)
keep = building_kind.Building_Subkind(stronghold, 'Keep', 0, 1, [cp.stronghold_master, cp.stronghold_spouse, cp.stronghold_child, cp.keep_servant, cp.keep_security, cp.keep_apprentice, cp.keep_unique, cp.keep_visitor])
castle = building_kind.Building_Subkind(stronghold, 'Castle', 2, 100)
shrine = building_kind.Building_Subkind(religious, 'Shrine', 0, 20)
monastery = building_kind.Building_Subkind(religious, 'Monastery', 0, 10)
church = building_kind.Building_Subkind(religious, 'Church', 1, 4)
cathedral = building_kind.Building_Subkind(religious, 'Cathedral', 2, 1)
school = building_kind.Building_Subkind(education, 'School', 1, 10)
university = building_kind.Building_Subkind(education, 'University', 2, 1)
prison = building_kind.Building_Subkind(military, 'Prison', 1, 20)
barrack = building_kind.Building_Subkind(military, 'Barrack', 1, 20)
fortress = building_kind.Building_Subkind(military, 'Fortress', 2, 1)
army = building_kind.Building_Subkind(military, 'Army', 0, 0)
den = building_kind.Building_Subkind(criminal, 'Den', 1, 1)
front = building_kind.Building_Subkind(criminal, 'Front', 1, 4)
bandit_camp = building_kind.Building_Subkind(criminal, 'Camp', 0, 0)
artist_guild = building_kind.Building_Subkind(art, 'Artist guild', 1, 5)
circus = building_kind.Building_Subkind(art, 'Circus', 1, 2)
museum = building_kind.Building_Subkind(art, 'Museum', 2, 1)
homeless = building_kind.Building_Subkind(other, 'Homeless', 0, 1)
ship = building_kind.Building_Subkind(other, 'Ship', 0, 0)

subkinds = [farmer, commoner, bourgeois, noble, tavern, inn, hospital, whorehouse, bank, general_store, food, health,
            book, magic, luxury, blacksmith, tailor, leatherwork, woodwork, other_craft, keep, castle, shrine,
            monastery, church, cathedral, school, university, prison, barrack, fortress, army, den, front, bandit_camp,
            artist_guild, circus, museum, homeless, ship]

