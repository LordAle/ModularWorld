from objects import role_professions as rp
from objects import profession

# Sources:
#   Medieval demographics made easy By S. John Ross http://www222.pair.com/sjohn/blueroom/demog.htm
#   What did people do in a Medieval City? By Shawn Vincent http://www.svincent.com/MagicJar/Economics/MedievalOccupations.html

# Professions definition
# (name, wealth, [class], [odds of class], geography
# Geography is used to specify a required geographical feature. Support: [Plains, Forests, River, Sea, Mountains, Mines and Water (River or Sea)]

# Governance
catchpole = profession.Profession('Catchpole', 1.2, ['Expert'], [1])
chancellor = profession.Profession('Chancellor', 1.9, ['Expert', 'Wizard'], [100, 1])
diplomat = profession.Profession('Diplomat', 1.7, ['Expert'], [1])
exchequer = profession.Profession('Exchequer', 1.9, ['Expert'], [1])
forester = profession.Profession('Forester', 1.6, ['Expert', 'Ranger'], [10, 1], 'Forests')
hayward = profession.Profession('Hayward', 1.6, ['Expert'], [1])
herald = profession.Profession('Herald', 1.1, ['Expert'], [1])
judge = profession.Profession('Judge', 2, ['Expert'], [1])
knight = profession.Profession('Knight', 1.8, ['Fighter', 'Paladin'], [50, 1])
liner = profession.Profession('Liner', 1.5, ['Expert'], [1])
local_lord = profession.Profession('Local Lord', 2, ['Expert', 'Fighter'], [10, 3])
noble = profession.Profession('Noble', 2, ['Expert', 'Sorcerer', 'Wizard'], [100, 1, 1])
summoner = profession.Profession('Summoner', 1.1, ['Expert'], [1])
# Military
bowman = profession.Profession('Bowman', 0.3, ['Warrior', 'Fighter'], [10, 1])
engineer = profession.Profession('Engineer', 0.9, ['Expert', 'Fighter'], [10, 1])
footman = profession.Profession('Footman', 0.2, ['Warrior', 'Fighter'], [10, 1])
mercenary = profession.Profession('Mercenary', 0.3, ['Warrior', 'Fighter'], [5, 1])
pikeman = profession.Profession('Pikeman', 0.3, ['Warrior', 'Fighter'], [10, 1])
sapper = profession.Profession('Sapper', 0.4, ['Expert', 'Rogue'], [10, 1])
scout = profession.Profession('Scout', 0.2, ['Warrior', 'Fighter', 'Rogue', 'Ranger'], [10, 1, 1, 1])
sergeant = profession.Profession('Sergeant', 0.7, ['Warrior', 'Fighter'], [10, 1])
general = profession.Profession('General', 1.5, ['Fighter'], [1])
# Security
bailiff = profession.Profession('Bailiff', 1.5, ['Expert', 'Fighter'], [10, 1])
constable = profession.Profession('Constable', 1.5, ['Fighter'], [1])
guard = profession.Profession('Guard', 0.1, ['Warrior', 'Fighter'], [10, 1])
guard_captain = profession.Profession('Guard Captain', 0.2, ['Fighter'], [1])
jailer = profession.Profession('Jailer', 0.1, ['Warrior', 'Fighter'], [10, 1])
sheriff = profession.Profession('Sheriff', 0.9, ['Fighter'], [1])
# Criminal
burglar = profession.Profession('Burglar', 0.05, ['Expert', 'Rogue'], [5, 1])
con_artist = profession.Profession('Con Artist', 0.2, ['Expert'], [1])
fence = profession.Profession('Fence', 0.4, ['Expert', 'Rogue'], [5, 1])
footpad = profession.Profession('Footpad', 0.05, ['Rogue', 'Fighter', 'Warrior'], [2, 1, 5])
pickpocket = profession.Profession('Pickpocket', 0, ['Expert', 'Rogue'], [5, 1])
poacher = profession.Profession('Poacher', 0, ['Expert', 'Ranger'], [10, 1], 'Forests')
# Religious
archbishop = profession.Profession('Archbishop', 1.9, ['Cleric'], [1])
bishop = profession.Profession('Bishop', 1.8, ['Cleric'], [1])
cardinal = profession.Profession('Cardinal', 2, ['Cleric'], [1])
monk = profession.Profession('Monk', 0, ['Expert', 'Monk'], [5, 1])
priest = profession.Profession('Priest', 0.4, ['Cleric'], [1])
# Merchant
apothecary = profession.Profession('Apothecary', 1, ['Expert'], [1])
banker = profession.Profession('Banker', 2, ['Expert'], [1])
innkeeper = profession.Profession('Innkeeper', 0.7, ['Expert'], [1])
merchant_book = profession.Profession('Book Merchant', 1.1, ['Expert'], [1])
merchant_cloth = profession.Profession('Cloth Merchant', 0.1, ['Expert'], [1])
merchant_food = profession.Profession('Food Merchant', 0.1, ['Expert'], [1])
merchant_fuel = profession.Profession('Fuel Merchant', 0.1, ['Expert'], [1])
merchant_jewelry = profession.Profession('Jewelry Merchant', 1.2, ['Expert'], [1])
merchant_magic = profession.Profession('Magic Merchant', 1.2, ['Expert', 'Wizard', 'Sorcerer'], [5, 1, 1])
merchant_skin = profession.Profession('Skin Merchant', 0.1, ['Expert'], [1])
merchant_spice = profession.Profession('Spice Merchant', 1, ['Expert'], [1])
merchant_stone = profession.Profession('Stone Merchant', 0.1, ['Expert'], [1])
merchant_textile = profession.Profession('Textile Merchant', 0.1, ['Expert'], [1])
merchant_wood = profession.Profession('Wood Merchant', 0.1, ['Expert'], [1])
# Entertainer
acrobat = profession.Profession('Acrobat', 0, ['Expert', 'Rogue'], [5, 1])
actor = profession.Profession('Actor', 0.1, ['Expert', 'Bard'], [5, 1])
musician = profession.Profession('Musician', 0.1, ['Expert', 'Bard'], [5, 1])
painter = profession.Profession('Painter', 0.1, ['Expert'], [1])
sculptor = profession.Profession('Sculptor', 0.1, ['Expert'], [1])
writer = profession.Profession('Writer', 0.1, ['Expert'], [1])
# Food provider
farmer = profession.Profession('Farmer', 0, ['Expert'], [1])
fisherman = profession.Profession('Fisherman', 0, ['Expert'], [1], 'Water')
herder = profession.Profession('Herder', 0.2, ['Expert'], [1], 'Plains')
hunter = profession.Profession('Hunter', 0, ['Expert'], [1])
# Scholar
alchemist = profession.Profession('Alchemist', 0.5, ['Expert'], [1])
astronomer = profession.Profession('Astronomer', 1.1, ['Expert'], [1], 'Mountains')
historian = profession.Profession('Historian', 0.5, ['Expert'], [1])
librarian = profession.Profession('Librarian', 0, ['Expert'], [1])
mathematician = profession.Profession('Mathematician', 0.5, ['Expert'], [1])
mage = profession.Profession('Mage', 1.1, ['Wizard'], [1])
philosopher = profession.Profession('Philosopher', 0.5, ['Expert'], [1])
professor = profession.Profession('Professor', 0.5, ['Expert'], [1])
theologian = profession.Profession('Theologian', 0.5, ['Expert', 'Cleric'], [2, 1])
# Sailor
navigator = profession.Profession('Navigator', 0.5, ['Expert'], [1], 'Sea')
sailor = profession.Profession('Sailor', 0, ['Expert'], [1], 'Sea')
captain = profession.Profession('Captain', 0.8, ['Expert'], [1], 'Sea')
sailmaker = profession.Profession('Sailmaker', 0.1, ['Expert'], [1], 'Water')
shipwright = profession.Profession('Shipwright', 0.4, ['Expert'], [1], 'Water')
# Craftsman
shoemaker = profession.Profession('Shoemaker', 0.01, ['Expert'], [1])
furrier = profession.Profession('Furrier', 0.01, ['Expert'], [1])
tailor = profession.Profession('Tailor', 0.01, ['Expert'], [1])
jeweler = profession.Profession('Jeweler', 0.9, ['Expert'], [1])
pastrycook = profession.Profession('Pastrycook', 0, ['Expert'], [1])
mason = profession.Profession('Mason', 0.01, ['Expert'], [1])
carpenter = profession.Profession('Carpenter', 0.01, ['Expert'], [1])
weaver = profession.Profession('Weaver', 0, ['Expert'], [1])
chandler = profession.Profession('Chandler', 0.01, ['Expert'], [1])
cooper = profession.Profession('Cooper', 0, ['Expert'], [1])
baker = profession.Profession('Baker', 0, ['Expert'], [1])
hatmaker = profession.Profession('Hatmaker', 0.01, ['Expert'], [1])
saddler = profession.Profession('Saddler', 0.01, ['Expert'], [1])
chicken_butcher = profession.Profession('Chicken Butcher', 0, ['Expert'], [1])
pursemaker = profession.Profession('Pursemaker', 0, ['Expert'], [1])
butcher = profession.Profession('Butcher', 0.01, ['Expert'], [1])
buckle_maker = profession.Profession('Buckle-maker', 0, ['Expert'], [1])
plasterer = profession.Profession('Plasterer', 0, ['Expert'], [1])
blacksmith = profession.Profession('Blacksmith', 0.01, ['Expert'], [1])
painter_craft = profession.Profession('Painter (Building)', 0, ['Expert'], [1])
roofer = profession.Profession('Roofer', 0, ['Expert'], [1])
locksmith = profession.Profession('Locksmith', 0.01, ['Expert'], [1])
ropemaker = profession.Profession('Ropemaker', 0, ['Expert'], [1])
tanner = profession.Profession('Tanner', 0, ['Expert'], [1])
harness_maker = profession.Profession('Harness-Maker', 0, ['Expert'], [1])
bleacher = profession.Profession('Bleacher', 0, ['Expert'], [1])
cutler = profession.Profession('Cutler', 0.01, ['Expert'], [1])
glovemaker = profession.Profession('Glovemaker', 0.01, ['Expert'], [1])
woodcarver = profession.Profession('Woodcarver', 0.01, ['Expert'], [1])
accoutrement_maker = profession.Profession('Accoutrement Maker', 0.01, ['Expert'], [1])
arkwright = profession.Profession('Arkwright', 0.01, ['Expert'], [1])
armorer = profession.Profession('Armorer', 0.05, ['Expert', 'Fighter'], [25, 1])
balancemaker = profession.Profession('Balancemaker', 0.05, ['Expert'], [1])
basketmaker = profession.Profession('Basketmaker', 0, ['Expert'], [1])
brewer = profession.Profession('Brewer', 0.01, ['Expert'], [1])
bellmaker = profession.Profession('Bellmaker', 0.01, ['Expert'], [1])
bottelier = profession.Profession('Bottelier', 0, ['Expert'], [1])
bowyer = profession.Profession('Bowyer', 0.05, ['Expert', 'Fighter'], [25, 1])
brickmaker = profession.Profession('Brickmaker', 0, ['Expert'], [1])
broom_maker = profession.Profession('Broom Maker', 0, ['Expert'], [1])
canvasser = profession.Profession('Canvasser', 0, ['Expert'], [1])
card_maker = profession.Profession('Card Maker', 0.01, ['Expert'], [1])
cartographer = profession.Profession('Cartographer', 0.3, ['Expert'], [1])
cartwright = profession.Profession('Cartwright', 0.01, ['Expert'], [1])
chainmaker = profession.Profession('Chainmaker', 0, ['Expert'], [1])
cheesemaker = profession.Profession('Cheesemaker', 0.01, ['Expert'], [1])
clockmaker = profession.Profession('Clockmaker', 0.05, ['Expert'], [1])
dyer = profession.Profession('Dyer', 0, ['Expert'], [1])
embroiderer = profession.Profession('Embroiderer', 0.01, ['Expert'], [1])
feltmaker = profession.Profession('Feltmaker', 0, ['Expert'], [1])
fletcher = profession.Profession('Fletcher', 0.01, ['Expert'], [1])
foundryman = profession.Profession('Foundryman', 0, ['Expert'], [1], 'Mines')
girdler = profession.Profession('Girdler', 0, ['Expert'], [1])
glassblower = profession.Profession('Glassblower', 0.01, ['Expert'], [1])
horner = profession.Profession('Horner', 0.01, ['Expert', 'Bard'], [5, 1])
illuminator = profession.Profession('Illuminator', 0.05, ['Expert'], [1])
lampwright = profession.Profession('Lampwright', 0.01, ['Expert'], [1])
luthier = profession.Profession('Luthier', 0.01, ['Expert', 'Bard'], [5, 1])
minter = profession.Profession('Minter', 1.5, ['Expert'], [1])
mirrorer = profession.Profession('Mirrorer', 0.01, ['Expert'], [1])
nedeller = profession.Profession('Nedeller', 0, ['Expert'], [1])
parchmenter = profession.Profession('Parchmenter', 0, ['Expert'], [1])
rectifier = profession.Profession('Rectifier', 0.01, ['Expert'], [1])
reedmaker = profession.Profession('Reedmaker', 0.01, ['Expert', 'Bard'], [5, 1])
rugweaver = profession.Profession('Rugweaver', 0.01, ['Expert'], [1])
spectaclemaker = profession.Profession('Spectaclemaker', 0.01, ['Expert'], [1])
stonecutter = profession.Profession('Stonecutter', 0.01, ['Expert'], [1])
tapicer = profession.Profession('Tapicer', 0.01, ['Expert'], [1])
vintner = profession.Profession('Vintner', 0.01, ['Expert'], [1])
wheelwright = profession.Profession('Wheelwright', 0, ['Expert'], [1])
# Service
advocate = profession.Profession('Advocate', 0.9, ['Expert'], [1])
architect = profession.Profession('Architect', 0.9, ['Expert'], [1])
assistant = profession.Profession('Assistant', 0, ['Expert'], [1])
barber = profession.Profession('Barber', 0, ['Expert'], [1])
bather = profession.Profession('Bather', 0, ['Expert'], [1])
builder = profession.Profession('Builder', 0, ['Expert'], [1])
carter = profession.Profession('Carter', 0, ['Expert'], [1])
copyist = profession.Profession('Copyist', 0, ['Expert'], [1])
dentist = profession.Profession('Dentist', 0.5, ['Expert'], [1])
doctor = profession.Profession('Doctor', 0.6, ['Expert'], [1])
falconer = profession.Profession('Falconer', 0.9, ['Expert'], [1])
fewterer = profession.Profession('Fewterer', 0.8, ['Expert'], [1])
ferryman = profession.Profession('Ferryman', 0, ['Expert'], [1], 'River')
gardner = profession.Profession('Gardner', 0.01, ['Expert'], [1])
gravedigger = profession.Profession('Gravedigger', 0, ['Expert'], [1])
horse_groomer = profession.Profession('Horse Groomer', 0.3, ['Expert'], [1], 'Plains')
launderer = profession.Profession('Launderer', 0, ['Expert'], [1])
link_boy = profession.Profession('Link Boy', 0, ['Expert'], [1])
maid = profession.Profession('Maid', 0, ['Expert'], [1])
messanger = profession.Profession('Messanger', 0, ['Expert'], [1])
miner = profession.Profession('Miner', 0, ['Expert'], [1], 'Mines')
miller = profession.Profession('Miller', 0.2, ['Expert'], [1])
midwife = profession.Profession('Midwife', 0, ['Expert'], [1])
porter = profession.Profession('Porter', 0, ['Expert'], [1])
prostitute = profession.Profession('Prostitute', 0, ['Expert'], [1])
raker = profession.Profession('Raker', 0, ['Expert'], [1])
cook = profession.Profession('Cook', 0.4, ['Expert'], [1])
tenter = profession.Profession('Tenter', 0, ['Expert'], [1])
water_carrier = profession.Profession('Water Carrier', 0, ['Expert'], [1])
# Other
adventurer = profession.Profession('Adventurer', 0.1, [])
beggar = profession.Profession('Beggar', 0, ['Expert'], [1])
hermit = profession.Profession('Hermit', 0, ['Expert', 'Druid', 'Monk', 'Sorcerer', 'Warlock', 'Wizard'], [1, 1, 1, 1, 1, 1])
savage = profession.Profession('Savage', 0, ['Warrior', 'Barbarian', 'Druid', 'Sorcerer'], [10, 4, 1, 1])
same = profession.Profession('Same', 0, ['Error'], [1])

professions = [catchpole, chancellor, diplomat, exchequer, forester, hayward, herald, judge, knight, liner, local_lord, noble, summoner, bowman, engineer, footman, mercenary, pikeman, sapper, scout, sergeant, general, bailiff, constable, guard, guard_captain, jailer, sheriff, burglar, con_artist, fence, footpad, pickpocket, poacher, archbishop, bishop, cardinal, monk, priest, apothecary, banker, innkeeper, merchant_book, merchant_cloth, merchant_food, merchant_fuel, merchant_jewelry, merchant_magic, merchant_skin, merchant_spice, merchant_stone, merchant_textile, merchant_wood, acrobat, actor, musician, painter, sculptor, writer, farmer, fisherman, herder, hunter, alchemist, astronomer, historian, librarian, mathematician, mage, philosopher, professor, theologian, navigator, sailor, captain, sailmaker, shipwright, shoemaker, furrier, tailor, jeweler, pastrycook, mason, carpenter, weaver, chandler, cooper, baker, hatmaker, saddler, chicken_butcher, pursemaker, butcher, buckle_maker, plasterer, blacksmith, painter_craft, roofer, locksmith, ropemaker, tanner, harness_maker, bleacher, cutler, glovemaker, woodcarver, accoutrement_maker, arkwright, armorer, balancemaker, basketmaker, brewer, bellmaker, bottelier, bowyer, brickmaker, broom_maker, canvasser, card_maker, cartographer, cartwright, chainmaker, cheesemaker, clockmaker, dyer, embroiderer, feltmaker, fletcher, foundryman, girdler, glassblower, horner, illuminator, lampwright, luthier, minter, mirrorer, nedeller, parchmenter, rectifier, reedmaker, rugweaver, spectaclemaker, stonecutter, tapicer, vintner, wheelwright, advocate, architect, assistant, barber, bather, builder, carter, copyist, dentist, doctor, falconer, fewterer, ferryman, gardner, gravedigger, horse_groomer, launderer, link_boy, maid, messanger, miner, miller, midwife, porter, prostitute, raker, cook, tenter, water_carrier, adventurer, beggar, hermit, savage, same]


# --------- profession distribution by role and building ----------
# Profession structures
# Role:" ", Quantity: Distribution_type, (Par1,Par2), Profession: [A,B,C], Weight:[1,2,3]
# Supportedd Quantity are ['One', Odds], ['Flat',(Min,Max)] and ['Normal',(Mean, Standard_Deviation)]
# 'same' is a special profession, gives the character the same profession as the Master


# House
farmer_house_master = rp.RoleProfessions('Master', 'One', 1, [farmer, fisherman, herder, hunter], [20,20,1,1])
farmer_house_spouse = rp.RoleProfessions('Spouse', 'One', 0.9, [same, farmer, fisherman, herder, hunter], [50, 20,20,1,1])
farmer_house_child = rp.RoleProfessions('Child', 'Normal', (4,1), [same, farmer, fisherman, herder, hunter], [50, 20,20,1,1])
commoner_house_master = rp.RoleProfessions('Master', 'One', 1, [guard, barber, builder, carter, ferryman, gardner, gravedigger, launderer, link_boy, maid, messanger, miner, midwife, porter, raker, tenter, water_carrier], [10,10,5,1,1,1,1,4,1,15,2,25,2,1,1,10,3])
commoner_house_spouse = rp.RoleProfessions('Spouse', 'One', 0.9, [same, guard, barber, builder, carter, ferryman, gardner, gravedigger, launderer, link_boy, maid, messanger, miner, midwife, porter, raker, tenter, water_carrier], [100,10,10,5,1,1,1,1,4,1,15,2,25,2,1,1,10,3])
bourgeois_house_master = rp.RoleProfessions('Master', 'One', 1, [advocate, architect, bather, dentist, doctor, falconer, fewterer, horse_groomer, miller], [1,1,3,3,3,1,1,2,3])
bourgeois_house_spouse = rp.RoleProfessions('Spouse', 'One', 0.9, [same, advocate, architect, bather, dentist, doctor, falconer, fewterer, horse_groomer, miller], [30,1,1,3,3,3,1,1,2,3])
noble_house_master = rp.RoleProfessions('Master', 'One', 1, [diplomat, noble], [1,50])

# Service
tavern_master = rp.RoleProfessions('Master', 'One', 1, [brewer, cook], [1,1])
inn_master = rp.RoleProfessions('Master', 'One', 1, [innkeeper], [1])
hospital_master = rp.RoleProfessions('Master', 'One', 1, [doctor], [1])
hospital_apprentice = rp.RoleProfessions('Apprentice', 'Normal', (0,2), [doctor], [1])
whorehouse_master = rp.RoleProfessions('Master', 'One', 1, [prostitute], [1])
whorehouse_servant = rp.RoleProfessions('Servant', 'Normal', (5,2), [prostitute], [1])
bank_master = rp.RoleProfessions('Master', 'One', 1, [banker], [1])

# Store
general_master = rp.RoleProfessions('Master', 'One', 1, [merchant_cloth, merchant_fuel, merchant_skin, merchant_stone, merchant_textile, merchant_wood], [5,3,3,1,2,2])
food_master = rp.RoleProfessions('Master', 'One', 1, [merchant_food, pastrycook, baker, chicken_butcher, butcher, brewer, cheesemaker, rectifier, vintner], [10,3,4,2,1,3,1,1,2])
health_master = rp.RoleProfessions('Master', 'One', 1, [apothecary, alchemist], [10,1])
book_master = rp.RoleProfessions('Master', 'One', 1, [merchant_book, illuminator], [10,1])
magic_master = rp.RoleProfessions('Master', 'One', 1, [merchant_magic, mage], [10,1])
luxury_master = rp.RoleProfessions('Master', 'One', 1, [merchant_jewelry, merchant_spice], [1,1])

# Workshop
blacksmith_master = rp.RoleProfessions('Master', 'One', 1, [blacksmith, buckle_maker, locksmith, cutler, armorer, bellmaker, brickmaker, chainmaker, foundryman, nedeller], [5,3,3,1,1,1,3,2,5,2])
tailor_master = rp.RoleProfessions('Master', 'One', 1, [tailor, weaver, hatmaker, pursemaker, ropemaker, bleacher, glovemaker, basketmaker, embroiderer, feltmaker, rugweaver, tapicer], [10,5,2,2,1,1,1,1,1,1,1,1])
leatherwork_master = rp.RoleProfessions('Master', 'One', 1, [shoemaker, furrier, saddler, tanner, harness_maker, bottelier, girdler], [8,6,2,1,1,1,1])
woodwork_master = rp.RoleProfessions('Master', 'One', 1, [cooper, woodcarver, arkwright, bowyer, broom_maker, cartwright, fletcher, wheelwright], [3,2,1,1,1,2,2,3])
builder_master = rp.RoleProfessions('Master', 'One', 1, [mason, carpenter, plasterer, painter_craft, roofer, stonecutter], [3,3,2,2,3,1])
other_craft_master = rp.RoleProfessions('Master', 'One', 1, [jeweler, chandler, accoutrement_maker, balancemaker, canvasser, card_maker, cartographer, clockmaker, glassblower, horner, lampwright, luthier, minter, mirrorer, parchmenter, reedmaker, spectaclemaker], [10,5,2,1,1,2,1,1,4,1,5,1,1,2,5,1,1])

# Stronghold
stronghold_master = rp.RoleProfessions('Master', 'One', 1, [local_lord], [1])
stronghold_spouse = rp.RoleProfessions('Spouse', 'One', 0.9, [noble], [1])
stronghold_child = rp.RoleProfessions('Child', 'Normal', (3,1), [noble, knight], [1,1])
keep_servant = rp.RoleProfessions('Servant', 'Normal', (3,1), [maid, gardner, messanger, porter, cook], [15,2,3,2,1])
keep_security = rp.RoleProfessions('Security', 'Normal', (4,1), [guard, guard_captain], [15,1])
keep_apprentice = rp.RoleProfessions('Apprentice', 'Normal', (1,1), [noble, knight], [1,1])
keep_unique = rp.RoleProfessions('Unique', 'Normal', (2,1), [constable, chancellor, exchequer, forester], [2,2,1,2])
keep_visitor = rp.RoleProfessions('Visitor', 'Normal', (0,1), [diplomat], [1])
castle_servant = rp.RoleProfessions('Servant', 'Normal', (12,2), [maid, gardner, messanger, porter, cook], [15,2,3,2,1])
castle_security = rp.RoleProfessions('Security', 'Normal', (15,2), [guard, guard_captain], [15,1])
castle_apprentice = rp.RoleProfessions('Apprentice', 'Normal', (2,1), [noble, knight], [1,1])
castle_unique = rp.RoleProfessions('Unique', 'Normal', (12,2), [bailiff, catchpole, constable, chancellor, exchequer, forester, hayward, herald, judge, liner, summoner], [5,1,20,20,15,15,5,10,5,1,5])
castle_visitor = rp.RoleProfessions('Visitor', 'Normal', (5,1), [diplomat, noble, knight], [1,1,1])

# Religious
shrine_master = rp.RoleProfessions('Master', 'One', 1, [priest], [1])
monastery_master = rp.RoleProfessions('Master', 'One', 1, [monk], [1])
monastery_apprentice = rp.RoleProfessions('Apprentice', 'Normal', (5,2), [monk], [1])
church_master = rp.RoleProfessions('Master', 'One', 1, [priest, bishop], [5,1])
cathedral_master = rp.RoleProfessions('Master', 'One', 1, [bishop, archbishop, cardinal], [10,4,1])

# Education
school_master = rp.RoleProfessions('Master', 'One', 1, [professor], [1])
school_teachers = rp.RoleProfessions('Apprentice', 'Normal', (3,1), [professor], [1])
university_master = rp.RoleProfessions('Master', 'One', 1, [alchemist, astronomer, historian, mathematician, mage, philosopher, theologian], [3,3,3,1,5,3,3])
university_professors = rp.RoleProfessions('Apprentice', 'Normal', (10,2), [alchemist, astronomer, historian, mathematician, mage, philosopher, theologian], [3,3,3,1,5,3,3])
university_servant = rp.RoleProfessions('Servant', 'Normal', (6,1), [maid, librarian, copyist], [2,1,1])

# Military
prison_master = rp.RoleProfessions('Master', 'One', 1, [jailer], [1])
prison_jailers = rp.RoleProfessions('Apprentice', 'Normal', (3,1), [jailer], [1])
barrack_master = rp.RoleProfessions('Master', 'One', 1, [sergeant], [1])
barrack_soldier = rp.RoleProfessions('Apprentice', 'Normal', (10,3), [bowman, footman, pikeman, scout], [2,5,2,1])
fortress_master = rp.RoleProfessions('Master', 'One', 1, [general], [1])
fortress_soldier = rp.RoleProfessions('Apprentice', 'Normal', (100,20), [bowman, engineer, footman, pikeman, sapper, sergeant, scout], [5,1,10,5,1,3,3])
fortress_craftsman = rp.RoleProfessions('Servant', 'Normal', (5,2), [accoutrement_maker, armorer, fletcher, bowyer], [3,3,4,2])
fortress_servant = rp.RoleProfessions('Servant', 'Normal', (5,2), [maid, cook, porter], [4,3,2])

# Criminal
den_master = rp.RoleProfessions('Master', 'One', 1, [burglar, con_artist, fence, footpad, pickpocket], [1,1,1,1,1])
den_criminals = rp.RoleProfessions('Apprentice', 'Normal', (10,3), [burglar, con_artist, fence, footpad, pickpocket], [1,1,1,1,1])
front_master = rp.RoleProfessions('Master', 'One', 1, [fence], [1])
camp_master = rp.RoleProfessions('Master', 'One', 1, [footpad], [1])
camp_criminals = rp.RoleProfessions('Apprentice', 'Normal', (10,3), [footpad], [1])

# Art
artist_master = rp.RoleProfessions('Master', 'One', 1, [acrobat, actor, musician, painter, sculptor, writer], [1,1,1,1,1,1])
artist_members = rp.RoleProfessions('Apprentice', 'Normal', (10,3), [acrobat, actor, musician, painter, sculptor, writer], [1,1,1,1,1,1])
circus_master = rp.RoleProfessions('Master', 'One', 1, [acrobat, actor, musician], [1,1,1])
circus_member = rp.RoleProfessions('Apprentice', 'Normal', (5,2), [acrobat, actor, musician], [1,1,1])
museum_master = rp.RoleProfessions('Master', 'One', 1, [historian], [1])
museum_apprentice = rp.RoleProfessions('Apprentice', 'Normal', (2,1), [historian], [1])

# Other
homeless_master = rp.RoleProfessions('Master', 'One', 1, [beggar], [1])
ship_master = rp.RoleProfessions('Master', 'One', 1, [captain], [1])
ship_navigator = rp.RoleProfessions('Unique', 'One', 0.5, [navigator], [1])
ship_sailor = rp.RoleProfessions('Servant', 'Normal', (12,3), [sailor], [1])

# Reusable
spouse_same = rp.RoleProfessions('Spouse', 'One', 0.9, [same], [1])
spouse_assistant = rp.RoleProfessions('Spouse', 'One', 0.9, [same, assistant], [1,10])
child_same = rp.RoleProfessions('Child', 'Normal', (3,1), [same], [1])
child_commoner = rp.RoleProfessions('Child', 'Normal', (4,1), [same, assistant, guard, barber, builder, carter, ferryman, gardner, gravedigger, launderer, link_boy, maid, messanger, miner, midwife, porter, raker, tenter, water_carrier], [50,20,10,10,5,1,1,1,1,4,1,15,2,25,2,1,1,10,3])
child_bourgeois = rp.RoleProfessions('Child', 'Normal', (3,1), [same, assistant, advocate, architect, bather, dentist, doctor, falconer, fewterer, horse_groomer, miller], [15,10,1,1,3,3,3,1,1,2,3])
child_craftsman = rp.RoleProfessions('Child', 'Normal', (3,1), [same, assistant], [1,2])
apprentice_craftsman = rp.RoleProfessions('Apprentice', 'Normal', (1,1), [same], [1])
assistant_0 = rp.RoleProfessions('Servant', 'Normal', (0,1), [assistant], [1])
assistant_1 = rp.RoleProfessions('Servant', 'Normal', (1,1), [assistant], [1])
assistant_2 = rp.RoleProfessions('Servant', 'Normal', (2,1), [assistant], [1])
assistant_3 = rp.RoleProfessions('Servant', 'Normal', (3,1), [assistant], [1])
guard_0 = rp.RoleProfessions('Security', 'Normal', (0,1), [guard], [1])
guard_1 = rp.RoleProfessions('Security', 'Normal', (1,1), [guard], [1])
guard_2 = rp.RoleProfessions('Security', 'Normal', (2,1), [guard], [1])
guard_3 = rp.RoleProfessions('Security', 'Normal', (3,1), [guard], [1])
maid_0 = rp.RoleProfessions('Servant', 'Normal', (0,1), [maid], [1])
maid_1 = rp.RoleProfessions('Servant', 'Normal', (1,1), [maid], [1])
maid_2 = rp.RoleProfessions('Servant', 'Normal', (2,1), [maid], [1])
maid_3 = rp.RoleProfessions('Servant', 'Normal', (3,1), [maid], [1])
priest_0 = rp.RoleProfessions('Apprentice', 'Normal', (0,1), [priest], [1])
priest_1 = rp.RoleProfessions('Apprentice', 'Normal', (1,1), [priest], [1])
priest_2 = rp.RoleProfessions('Apprentice', 'Normal', (2,1), [priest], [1])
priest_3 = rp.RoleProfessions('Apprentice', 'Normal', (3,1), [priest], [1])
tenter_0 = rp.RoleProfessions('Servant', 'Normal', (0,1), [tenter], [1])
tenter_1 = rp.RoleProfessions('Servant', 'Normal', (1,1), [tenter], [1])
tenter_2 = rp.RoleProfessions('Servant', 'Normal', (2,1), [tenter], [1])
tenter_3 = rp.RoleProfessions('Servant', 'Normal', (3,1), [tenter], [1])

# Separation like this is not necessary, only profession_list is required
profession_governance = ['Catchpole','Chancellor','Diplomat','Exchequer','Forester','Hayward','Herald','Judge','Knight',
                         'Liner', 'Local Lord', 'Nobleman(woman)','Summoner']
profession_military = ['Bowman','Engineer','Footman','Mercenary','Pikeman','Sapper','Scout','Sergeant','General']
profession_security = ['Bailiff','Constable','Guardsman','Jailer','Sherrif']
profession_criminal = ['Burglar','Con Artist','Fence','Footpad','Pickpocket','Poacher']
profession_religious = ['Archbishop','Bishop','Cardinal','Monk','Priest']
profession_merchant = ['Apothecary','Banker','Merchant (Beverage)','Merchant (Book)','Merchant (Cloth)','Merchant (Food)',
                       'Merchant (Fuel)', 'Innkeeper','Merchant (Jewelry)', 'Merchant (Magic)', 'Merchant (Skin)',
                       'Merchant (Spice)','Merchant (Stone and Ore)','Merchant (Textile)','Merchant (Wood)']
profession_entertainer = ['Acrobat','Actor','Musician','Painter (Art)','Sculptor','Singer','Writer']
profession_food_provider = ['Farmer','Fisherman','Herder','Hunter']
profession_scholar = ['Alchemist','Astronomer','Librarian','Mathematician','Mage','Philosopher','Professor','Theologian']
profession_sailor = ['Navigator','Sailor','Captain','Sailmaker','Shipwright']
profession_craftsman = ['Shoemaker','Furrier','Tailor','Jeweler','Pastrycook','Mason','Carpenter','Weaver','Chandler','Cooper (Barrel-maker)',
                        'Baker','Hatmaker','Saddler','Chicken Butcher','Pursemaker','Butcher','Buckler-maker','Plasterer','Blacksmith','Painter',
                        'Roofer','Locksmith','Ropemaker','Tanner','Rugmaker','Harness-Maker','Bleacher','Cutler','Glovemaker','Woodcarver',
                        'Accoutrement maker','Arkwright','Armorer','Balancemaker','Basketmaker','Brewer','Bellmaker', 'Bottelier','Bowyer','Brickmaker',
                        'Broom maker','Canvasser','Card maker','Cartographer','Cartwright','Chainmaker','Cheesemaker','Clockmaker','Dyer','Embroiderer',
                        'Feltmaker','Fletcher','Foundryman','Girdler','Glassblower','Horner,','Illuminator',
                        'Lampwright','Luthier','Minter','Mirrorer','Nedeller','Parchmenter','Rectifier','Reedmaker','Rugweaver',
                        'Spectaclemaker','Stonecutter','Tapicer','Vintner','Wheelwright']
profession_service = ['Advocate','Architect', 'Barber','Bather','Builder','Carter','Copyist','Dentist','Doctor','Falconer',
                      'Fewterer (Keeper of dogs)','Ferryman','Gardner','Gravedigger','Horse groomer','Launderer','Link boy (Torch carrier)','Maid','Messanger','Miner',
                      'Miller','Porter','Prostitute','Raker','Cook','Tenter','Water Carrier']
profession_other = ['Adventurer','Beggar','Hermit','Savage']
profession_dict = {'Governance':profession_governance,'Military':profession_military,'Security':profession_security,
                   'Criminal':profession_criminal,'Religious':profession_religious,
                   'Merchant':profession_merchant,'Entertainer':profession_entertainer,'Food Provider':profession_food_provider,'Scholar':profession_scholar,'Sailor':profession_sailor,
                   'Craftsman':profession_craftsman,'Service':profession_service,'Other':profession_other}
profession_list = profession_governance + profession_military + profession_security + profession_criminal + \
                  profession_religious + profession_merchant + profession_entertainer + profession_scholar + \
                  profession_sailor + profession_craftsman + profession_service + profession_other


