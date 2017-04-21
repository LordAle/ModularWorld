
# Lists used when generating all other objects
# Should be the only thing that require modification to create a new world type


# Master, Spouse, Child and Unique are special roles that are used in source code and should not be modified
roles = ['Master', 'Spouse', 'Child', 'Servant', 'Security', 'Apprentice', 'Unique', 'Visitor']

races = ['Dwarf', 'Elf', 'Halfling', 'Human', 'Gnome', 'Half-Elf', 'Half-Orc']

# Support for different genders isn't included yet
genders = ['Male', 'Female']

# The range is used to indicate adult and maximal age for each race
ages = {'Dwarf': (25, 150), 'Elf': (30, 200), 'Halfling': (20, 100), 'Human': (16, 80), 'Gnome': (22, 120),
        'Half-Elf': (22, 120), 'Half-Orc': (14, 70)}

# Wealth position is used in profession_info, ordering matters
wealth = ['Poor', 'Middle', 'Rich']

classes = ['Fighter', 'Rogue', 'Wizard', 'Cleric']

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
profession_entertainer = ['Acrobat','Actor','Illuminator','Musician','Painter (Art)','Sculptor','Singer','Writer']
profession_food_provider = ['Farmer','Fisherman','Herder','Hunter']
profession_scholar = ['Alchemist','Astronomer','Librarian','Mathematician','Mage','Philosopher','Professor','Theologian']
profession_sailor = ['Navigator','Sailor','Captain','Sailmaker','Shipwright']
profession_craftsman = ['Shoemaker','Furrier','Tailor','Jeweler','Pastrycook','Mason','Carpenter','Weaver','Chandler','Cooper (Barrel-maker)',
                        'Baker','Hatmaker','Saddler','Chicken Butcher','Pursemaker','Butcher','Buckler-maker','Plasterer','Blacksmith','Painter',
                        'Roofer','Locksmith','Ropemaker','Tanner','Rugmaker','Harness-Maker','Bleacher','Cutler','Glovemaker','Woodcarver',
                        'Accoutrement maker','Arkwright','Armorer','Balancemaker','Basketmaker','Brewer','Bellmaker', 'Bottelier','Bowyer','Brickmaker',
                        'Broom maker','Canvasser','Card maker','Cartographer','Cartwright','Chainmaker','Cheesemaker','Clockmaker','Dyer','Embroiderer',
                        'Feltmaker','Fletcher','Foundryman','Girdler','Glassblower','Horner,','Lampwright','Luthier','Minter','Mirrorer',
                        'Nedeller','Parchmenter','Rectifier','Reedmaker','Rugweaver','Spectaclemaker','Stonecutter','Tapicer','Vintner','Wheelwright']
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



##################Weight###############################

#All lists of weight are here
#Each weight list lenght must match exactly the lenght of the base list
#The remove a value from a base list, it is preferred to use a value of 0 in the weight list and generate a weighted list

weight_race = [0,0,0,5,0,0,0]
weight_gender = [1,1]
weight_age = [1,2,3,3,3,2,2,1]
weight_alignment = [3,5,2,4,3,2,3,2,1]
weight_social_class_dominant = [15,4,1]
weight_social_class_accepted = [50,10,1]
weight_social_class_ostracized = [200,20,1]
weight_occupation = [0,4,2,2,6,4,1,175,1,16,16,4,1]
weight_occupation_high_class = [16,4,1,0,3,4,2,0,3,0,8,2,0]
weight_occupation_middle_class = [4,16,6,3,9,12,3,77,2,0,56,8,0]
weight_occupation_low_class = [0,0,3,7,18,4,0,697,0,0,16,10,5]

weight_governance = [1,4,1,2,2,1,1,1,20,1,0,77,1]
weight_military = [30,1,140,5,20,1,1,2]
weight_security = [3,3,49,1,6]
weight_criminal = [10,1,4,8,12,12]
weight_religious = [9,40,1,9500,450]
weight_merchant = [2,1,5,1,17,33,11,3,2,2,6,3,4,6,4]
weight_entertainer = [6,2,1,5,2,2,1,1]
weight_food_provider = [95,0,4,1]
weight_scholar = [2,1,2,1,6,1,6,1]
weight_sailor = [1,20,1,2,4]
weight_craftsman = [60,60,60,30,25,25,25,20,17,17,
15,13,12,12,11,10,8,8,8,8,
7,6,6,6,6,6,5,5,5,5,
8,5,20,3,8,15,3,8,10,15,
8,4,4,3,8,7,15,3,8,5,
8,10,8,8,5,4,8,4,4,5,
5,5,10,4,7,4,5,7,15,8]
weight_service=  [14,1,28,4,6,4,4,1,6,1,
1,1,2,1,2,8,1,40,2,10,
2,8,20,4,24,20,10]
weight_other = [8,8,1,1]




