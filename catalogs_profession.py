import profession
import role_professions as rp

# Governance
catchpole = profession.Profession('Catchpole', 1.2, [])
chancellor = profession.Profession('Chancellor', 1.9, ['Expert', 'Wizard'], [100,1])
diplomat = profession.Profession('Diplomat', 1.7, ['Expert'], [1])
exchequer = profession.Profession('Exchequer', 1.9, ['Expert'], [1])
forester = profession.Profession('Forester', 1.6, ['Expert', 'Ranger'], [10,1], 'Forests')
hayward = profession.Profession('Hayward', 1.6, ['Expert'], [1])
herald = profession.Profession('Herald', 1.1, [])
judge = profession.Profession('Judge', 2, [])
knight = profession.Profession('Knight', 1.8, ['Fighter', 'Paladin'], [50,1])
liner = profession.Profession('Liner', 1.5, [])
local_lord = profession.Profession('Local Lord', 2, ['Expert', 'Bard', 'Fighter'], [10,1,3])
noble = profession.Profession('Noble', 2, ['Expert'], [1])
summoner = profession.Profession('Summoner', 1.1, [])
# Military
bowman = profession.Profession('Bowman', 0.3, [])
engineer = profession.Profession('Engineer', 0.9, [])
footman = profession.Profession('Footman', 0.2, [])
mercenary = profession.Profession('Mercenary', 0.3, [])
pikeman = profession.Profession('Pikeman', 0.3, [])
sapper = profession.Profession('Sapper', 0.4, [])
scout = profession.Profession('Scout', 0.2, [])
sergeant = profession.Profession('Sergeant', 0.7, [])
general = profession.Profession('General', 1.5, [])
# Security
bailiff = profession.Profession('Bailiff', 1.5, [])
constable = profession.Profession('Constable', 1.5, [])
guard = profession.Profession('Guard', 0.2, ['Warrior', 'Fighter'], [10,1])
jailer = profession.Profession('Jailer', 0.1, [])
sheriff = profession.Profession('Sheriff', 0.9, [])
# Criminal
burglar = profession.Profession('Burglar', 0.05, [])
con_artist = profession.Profession('Con Artist', 0.2, [])
fence = profession.Profession('Fence', 0.4, [])
footpad = profession.Profession('Footpad', 0.05, [])
pickpocket = profession.Profession('Pickpocket', 0, [])
poacher = profession.Profession('Poacher', 0, [], 'Forests')
# Religious
archbishop = profession.Profession('Archbishop', 1.9, [])
bishop = profession.Profession('Bishop', 1.8, [])
cardinal = profession.Profession('Cardinal', 2, [])
monk = profession.Profession('Monk', 0, [])
priest = profession.Profession('Priest', 0.4, [])
# Merchant
apothecary = profession.Profession('Apothecary', 1, [])
banker = profession.Profession('Banker', 2, [])
innkeeper = profession.Profession('Innkeeper', 0.7, [])
merchant_book = profession.Profession('Book Merchant', 1.1, [])
merchant_cloth = profession.Profession('Cloth Merchant', 0.1, [])
merchant_food = profession.Profession('Food Merchant', 0.1, [])
merchant_fuel = profession.Profession('Fuel Merchant', 0.1, [])
merchant_jewelry = profession.Profession('Jewelry Merchant', 1.2, [])
merchant_magic = profession.Profession('Magic Merchant', 1.2, [])
merchant_skin = profession.Profession('Skin Merchant', 0.1, [])
merchant_spice = profession.Profession('Spice Merchant', 1, [])
merchant_stone = profession.Profession('Stone Merchant', 0.1, [])
merchant_textile = profession.Profession('Textile Merchant', 0.1, [])
merchant_wood = profession.Profession('Wood Merchant', 0.1, [])
# Entertainer
acrobat = profession.Profession('Acrobat', 0, [])
actor = profession.Profession('Actor', 0.1, [])
musician = profession.Profession('Musician', 0.1, [])
painter = profession.Profession('Painter', 0.1, [])
sculptor = profession.Profession('Sculptor', 0.1, [])
writer = profession.Profession('Writer', 0.1, [])
# Food provider
farmer = profession.Profession('Farmer', 0, ['Expert'], [1])
fisherman = profession.Profession('Fisherman', 0, ['Expert'], [1], 'Water')
herder = profession.Profession('Herder', 0.2, ['Expert'], [1], 'Plains')
hunter = profession.Profession('Hunter', 0, ['Expert'], [1])
# Scholar
alchemist = profession.Profession('Alchemist', 0.5, [])
astronomer = profession.Profession('Astronomer', 1.1, [], 'Mountains')
librarian = profession.Profession('Librarian', 0, [])
mathematician = profession.Profession('Mathematician', 0.5, [])
mage = profession.Profession('Mage', 1.1, [])
philosopher = profession.Profession('Philosopher', 0.5, [])
professor = profession.Profession('Professor', 0.5, [])
theologian = profession.Profession('Theologian', 0.5, [])
# Sailor
navigator = profession.Profession('Navigator', 0.5, [], 'Sea')
sailor = profession.Profession('Sailor', 0, [], 'Sea')
captain = profession.Profession('Captain', 0.8, [], 'Sea')
sailmaker = profession.Profession('Sailmaker', 0.1, [], 'Water')
shipwright = profession.Profession('Shipwright', 0.4, [], 'Water')
# Craftsman
shoemaker = profession.Profession('Shoemaker', 0.01, [])
furrier = profession.Profession('Furrier', 0.01, [])
tailor = profession.Profession('Tailor', 0.01, [])
jeweler = profession.Profession('Jeweler', 0.9, [])
pastrycook = profession.Profession('Pastrycook', 0, [])
mason = profession.Profession('Mason', 0.01, [])
carpenter = profession.Profession('Carpenter', 0.01, [])
weaver = profession.Profession('Weaver', 0, [])
chandler = profession.Profession('Chandler', 0.01, [])
cooper = profession.Profession('Cooper', 0, [])
baker = profession.Profession('Baker', 0, [])
hatmaker = profession.Profession('Hatmaker', 0.01, [])
saddler = profession.Profession('Saddler', 0.01, [])
chicken_butcher = profession.Profession('Chicken Butcher', 0, [])
pursemaker = profession.Profession('Pursemaker', 0, [])
butcher = profession.Profession('Butcher', 0.01, [])
buckle_maker = profession.Profession('Buckle-maker', 0, [])
plasterer = profession.Profession('Plasterer', 0, [])
blacksmith = profession.Profession('Blacksmith', 0.01, [])
painter_craft = profession.Profession('Painter (Building)', 0, [])
roofer = profession.Profession('Roofer', 0, [])
locksmith = profession.Profession('Locksmith', 0.01, [])
ropemaker = profession.Profession('Ropemaker', 0, [])
tanner = profession.Profession('Tanner', 0, [])
rugmaker = profession.Profession('Rugmaker', 0.01, [])
harness_maker = profession.Profession('Harness-Maker', 0, [])
bleacher = profession.Profession('Bleacher', 0, [])
cutler = profession.Profession('Cutler', 0.01, [])
glovemaker = profession.Profession('Glovemaker', 0.01, [])
woodcarver = profession.Profession('Woodcarver', 0.01, [])
accoutrement_maker = profession.Profession('Accoutrement Maker', 0.01, [])
arkwright = profession.Profession('Arkwright', 0.01, [])
armorer = profession.Profession('Armorer', 0.05, [])
balancemaker = profession.Profession('Balancemaker', 0.05, [])
basketmaker = profession.Profession('Basketmaker', 0, [])
brewer = profession.Profession('Brewer', 0.01, [])
bellmaker = profession.Profession('Bellmaker', 0.01, [])
bottelier = profession.Profession('Bottelier', 0, [])
bowyer = profession.Profession('Bowyer', 0.05, [])
brickmaker = profession.Profession('Brickmaker', 0, [])
broom_maker = profession.Profession('Broom Maker', 0, [])
canvasser = profession.Profession('Canvasser', 0, [])
card_maker = profession.Profession('Card Maker', 0.01, [])
cartographer = profession.Profession('Cartographer', 0.3, [])
cartwright = profession.Profession('Cartwright', 0.01, [])
chainmaker = profession.Profession('Chainmaker', 0, [])
cheesemaker = profession.Profession('Cheesemaker', 0.01, [])
clockmaker = profession.Profession('Clockmaker', 0.05, [])
dyer = profession.Profession('Dyer', 0, [])
embroiderer = profession.Profession('Embroiderer', 0.01, [])
feltmaker = profession.Profession('Feltmaker', 0, [])
fletcher = profession.Profession('Fletcher', 0.01, [])
foundryman = profession.Profession('Foundryman', 0, [])
girdler = profession.Profession('Girdler', 0, [])
glassblower = profession.Profession('Glassblower', 0.01, [])
horner = profession.Profession('Horner', 0.01, [])
illuminator = profession.Profession('Illuminator', 0.05, [])
lampwright = profession.Profession('Lampwright', 0.01, [])
luthier = profession.Profession('Luthier', 0.01, [])
minter = profession.Profession('Minter', 1.5, [])
mirrorer = profession.Profession('Mirrorer', 0.01, [])
nedeller = profession.Profession('Nedeller', 0, [])
parchmenter = profession.Profession('Parchmenter', 0, [])
rectifier = profession.Profession('Rectifier', 0.01, [])
reedmaker = profession.Profession('Reedmaker', 0.01, [])
rugweaver = profession.Profession('Rugweaver', 0.01, [])
spectaclemaker = profession.Profession('Spectaclemaker', 0.01, [])
stonecutter = profession.Profession('Stonecutter', 0.01, [])
tapicer = profession.Profession('Tapicer', 0.01, [])
vintner = profession.Profession('Vintner', 0.01, [])
wheelwright = profession.Profession('Wheelwright', 0, [])
# Service
advocate = profession.Profession('Advocate', 0.9, [])
architect = profession.Profession('Architect', 0.9, [])
barber = profession.Profession('Barber', 0, ['Expert'], [1])
bather = profession.Profession('Bather', 0, [])
builder = profession.Profession('Builder', 0, [])
carter = profession.Profession('Carter', 0, [])
copyist = profession.Profession('Copyist', 0, [])
dentist = profession.Profession('Dentist', 0.5, [])
doctor = profession.Profession('Doctor', 0.6, [])
falconer = profession.Profession('Falconer', 0.9, [])
fewterer = profession.Profession('Fewterer', 0.8, [])
ferryman = profession.Profession('Ferryman', 0, [], 'River')
gardner = profession.Profession('Gardner', 0.01, [])
gravedigger = profession.Profession('Gravedigger', 0, [])
horse_groomer = profession.Profession('Horse Groomer', 0.3, [], 'Plains')
launderer = profession.Profession('Launderer', 0, [])
link_boy = profession.Profession('Link Boy', 0, [])
maid = profession.Profession('Maid', 0, ['Expert'], [1])
messanger = profession.Profession('Messanger', 0, [])
miner = profession.Profession('Miner', 0, [], 'Mines')
miller = profession.Profession('Miller', 0.2, [])
midwife = profession.Profession('Midwife', 0, [])
porter = profession.Profession('Porter', 0, [])
prostitute = profession.Profession('Prostitute', 0, [])
raker = profession.Profession('Raker', 0, [])
restaurateur = profession.Profession('Restaurateur', 0.4, [])
tenter = profession.Profession('Tenter', 0, [])
water_carrier = profession.Profession('Water Carrier', 0, [])
# Other
adventurer = profession.Profession('Adventurer', 0.1, [])
beggar = profession.Profession('Beggar', 0, [])
hermit = profession.Profession('Hermit', 0, [])
savage = profession.Profession('Savage', 0, [])
same = profession.Profession('Same', 0, [])

professions = [catchpole, chancellor, diplomat, exchequer, forester, hayward, herald, judge, knight, liner, local_lord, noble, summoner, bowman, engineer, footman, mercenary, pikeman, sapper, scout, sergeant, general, bailiff, constable, guard, jailer, sheriff, burglar, con_artist, fence, footpad, pickpocket, poacher, archbishop, bishop, cardinal, monk, priest, apothecary, banker, innkeeper, merchant_book, merchant_cloth, merchant_food, merchant_fuel, merchant_jewelry, merchant_magic, merchant_skin, merchant_spice, merchant_stone, merchant_textile, merchant_wood, acrobat, actor, musician, painter, sculptor, writer, farmer, fisherman, herder, hunter, alchemist, astronomer, librarian, mathematician, mage, philosopher, professor, theologian, navigator, sailor, captain, sailmaker, shipwright, shoemaker, furrier, tailor, jeweler, pastrycook, mason, carpenter, weaver, chandler, cooper, baker, hatmaker, saddler, chicken_butcher, pursemaker, butcher, buckle_maker, plasterer, blacksmith, painter_craft, roofer, locksmith, ropemaker, tanner, rugmaker, harness_maker, bleacher, cutler, glovemaker, woodcarver, accoutrement_maker, arkwright, armorer, balancemaker, basketmaker, brewer, bellmaker, bottelier, bowyer, brickmaker, broom_maker, canvasser, card_maker, cartographer, cartwright, chainmaker, cheesemaker, clockmaker, dyer, embroiderer, feltmaker, fletcher, foundryman, girdler, glassblower, horner, illuminator, lampwright, luthier, minter, mirrorer, nedeller, parchmenter, rectifier, reedmaker, rugweaver, spectaclemaker, stonecutter, tapicer, vintner, wheelwright, advocate, architect, barber, bather, builder, carter, copyist, dentist, doctor, falconer, fewterer, ferryman, gardner, gravedigger, horse_groomer, launderer, link_boy, maid, messanger, miner, miller, midwife, porter, prostitute, raker, restaurateur, tenter, water_carrier, adventurer, beggar, hermit, savage, same]


# --------- profession distribution by role and building ----------

# Houses
farmer_house_master = rp.RoleProfessions('Master', 'One', 1, [farmer, fisherman, herder, hunter], [20,20,1,1])
farmer_house_spouse = rp.RoleProfessions('Spouse', 'One', 0.9, [same, farmer, fisherman, herder, hunter], [50, 20,20,1,1])
farmer_house_child = rp.RoleProfessions('Child', 'Normal', (3,1), [same, farmer, fisherman, herder, hunter], [50, 20,20,1,1])
commoner_house_master = rp.RoleProfessions('Master', 'One', 1, [barber], [1])
commoner_house_spouse = rp.RoleProfessions('Spouse', 'One', 0.9, [barber], [1])
commoner_house_child = rp.RoleProfessions('Child', 'Normal', (3,1), [guard, maid], [1,1])

# Stronghold
stronghold_master = rp.RoleProfessions('Master', 'One', 1, [local_lord], [1])
stronghold_spouse = rp.RoleProfessions('Spouse', 'One', 0.9, [noble], [1])
stronghold_child = rp.RoleProfessions('Child', 'Normal', (3,1), [noble, knight], [1,1])
keep_servant = rp.RoleProfessions('Servant', 'Normal', (2,1), [maid], [1])
keep_security = rp.RoleProfessions('Security', 'Normal', (3,1), [guard], [1])
keep_apprentice = rp.RoleProfessions('Apprentice', 'Normal', (1,1), [knight], [1])
keep_unique = rp.RoleProfessions('Unique', 'Normal', (1,1), [chancellor, exchequer, forester, hayward], [5,3,5,2])
keep_visitor = rp.RoleProfessions('Visitor', 'Normal', (0,1), [diplomat], [1])




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
                      'Miller','Porter','Prostitute','Raker','Restaurateur','Tenter','Water Carrier']
profession_other = ['Adventurer','Beggar','Hermit','Savage']
profession_dict = {'Governance':profession_governance,'Military':profession_military,'Security':profession_security,
                   'Criminal':profession_criminal,'Religious':profession_religious,
                   'Merchant':profession_merchant,'Entertainer':profession_entertainer,'Food Provider':profession_food_provider,'Scholar':profession_scholar,'Sailor':profession_sailor,
                   'Craftsman':profession_craftsman,'Service':profession_service,'Other':profession_other}
profession_list = profession_governance + profession_military + profession_security + profession_criminal + \
                  profession_religious + profession_merchant + profession_entertainer + profession_scholar + \
                  profession_sailor + profession_craftsman + profession_service + profession_other

# Profession structures
#[ {Role:" ", Quantity:['Formula, (Par1,Par2)], Profession: [A,B,C], Weight:[1,2,3], 'Geography':[None,'Plains',
# 'Sea'] }, { ... } ]
# Supportedd Quantity are ['One', Odds], ['Flat',(Min,Max)] and ['Normal',(Mean, Standard_Deviation)]
# 'Same' is a special profession, gives the character the same profession as the Master
# Geography is used to specify a required geographical feature. Support: [Plains, Forests, River, Sea, Mountains,
# Mines and Water (River or Sea)]

profession = {'House': {'Farmer':
                            [{'Role': 'Master', 'Quantity': ['One', 1], 'Profession': ['Farmer','Fisherman','Herder','Hunter'],
                              'Weight': [20,20,1,1], 'Geography': [None,'Water','Plains',None]},
                             {'Role': 'Spouse', 'Quantity': ('One', 0.9), 'Profession': ['Same','Farmer','Fisherman','Herder','Hunter'],
                              'Weight': [50,20,10,1,1], 'Geography': [None,None,'Water','Plains',None]},
                             {'Role': 'Child', 'Quantity': ('Normal', (3,1)), 'Profession': ['Same','Farmer','Fisherman','Herder','Hunter'],
                              'Weight': [50,20,10,1,1], 'Geography': [None,None,'Water','Plains',None]}
                             ],
                        'Commoner':
                            [{'Role': 'Master', 'Quantity': ('One', 1), 'Profession': ['Barber'], 'Weight': [1],
                              'Geography': [None]},
                             {'Role': 'Spouse', 'Quantity': ('One', 0.9), 'Profession': ['Same'], 'Weight': [1],
                              'Geography': [None]},
                             {'Role': 'Child', 'Quantity': ('Normal', (3,1)), 'Profession': ['Guardsman','Maid'],
                              'Weight': [1,1], 'Geography': [None,None]},
                             ],
                        'Bourgeois':
                            [{'Role': 'Master', 'Quantity': (1, 1), 'Profession': [], 'Weight': [], 'Geography': []},
                             {'Role': 'Spouse', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                             {'Role': 'Child', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                             {'Role': 'Servant', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                             {'Role': 'Security', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                             {'Role': 'Apprentice', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                             {'Role': 'Unique', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                             {'Role': 'Visitor', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []}
                             ],
                        'Noble': [1,1]},
            'Service': [['Tavern',0,10],
                        ['Inn',1,5],
                        ['Hospital',1,1],
                        ['Whorehouse',1,5]],
            'Shop': [['General',0,20],
                     ['Food',0,10],
                     ['Health',1,5],
                     ['Book',1,2],
                     ['Magic',2,1],
                     ['Luxury',2,2]],
            'Workshop': [['Blacksmith',0,2],
                         ['Tailor',0,5],
                         ['Leatherwork',0,2],
                         ['Woodwork',0,4],
                         ['Other',1,1]],
            'Castle': {'Keep':
                           [{'Role': 'Master', 'Quantity': ('One', 1), 'Profession': ['Local Lord'], 'Weight': [1],
                             'Geography': [None]},
                            {'Role': 'Spouse', 'Quantity': ('One', 0.9), 'Profession': ['Nobleman(woman)'],
                             'Weight': [1], 'Geography': [None]},
                            {'Role': 'Child', 'Quantity': ('Normal', (3,1)), 'Profession': ['Nobleman(woman)'],
                             'Weight': [1], 'Geography': [None]},
                            {'Role': 'Servant', 'Quantity': ('Normal', (2,1)), 'Profession': ['Maid'], 'Weight': [1],
                             'Geography': [None]},
                            {'Role': 'Security', 'Quantity': ('Normal', (3,1)), 'Profession': ['Guardsman'],
                             'Weight': [1], 'Geography': [None]},
                            {'Role': 'Apprentice', 'Quantity': ('Normal', (1,1)), 'Profession': ['Knight'],
                             'Weight': [1], 'Geography': [None]},
                            {'Role': 'Unique', 'Quantity': ('Normal', (1,1)), 'Profession': ['Chancellor','Exchequer','Forester','Hayward'],
                             'Weight': [5,3,5,2,], 'Geography': [None,None,'Forests',None]},
                            {'Role': 'Visitor', 'Quantity': ('Normal', (0,1)), 'Profession': ['Diplomat'],
                             'Weight': [1], 'Geography': [None]}],
                       'Castle':
                           [{'Role': 'Master', 'Quantity': ('One', 1), 'Profession': [], 'Weight': [], 'Geography': []},
                            {'Role': 'Spouse', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                            {'Role': 'Child', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                            {'Role': 'Servant', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                            {'Role': 'Security', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                            {'Role': 'Apprentice', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                            {'Role': 'Unique', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []},
                            {'Role': 'Visitor', 'Quantity': (), 'Profession': [], 'Weight': [], 'Geography': []}]
                       },
            'Religious': [['Shrine',0,20],
                          ['Monastery',0,10],
                          ['Church',1,4],
                          ['Cathedral',2,1]],
            'Education': [['School',1,10],
                          ['University',2,1]],
            'Military': [['Prison',1,20],
                         ['Barrack',1,20],
                         ['Fortress',2,1],
                         ['Army',0,0]],
            'Criminal': [['Den',1,1],
                         ['Front',1,4],
                         ['Camp',0,0]],
            'Art': [['Artist Guild',1,5],
                    ['Circus',0,2],
                    ['Museum',2,1]],
            'Other': [['Homeless',0,1],
                      ['Ship',0,0]]
            }


profession_info = {'Catchpole': {'Wealth': 0, 'Class': []},
                   'Chancellor': {'Wealth': 1.8, 'Class': []},
                   'Diplomat': {'Wealth': 1.5, 'Class': []},
                   'Exchequer': {'Wealth': 1.8, 'Class': []},
                   'Forester': {'Wealth': 1.5, 'Class': []},
                   'Hayward': {'Wealth': 1.5, 'Class': []},
                   'Herald': {'Wealth': 0, 'Class': []},
                   'Judge': {'Wealth': 0, 'Class': []},
                   'Knight': {'Wealth': 1.5, 'Class': []},
                   'Liner': {'Wealth': 0, 'Class': []},
                   'Local Lord': {'Wealth': 2, 'Class': []},
                   'Nobleman(woman)': {'Wealth': 2, 'Class': []},
                   'Summoner': {'Wealth': 0, 'Class': []},
                   'Bowman': {'Wealth': 0, 'Class': []},
                   'Engineer': {'Wealth': 0, 'Class': []},
                   'Footman': {'Wealth': 0, 'Class': []},
                   'Mercenary': {'Wealth': 0, 'Class': []},
                   'Pikeman': {'Wealth': 0, 'Class': []},
                   'Sapper': {'Wealth': 0, 'Class': []},
                   'Scout': {'Wealth': 0, 'Class': []},
                   'Sergeant': {'Wealth': 0, 'Class': []},
                   'General': {'Wealth': 0, 'Class': []},
                   'Bailiff': {'Wealth': 0, 'Class': []},
                   'Constable': {'Wealth': 0, 'Class': []},
                   'Guardsman': {'Wealth': 0.5, 'Class': []},
                   'Jailer': {'Wealth': 0, 'Class': []},
                   'Sherrif': {'Wealth': 0, 'Class': []},
                   'Burglar': {'Wealth': 0, 'Class': []},
                   'Con Artist': {'Wealth': 0, 'Class': []},
                   'Fence': {'Wealth': 0, 'Class': []},
                   'Footpad': {'Wealth': 0, 'Class': []},
                   'Pickpocket': {'Wealth': 0, 'Class': []},
                   'Poacher': {'Wealth': 0, 'Class': []},
                   'Archbishop': {'Wealth': 0, 'Class': []},
                   'Bishop': {'Wealth': 0, 'Class': []},
                   'Cardinal': {'Wealth': 0, 'Class': []},
                   'Monk': {'Wealth': 0, 'Class': []},
                   'Priest': {'Wealth': 0, 'Class': []},
                   'Apothecary': {'Wealth': 0, 'Class': []},
                   'Banker': {'Wealth': 0, 'Class': []},
                   'Merchant (Beverage)': {'Wealth': 0, 'Class': []},
                   'Merchant (Book)': {'Wealth': 0, 'Class': []},
                   'Merchant (Cloth)': {'Wealth': 0, 'Class': []},
                   'Merchant (Food)': {'Wealth': 0, 'Class': []},
                   'Merchant (Fuel)': {'Wealth': 0, 'Class': []},
                   'Innkeeper': {'Wealth': 0, 'Class': []},
                   'Merchant (Jewelry)': {'Wealth': 0, 'Class': []},
                   'Merchant (Magic)': {'Wealth': 0, 'Class': []},
                   'Merchant (Skin)': {'Wealth': 0, 'Class': []},
                   'Merchant (Spice)': {'Wealth': 0, 'Class': []},
                   'Merchant (Stone and Ore)': {'Wealth': 0, 'Class': []},
                   'Merchant (Textile)': {'Wealth': 0, 'Class': []},
                   'Merchant (Wood)': {'Wealth': 0, 'Class': []},
                   'Acrobat': {'Wealth': 0, 'Class': []},
                   'Actor': {'Wealth': 0, 'Class': []},
                   'Illuminator': {'Wealth': 0, 'Class': []},
                   'Musician': {'Wealth': 0, 'Class': []},
                   'Painter (Art)': {'Wealth': 0, 'Class': []},
                   'Sculptor': {'Wealth': 0, 'Class': []},
                   'Singer': {'Wealth': 0, 'Class': []},
                   'Writer': {'Wealth': 0, 'Class': []},
                   'Farmer': {'Wealth': 0, 'Class': []},
                   'Fisherman': {'Wealth': 0, 'Class': []},
                   'Herder': {'Wealth': 0, 'Class': []},
                   'Hunter': {'Wealth': 0, 'Class': []},
                   'Alchemist': {'Wealth': 0, 'Class': []},
                   'Astronomer': {'Wealth': 0, 'Class': []},
                   'Librarian': {'Wealth': 0, 'Class': []},
                   'Mathematician': {'Wealth': 0, 'Class': []},
                   'Mage': {'Wealth': 0, 'Class': []},
                   'Philosopher': {'Wealth': 0, 'Class': []},
                   'Professor': {'Wealth': 0, 'Class': []},
                   'Theologian': {'Wealth': 0, 'Class': []},
                   'Navigator': {'Wealth': 0, 'Class': []},
                   'Sailor': {'Wealth': 0, 'Class': []},
                   'Captain': {'Wealth': 0, 'Class': []},
                   'Sailmaker': {'Wealth': 0, 'Class': []},
                   'Shipwright': {'Wealth': 0, 'Class': []},
                   'Shoemaker': {'Wealth': 0, 'Class': []},
                   'Furrier': {'Wealth': 0, 'Class': []},
                   'Tailor': {'Wealth': 0, 'Class': []},
                   'Jeweler': {'Wealth': 0, 'Class': []},
                   'Pastrycook': {'Wealth': 0, 'Class': []},
                   'Mason': {'Wealth': 0, 'Class': []},
                   'Carpenter': {'Wealth': 0, 'Class': []},
                   'Weaver': {'Wealth': 0, 'Class': []},
                   'Chandler': {'Wealth': 0, 'Class': []},
                   'Cooper (Barrel-maker)': {'Wealth': 0, 'Class': []},
                   'Baker': {'Wealth': 0, 'Class': []},
                   'Hatmaker': {'Wealth': 0, 'Class': []},
                   'Saddler': {'Wealth': 0, 'Class': []},
                   'Chicken Butcher': {'Wealth': 0, 'Class': []},
                   'Pursemaker': {'Wealth': 0, 'Class': []},
                   'Butcher': {'Wealth': 0, 'Class': []},
                   'Buckler-maker': {'Wealth': 0, 'Class': []},
                   'Plasterer': {'Wealth': 0, 'Class': []},
                   'Blacksmith': {'Wealth': 0, 'Class': []},
                   'Painter': {'Wealth': 0, 'Class': []},
                   'Roofer': {'Wealth': 0, 'Class': []},
                   'Locksmith': {'Wealth': 0, 'Class': []},
                   'Ropemaker': {'Wealth': 0, 'Class': []},
                   'Tanner': {'Wealth': 0, 'Class': []},
                   'Rugmaker': {'Wealth': 0, 'Class': []},
                   'Harness-Maker': {'Wealth': 0, 'Class': []},
                   'Bleacher': {'Wealth': 0, 'Class': []},
                   'Cutler': {'Wealth': 0, 'Class': []},
                   'Glovemaker': {'Wealth': 0, 'Class': []},
                   'Woodcarver': {'Wealth': 0, 'Class': []},
                   'Accoutrement maker': {'Wealth': 0, 'Class': []},
                   'Arkwright': {'Wealth': 0, 'Class': []},
                   'Armorer': {'Wealth': 0, 'Class': []},
                   'Balancemaker': {'Wealth': 0, 'Class': []},
                   'Basketmaker': {'Wealth': 0, 'Class': []},
                   'Brewer': {'Wealth': 0, 'Class': []},
                   'Bellmaker': {'Wealth': 0, 'Class': []},
                   'Bottelier': {'Wealth': 0, 'Class': []},
                   'Bowyer': {'Wealth': 0, 'Class': []},
                   'Brickmaker': {'Wealth': 0, 'Class': []},
                   'Broom maker': {'Wealth': 0, 'Class': []},
                   'Canvasser': {'Wealth': 0, 'Class': []},
                   'Card maker': {'Wealth': 0, 'Class': []},
                   'Cartographer': {'Wealth': 0, 'Class': []},
                   'Cartwright': {'Wealth': 0, 'Class': []},
                   'Chainmaker': {'Wealth': 0, 'Class': []},
                   'Cheesemaker': {'Wealth': 0, 'Class': []},
                   'Clockmaker': {'Wealth': 0, 'Class': []},
                   'Dyer': {'Wealth': 0, 'Class': []},
                   'Embroiderer': {'Wealth': 0, 'Class': []},
                   'Feltmaker': {'Wealth': 0, 'Class': []},
                   'Fletcher': {'Wealth': 0, 'Class': []},
                   'Foundryman': {'Wealth': 0, 'Class': []},
                   'Girdler': {'Wealth': 0, 'Class': []},
                   'Glassblower': {'Wealth': 0, 'Class': []},
                   'Horner,': {'Wealth': 0, 'Class': []},
                   'Lampwright': {'Wealth': 0, 'Class': []},
                   'Luthier': {'Wealth': 0, 'Class': []},
                   'Minter': {'Wealth': 0, 'Class': []},
                   'Mirrorer': {'Wealth': 0, 'Class': []},
                   'Nedeller': {'Wealth': 0, 'Class': []},
                   'Parchmenter': {'Wealth': 0, 'Class': []},
                   'Rectifier': {'Wealth': 0, 'Class': []},
                   'Reedmaker': {'Wealth': 0, 'Class': []},
                   'Rugweaver': {'Wealth': 0, 'Class': []},
                   'Spectaclemaker': {'Wealth': 0, 'Class': []},
                   'Stonecutter': {'Wealth': 0, 'Class': []},
                   'Tapicer': {'Wealth': 0, 'Class': []},
                   'Vintner': {'Wealth': 0, 'Class': []},
                   'Wheelwright': {'Wealth': 0, 'Class': []},
                   'Advocate': {'Wealth': 0, 'Class': []},
                   'Architect': {'Wealth': 0, 'Class': []},
                   'Barber': {'Wealth': 0, 'Class': []},
                   'Bather': {'Wealth': 0, 'Class': []},
                   'Builder': {'Wealth': 0, 'Class': []},
                   'Carter': {'Wealth': 0, 'Class': []},
                   'Copyist': {'Wealth': 0, 'Class': []},
                   'Dentist': {'Wealth': 0, 'Class': []},
                   'Doctor': {'Wealth': 0, 'Class': []},
                   'Falconer': {'Wealth': 0, 'Class': []},
                   'Fewterer (Keeper of dogs)': {'Wealth': 0, 'Class': []},
                   'Ferryman': {'Wealth': 0, 'Class': []},
                   'Gardner': {'Wealth': 0, 'Class': []},
                   'Gravedigger': {'Wealth': 0, 'Class': []},
                   'Horse groomer': {'Wealth': 0, 'Class': []},
                   'Launderer': {'Wealth': 0, 'Class': []},
                   'Link boy (Torch carrier)': {'Wealth': 0, 'Class': []},
                   'Maid': {'Wealth': 0, 'Class': []},
                   'Messanger': {'Wealth': 0, 'Class': []},
                   'Miner': {'Wealth': 0, 'Class': []},
                   'Miller': {'Wealth': 0, 'Class': []},
                   'Porter': {'Wealth': 0, 'Class': []},
                   'Prostitute': {'Wealth': 0, 'Class': []},
                   'Raker': {'Wealth': 0, 'Class': []},
                   'Restaurateur': {'Wealth': 0, 'Class': []},
                   'Tenter': {'Wealth': 0, 'Class': []},
                   'Water Carrier': {'Wealth': 0, 'Class': []},
                   'Adventurer': {'Wealth': 0, 'Class': []},
                   'Beggar': {'Wealth': 0, 'Class': []},
                   'Hermit': {'Wealth': 0, 'Class': []},
                   'Savage': {'Wealth': 0, 'Class': []}}