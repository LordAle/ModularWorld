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
commoner = building_kind.Building_Subkind(house, 'Commoner', 0, 10, [cp.commoner_house_master, cp.commoner_house_spouse, cp.child_commoner])
bourgeois = building_kind.Building_Subkind(house, 'Bourgeois', 0, 2, [cp.bourgeois_house_master, cp.bourgeois_house_spouse, cp.child_bourgeois, cp.maid_2, cp.guard_1])
noble = building_kind.Building_Subkind(house, 'Noble', 1, 1, [cp.noble_house_master, cp.spouse_same, cp.child_same, cp.maid_3, cp.guard_2])
tavern = building_kind.Building_Subkind(service, 'Tavern', 0, 20, [cp.tavern_master, cp.spouse_same, cp.child_commoner])
inn = building_kind.Building_Subkind(service, 'Inn', 1, 10, [cp.inn_master, cp.spouse_same, cp.child_commoner, cp.maid_2])
hospital = building_kind.Building_Subkind(service, 'Hospital', 1, 2, [cp.hospital_master, cp.spouse_assistant, cp.child_bourgeois, cp.hospital_apprentice, cp.assistant_3, cp.maid_2])
whorehouse = building_kind.Building_Subkind(service, 'Whorehouse', 1, 10, [cp.whorehouse_master, cp.whorehouse_servant, cp.guard_1])
bank = building_kind.Building_Subkind(service, 'Bank', 2, 1, [cp.bank_master, cp.spouse_assistant, cp.child_bourgeois, cp.assistant_1, cp.maid_1, cp.guard_3])
general_store = building_kind.Building_Subkind(shop, 'General', 0, 20, [cp.general_master, cp.spouse_assistant, cp.child_commoner])
food = building_kind.Building_Subkind(shop, 'Food', 0, 10, [cp.food_master, cp.spouse_assistant, cp.child_commoner, cp.assistant_1])
health = building_kind.Building_Subkind(shop, 'Health', 1, 5, [cp.health_master, cp.spouse_assistant, cp.child_bourgeois, cp.assistant_0, cp.guard_0])
book = building_kind.Building_Subkind(shop, 'Book', 1, 2, [cp.book_master, cp.spouse_assistant, cp.child_bourgeois, cp.guard_0])
magic = building_kind.Building_Subkind(shop, 'Magic', 2, 1, [cp.magic_master, cp.spouse_assistant, cp.child_bourgeois, cp.guard_1])
luxury = building_kind.Building_Subkind(shop, 'Luxury', 2, 2, [cp.luxury_master, cp.spouse_assistant, cp.child_bourgeois, cp.guard_1])
blacksmith = building_kind.Building_Subkind(workshop, 'Blacksmith', 0, 2, [cp.blacksmith_master, cp.spouse_assistant, cp.child_craftsman, cp.tenter_2, cp.apprentice_craftsman])
tailor = building_kind.Building_Subkind(workshop, 'Tailor', 0, 4, [cp.tailor_master, cp.spouse_assistant, cp.child_craftsman, cp.tenter_1, cp.apprentice_craftsman])
leatherwork = building_kind.Building_Subkind(workshop, 'Leatherwork', 0, 2, [cp.leatherwork_master, cp.spouse_assistant, cp.child_craftsman, cp.tenter_1, cp.apprentice_craftsman])
woodwork = building_kind.Building_Subkind(workshop, 'Woodwork', 0, 3, [cp.woodwork_master, cp.spouse_assistant, cp.child_craftsman, cp.tenter_1, cp.apprentice_craftsman])
builder = building_kind.Building_Subkind(workshop, 'Builder', 0, 4, [cp.builder_master, cp.spouse_assistant, cp.child_craftsman, cp.tenter_2, cp.apprentice_craftsman])
other_craft = building_kind.Building_Subkind(workshop, 'Other craft', 1, 1, [cp.other_craft_master, cp.spouse_assistant, cp.child_craftsman, cp.tenter_0, cp.apprentice_craftsman])
keep = building_kind.Building_Subkind(stronghold, 'Keep', 0, 1, [cp.stronghold_master, cp.stronghold_spouse, cp.stronghold_child, cp.keep_servant, cp.keep_security, cp.keep_apprentice, cp.keep_unique, cp.keep_visitor])
castle = building_kind.Building_Subkind(stronghold, 'Castle', 2, 100, [cp.stronghold_master, cp.stronghold_spouse, cp.stronghold_child, cp.castle_servant, cp.castle_security, cp.castle_apprentice, cp.castle_unique, cp.castle_visitor])
shrine = building_kind.Building_Subkind(religious, 'Shrine', 0, 20, [cp.shrine_master, cp.priest_0])
monastery = building_kind.Building_Subkind(religious, 'Monastery', 0, 10, [cp.monastery_master, cp.monastery_apprentice])
church = building_kind.Building_Subkind(religious, 'Church', 1, 4, [cp.church_master, cp.priest_2, cp.maid_1])
cathedral = building_kind.Building_Subkind(religious, 'Cathedral', 2, 1, [cp.cathedral_master, cp.priest_3, cp.maid_2, cp.guard_3])
school = building_kind.Building_Subkind(education, 'School', 1, 10, [cp.school_master, cp.school_teachers])
university = building_kind.Building_Subkind(education, 'University', 2, 1, [cp.university_master, cp.university_professors, cp.university_servant, cp.guard_3])
prison = building_kind.Building_Subkind(military, 'Prison', 1, 20, [cp.prison_master, cp.prison_jailers])
barrack = building_kind.Building_Subkind(military, 'Barrack', 1, 20, [cp.barrack_master, cp.barrack_soldier, cp.maid_2])
fortress = building_kind.Building_Subkind(military, 'Fortress', 2, 1, [cp.fortress_master, cp.fortress_soldier, cp.fortress_craftsman, cp.fortress_servant])
army = building_kind.Building_Subkind(military, 'Army', 0, 0, [cp.fortress_master, cp.fortress_soldier, cp.fortress_craftsman, cp.fortress_servant])
den = building_kind.Building_Subkind(criminal, 'Den', 1, 1, [cp.den_master, cp.den_criminals])
front = building_kind.Building_Subkind(criminal, 'Front', 1, 4, [cp.front_master, cp.guard_1])
bandit_camp = building_kind.Building_Subkind(criminal, 'Camp', 0, 0, [cp.camp_master, cp.camp_criminals])
artist_guild = building_kind.Building_Subkind(art, 'Artist guild', 1, 5, [cp.artist_master, cp.artist_members])
circus = building_kind.Building_Subkind(art, 'Circus', 0, 2, [cp.circus_master, cp.circus_member])
museum = building_kind.Building_Subkind(art, 'Museum', 2, 1, [cp.museum_master, cp.museum_apprentice, cp.guard_2])
homeless = building_kind.Building_Subkind(other, 'Homeless', 0, 1, [cp.homeless_master])
ship = building_kind.Building_Subkind(other, 'Ship', 0, 0, [cp.ship_master, cp.ship_navigator, cp.ship_sailor])

subkinds = [farmer, commoner, bourgeois, noble, tavern, inn, hospital, whorehouse, bank, general_store, food, health,
            book, magic, luxury, blacksmith, tailor, leatherwork, woodwork, other_craft, keep, castle, shrine,
            monastery, church, cathedral, school, university, prison, barrack, fortress, army, den, front, bandit_camp,
            artist_guild, circus, museum, homeless, ship]

