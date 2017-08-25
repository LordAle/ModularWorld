from objects import attribute 
from objects import morality 
from objects import race 
from objects import culture 
from objects import city_size 
from objects import building_kind 
from objects import social_group 
from objects import profession 
from objects import professions_group 
# This file is automatically generated by catalog_writer.py with the .csv files in the catalogs folder 

attributes = (attribute.Attribute("Strength", [7,19], 10, 2, 1), 
attribute.Attribute("Dexterity", [7,19], 10, 2, 1), 
attribute.Attribute("Constitution", [7,19], 10, 2, 1), 
attribute.Attribute("Intelligence", [7,19], 10, 2, 1), 
attribute.Attribute("Wisdom", [7,19], 10, 2, 1), 
attribute.Attribute("Charisma", [7,19], 10, 2, 1), 
) 

moralities = (morality.Morality("Altruism", [-1,1], 0, 0.2, 0, 1), 
morality.Morality("Order", [-1,1], 0, 0.2, 0, 1), 
) 

races = {"Error": race.Race("Error", 0, 0, 0, []), 
"Default": race.Race("Default", 0, 0, 0, []), 
"Human": race.Race("Human", 12, 16, 80, []), 
"Dwarf": race.Race("Dwarf", 14, 25, 150, ["Charisma-1", "Constitution+2"]), 
"Elf": race.Race("Elf", 18, 30, 200, ["Dexterity+2", "Constitution-1"]), 
"Halfling": race.Race("Halfling", 13, 20, 100, ["Strength-1", "Dexterity+2"]), 
"Gnome": race.Race("Gnome", 13, 22, 120, ["Intelligence+2"]), 
"Half-Elf": race.Race("Half-Elf", 13, 22, 120, []), 
"Half-Orc": race.Race("Half-Orc", 10, 14, 70, ["Strength+2", "Intelligence-1"]), 
} 

cultures = {"Error": culture.Culture("Error", races["Error"], [], "Equal", 0, [], []), 
"Default": culture.Culture("Default", races["Error"], [], "Equal", 0, [], []), 
"Human": culture.Culture("Human", races["Human"], [], "Patriarchal", 20, ["Halfling", "Half-Elven", "Half-Orcish", "Dwarven", "Gnomish", "Elven"], [8,4,3,1,1,1]), 
"Dwarven": culture.Culture("Dwarven", races["Dwarf"], ["Order+0.6"], "Patriarchal", 5, ["Gnomish", "Human", "Halfling"], [3,1,1]), 
"Elven": culture.Culture("Elven", races["Elf"], ["Altruism+0.5", "Order-0.5"], "Equal", 5, ["Half-Elven", "Halfling", "Human", "Gnomish"], [4,1,1,1]), 
"Halfling": culture.Culture("Halfling", races["Halfling"], ["Altruism+0.5", "Order+0.5"], "Equal", 15, ["Human", "Gnomish", "Half-Elven"], [7,2,1]), 
"Gnomish": culture.Culture("Gnomish", races["Gnome"], ["Order-0.5"], "Matriarchal", 5, ["Elven", "Dwarven", "Halfling", "Human", "Half-Elven"], [1,1,1,1,1]), 
"Half-Elven": culture.Culture("Half-Elven", races["Half-Elf"], [], "Equal", 10, ["Human", "Elven", "Halfling", "Gnomish"], [5,4,3,1]), 
"Half-Orcish": culture.Culture("Half-Orcish", races["Half-Orc"], ["Altruism-0.2", "Order-0.2"], "Patriarchal", 10, ["Human"], [1]), 
} 

city_sizes = {"Error": city_size.City_Size("Error", (0, 0)), 
"Default": city_size.City_Size("Default", (0, 0)), 
"Village": city_size.City_Size("Village", (20, 1000)), 
"Town": city_size.City_Size("Town", (1000, 8000)), 
"City": city_size.City_Size("City", (8000, 20000)), 
"Metropolis": city_size.City_Size("Metropolis", (20000, 100000)), 
} 

professions = {"Error": profession.Profession("Error", 0, "", 0), 
"Default": profession.Profession("Default", 0, "", 0), 
"Child": profession.Profession("Child", 0, "", 0), 
"Same": profession.Profession("Same", 0, "", 0), 
"Burgomeister": profession.Profession("Burgomeister", 0.4, "", 1), 
"Chancellor": profession.Profession("Chancellor", 0.6, "", 1), 
"Constable": profession.Profession("Constable", 0.6, "", 1), 
"Diplomat": profession.Profession("Diplomat", 0.6, "", 0), 
"Exchequer": profession.Profession("Exchequer", 0.7, "", 1), 
"Forester": profession.Profession("Forester", 0.6, "Forest", 1), 
"Judge": profession.Profession("Judge", 0.6, "", 1), 
"Knight": profession.Profession("Knight", 0.6, "", 0), 
"Local Lord": profession.Profession("Local Lord", 0.9, "", 1), 
"Noble": profession.Profession("Noble", 0.6, "", 0), 
"Soldier": profession.Profession("Soldier", 0.1, "", 0), 
"Guard": profession.Profession("Guard", 0.1, "", 0), 
"Thief": profession.Profession("Thief", 0.1, "", 0), 
"Acolyte": profession.Profession("Acolyte", 0.05, "", 0), 
"High Priest": profession.Profession("High Priest", 0.5, "", 0), 
"Priest": profession.Profession("Priest", 0.15, "", 0), 
"Banker": profession.Profession("Banker", 0.7, "", 0), 
"Innkeeper": profession.Profession("Innkeeper", 0.4, "", 0), 
"Merchant": profession.Profession("Merchant", 0.15, "", 0), 
"Artist": profession.Profession("Artist", 0.05, "", 0), 
"Farmer": profession.Profession("Farmer", 0.05, "", 0), 
"Fisherman": profession.Profession("Fisherman", 0.05, "Water", 0), 
"Herder": profession.Profession("Herder", 0.2, "Plain", 0), 
"Scholar": profession.Profession("Scholar", 0.3, "", 0), 
"Sailor": profession.Profession("Sailor", 0.05, "Sea", 0), 
"Ship Captain": profession.Profession("Ship Captain", 0.3, "Sea", 0), 
"Apprentice": profession.Profession("Apprentice", 0.1, "", 0), 
"Blacksmith": profession.Profession("Blacksmith", 0.3, "", 0), 
"Builder": profession.Profession("Builder", 0.2, "", 0), 
"Cook": profession.Profession("Cook", 0.2, "", 0), 
"Leatherworker": profession.Profession("Leatherworker", 0.2, "", 0), 
"Tailor": profession.Profession("Tailor", 0.2, "", 0), 
"Woodworker": profession.Profession("Woodworker", 0.2, "", 0), 
"Specialist Craftsman": profession.Profession("Specialist Craftsman", 0.2, "", 0), 
"Animal Keeper": profession.Profession("Animal Keeper", 0.4, "", 0), 
"Barber": profession.Profession("Barber", 0.05, "", 0), 
"Bather": profession.Profession("Bather", 0.4, "", 0), 
"Doctor": profession.Profession("Doctor", 0.4, "", 0), 
"Ferryman": profession.Profession("Ferryman", 0.05, "River", 0), 
"Gardner": profession.Profession("Gardner", 0.1, "", 0), 
"Gravedigger": profession.Profession("Gravedigger", 0, "", 0), 
"Maid": profession.Profession("Maid", 0.05, "", 0), 
"Miner": profession.Profession("Miner", 0.05, "Mine", 0), 
"Miller": profession.Profession("Miller", 0.4, "", 0), 
"Midwife": profession.Profession("Midwife", 0.05, "", 0), 
"Raker": profession.Profession("Raker", 0, "", 0), 
"Tenter": profession.Profession("Tenter", 0.05, "", 0), 
"Water Carrier": profession.Profession("Water Carrier", 0, "", 0), 
"Adventurer": profession.Profession("Adventurer", 0.3, "", 0), 
"Beggar": profession.Profession("Beggar", 0, "", 0), 
"Hermit": profession.Profession("Hermit", 0, "", 0), 
"Savage": profession.Profession("Savage", 0, "", 0), 
} 

social_groups = {"Error": social_group.Social_Group("Error", 0, "", "", [], [], [cultures["Error"]]), 
"Default": social_group.Social_Group("Default", 0, "", "", [], [], [cultures["Error"]]), 
"Noble": social_group.Social_Group("Noble", 1, "", "", [], [], [], [professions["Noble"]], [1]), 
"Bourgeois": social_group.Social_Group("Bourgeois", 0, "", ">0.4", [], [], [], [professions["Merchant"]], [1]), 
"Commoner": social_group.Social_Group("Commoner", 0, "", "<0.4", [], [], [], [professions["Miner"], professions["Tenter"]], [1,1]), 
"Farmer": social_group.Social_Group("Farmer", 0, "", "<0.4", [], [], [], [professions["Farmer"]], [1]), 
"Servant": social_group.Social_Group("Servant", 0, "Female", "<0.4", [], [], [], [professions["Maid"]], [1]), 
"Craftsman": social_group.Social_Group("Craftsman", 0, "", ">0.2", ["Dexterity>9"], [], [], [professions["Blacksmith"], professions["Builder"], professions["Leatherworker"], professions["Tailor"], professions["Woodworker"]], [1,2,2,3,2]), 
"Scholar": social_group.Social_Group("Scholar", 0, "", ">0.3", ["Intelligence>12"], [], [cultures["Human"], cultures["Elven"], cultures["Dwarven"]], [professions["Scholar"]], [1]), 
"Religious": social_group.Social_Group("Religious", 0, "", "", ["Wisdom>11"], [], [], [professions["Acolyte"], professions["Priest"]], [3,1]), 
"Criminal": social_group.Social_Group("Criminal", 0, "", "", [], ["Altruism<0"], [], [professions["Thief"]], [1]), 
"Artist": social_group.Social_Group("Artist", 0, "", "", ["Charisma>11"], [], [], [professions["Artist"]], [1]), 
"Military": social_group.Social_Group("Military", 0, "Male", ">0.2", ["Strength>11", "Constitution>9"], ["Order>0"], [], [professions["Guard"]], [1]), 
"Outsider": social_group.Social_Group("Outsider", 0, "", "", [], [], [], [professions["Hermit"], professions["Savage"]], [1,1]), 
"Monster": social_group.Social_Group("Monster", 1, "", "", [], [], [], [professions["Savage"]], [1]), 
} 

professions_groups = {"Default": professions_group.Professions_Group("Default", social_groups["Default"], 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], []), 
"Farmer Family": professions_group.Professions_Group("Farmer Family", social_groups["Farmer"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Farmer"], professions["Fisherman"], professions["Herder"]], [10,10,5], [professions["Farmer"], professions["Fisherman"], professions["Herder"]], [10,10,5]), 
"Commoner Family": professions_group.Professions_Group("Commoner Family", social_groups["Commoner"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Barber"], professions["Ferryman"], professions["Gravedigger"], professions["Midwife"], professions["Raker"], professions["Water Carrier"]], [1,1,1,1,1,1], [professions["Barber"], professions["Ferryman"], professions["Gravedigger"], professions["Midwife"], professions["Raker"], professions["Water Carrier"]], [1,1,1,1,1,1]), 
"Bourgeois Family": professions_group.Professions_Group("Bourgeois Family", social_groups["Bourgeois"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Animal Keeper"], professions["Bather"], professions["Burgomeister"], professions["Doctor"], professions["Miller"]], [2,1,5,2,3], [professions["Animal Keeper"], professions["Bather"], professions["Burgomeister"], professions["Doctor"], professions["Miller"]], [2,1,5,2,3]), 
"Noble Family": professions_group.Professions_Group("Noble Family", social_groups["Noble"], 1, 1, 1, 1,
                5, 1, 1, 0, [professions["Diplomat"], professions["Knight"], professions["Noble"], professions["Chancellor"], professions["Constable"], professions["Exchequer"], professions["Forester"]], [1,2,2,3,3,3,3], [professions["Diplomat"], professions["Knight"], professions["Noble"], professions["Chancellor"], professions["Constable"], professions["Exchequer"], professions["Forester"]], [1,2,2,3,3,3,3]), 
"Tavern Family": professions_group.Professions_Group("Tavern Family", social_groups["Commoner"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Cook"]], [1], [professions["Cook"]], [1]), 
"Inn Family": professions_group.Professions_Group("Inn Family", social_groups["Bourgeois"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Innkeeper"]], [1], [professions["Innkeeper"]], [1]), 
"Hospital Family": professions_group.Professions_Group("Hospital Family", social_groups["Bourgeois"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Doctor"]], [1], [professions["Doctor"]], [1]), 
"Bank Family": professions_group.Professions_Group("Bank Family", social_groups["Bourgeois"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Banker"]], [1], [professions["Banker"]], [1]), 
"General Store Family": professions_group.Professions_Group("General Store Family", social_groups["Commoner"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Merchant"]], [1], [professions["Merchant"]], [1]), 
"Luxury Store Family": professions_group.Professions_Group("Luxury Store Family", social_groups["Bourgeois"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Merchant"]], [1], [professions["Merchant"]], [1]), 
"Blacksmith Family": professions_group.Professions_Group("Blacksmith Family", social_groups["Craftsman"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Blacksmith"]], [1], [professions["Blacksmith"]], [1]), 
"Tailor Family": professions_group.Professions_Group("Tailor Family", social_groups["Craftsman"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Tailor"]], [1], [professions["Tailor"]], [1]), 
"Leatherwork Family": professions_group.Professions_Group("Leatherwork Family", social_groups["Craftsman"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Leatherworker"]], [1], [professions["Leatherworker"]], [1]), 
"Woodwork Family": professions_group.Professions_Group("Woodwork Family", social_groups["Craftsman"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Woodworker"]], [1], [professions["Woodworker"]], [1]), 
"Builder Family": professions_group.Professions_Group("Builder Family", social_groups["Craftsman"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Builder"]], [1], [professions["Builder"]], [1]), 
"Misc Workshop Family": professions_group.Professions_Group("Misc Workshop Family", social_groups["Craftsman"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Specialist Craftsman"]], [1], [professions["Specialist Craftsman"]], [1]), 
"Stronghold Family": professions_group.Professions_Group("Stronghold Family", social_groups["Noble"], 1, 1, 1, 1,
                5, 1, 1, 1, [professions["Local Lord"]], [1], [professions["Local Lord"]], [1]), 
"Master Shrine": professions_group.Professions_Group("Master Shrine", social_groups["Religious"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Acolyte"], professions["Priest"]], [1,1]), 
"Master Church": professions_group.Professions_Group("Master Church", social_groups["Religious"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Priest"]], [1]), 
"Master Cathedral": professions_group.Professions_Group("Master Cathedral", social_groups["Religious"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["High Priest"]], [1]), 
"Master School": professions_group.Professions_Group("Master School", social_groups["Scholar"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Scholar"]], [1]), 
"Master University": professions_group.Professions_Group("Master University", social_groups["Scholar"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Scholar"]], [1]), 
"Master Prison": professions_group.Professions_Group("Master Prison", social_groups["Military"], 1, 0, 0, 0,
                5, 1, 0, 1, [], [], [professions["Guard"]], [1]), 
"Master Barrack": professions_group.Professions_Group("Master Barrack", social_groups["Military"], 1, 0, 0, 0,
                5, 1, 0, 1, [], [], [professions["Soldier"]], [1]), 
"Master Fortress": professions_group.Professions_Group("Master Fortress", social_groups["Military"], 1, 0, 0, 0,
                5, 1, 0, 1, [], [], [professions["Soldier"]], [1]), 
"Master Thieves Den": professions_group.Professions_Group("Master Thieves Den", social_groups["Criminal"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Thief"]], [1]), 
"Master Criminal Front": professions_group.Professions_Group("Master Criminal Front", social_groups["Criminal"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Thief"]], [1]), 
"Master Artists Guild": professions_group.Professions_Group("Master Artists Guild", social_groups["Artist"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Artist"]], [1]), 
"Master Circus": professions_group.Professions_Group("Master Circus", social_groups["Artist"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Artist"]], [1]), 
"Master Museum": professions_group.Professions_Group("Master Museum", social_groups["Scholar"], 1, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Scholar"]], [1]), 
"Maid Few": professions_group.Professions_Group("Maid Few", social_groups["Servant"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Maid"]], [1]), 
"Maid Some": professions_group.Professions_Group("Maid Some", social_groups["Servant"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Maid"]], [1]), 
"Maid Many": professions_group.Professions_Group("Maid Many", social_groups["Servant"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Maid"]], [1]), 
"Guard Few": professions_group.Professions_Group("Guard Few", social_groups["Military"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Guard"]], [1]), 
"Guard Some": professions_group.Professions_Group("Guard Some", social_groups["Military"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Guard"]], [1]), 
"Guard Many": professions_group.Professions_Group("Guard Many", social_groups["Military"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Guard"]], [1]), 
"Apprentice Few": professions_group.Professions_Group("Apprentice Few", social_groups["Craftsman"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Apprentice"]], [1]), 
"Apprentice Some": professions_group.Professions_Group("Apprentice Some", social_groups["Craftsman"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Apprentice"]], [1]), 
"Apprentice Many": professions_group.Professions_Group("Apprentice Many", social_groups["Craftsman"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Apprentice"]], [1]), 
"Tenter Few": professions_group.Professions_Group("Tenter Few", social_groups["Craftsman"], 0, 0, 0, 0,
                5, 1, 0, 1, [], [], [professions["Tenter"]], [1]), 
"Tenter Some": professions_group.Professions_Group("Tenter Some", social_groups["Craftsman"], 0, 0, 0, 0,
                5, 1, 0, 1, [], [], [professions["Tenter"]], [1]), 
"Tenter Many": professions_group.Professions_Group("Tenter Many", social_groups["Craftsman"], 0, 0, 0, 0,
                5, 1, 0, 1, [], [], [professions["Tenter"]], [1]), 
"Hospital Employee": professions_group.Professions_Group("Hospital Employee", social_groups["Commoner"], 0, 0, 0, 0,
                5, 1, 0, 1, [], [], [professions["Cook"], professions["Midwife"], professions["Water Carrier"]], [1,3,1]), 
"Acolyte Few": professions_group.Professions_Group("Acolyte Few", social_groups["Religious"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Acolyte"]], [1]), 
"Priest Few": professions_group.Professions_Group("Priest Few", social_groups["Religious"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Priest"]], [1]), 
"Scholar Many": professions_group.Professions_Group("Scholar Many", social_groups["Scholar"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Scholar"]], [1]), 
"Thief Some": professions_group.Professions_Group("Thief Some", social_groups["Criminal"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Thief"]], [1]), 
"Artist Some": professions_group.Professions_Group("Artist Some", social_groups["Artist"], 0, 0, 0, 0,
                5, 1, 1, 1, [], [], [professions["Artist"]], [1]), 
} 

building_kinds = {"Error": building_kind.Building_Kind("Error", 0, 0, []), 
"Default": building_kind.Building_Kind("Default", 0, 0, []), 
"Farmer": building_kind.Building_Kind("Farmer", 0, 8, [professions_groups["Farmer Family"]]), 
"Commoner": building_kind.Building_Kind("Commoner", 0, 3, [professions_groups["Commoner Family"]]), 
"Bourgeois": building_kind.Building_Kind("Bourgeois", 500, 2, [professions_groups["Bourgeois Family"], professions_groups["Maid Few"]]), 
"Noble": building_kind.Building_Kind("Noble", 1000, 1, [professions_groups["Noble Family"], professions_groups["Maid Some"], professions_groups["Guard Few"]]), 
"Tavern": building_kind.Building_Kind("Tavern", 250, 5, [professions_groups["Tavern Family"], professions_groups["Maid Few"]]), 
"Inn": building_kind.Building_Kind("Inn", 750, 2, [professions_groups["Inn Family"], professions_groups["Maid Some"]]), 
"Hospital": building_kind.Building_Kind("Hospital", 1500, 1, [professions_groups["Hospital Family"], professions_groups["Hospital Employee"]]), 
"Bank": building_kind.Building_Kind("Bank", 5000, 1, [professions_groups["Bank Family"], professions_groups["Guard Some"]]), 
"General Store": building_kind.Building_Kind("General Store", 500, 5, [professions_groups["General Store Family"]]), 
"Luxury Store": building_kind.Building_Kind("Luxury Store", 1500, 1, [professions_groups["Luxury Store Family"], professions_groups["Guard Few"]]), 
"Blacksmith": building_kind.Building_Kind("Blacksmith", 200, 2, [professions_groups["Blacksmith Family"], professions_groups["Apprentice Few"], professions_groups["Tenter Some"]]), 
"Tailor": building_kind.Building_Kind("Tailor", 0, 3, [professions_groups["Tailor Family"], professions_groups["Apprentice Few"], professions_groups["Tenter Few"]]), 
"Leatherwork": building_kind.Building_Kind("Leatherwork", 0, 3, [professions_groups["Leatherwork Family"], professions_groups["Apprentice Few"], professions_groups["Tenter Few"]]), 
"Woodwork": building_kind.Building_Kind("Woodwork", 0, 2, [professions_groups["Woodwork Family"], professions_groups["Apprentice Few"], professions_groups["Tenter Some"]]), 
"Builder": building_kind.Building_Kind("Builder", 500, 2, [professions_groups["Builder Family"], professions_groups["Apprentice Some"], professions_groups["Tenter Many"]]), 
"Misc Workshop": building_kind.Building_Kind("Misc Workshop", 1000, 1, [professions_groups["Misc Workshop Family"], professions_groups["Apprentice Few"], professions_groups["Tenter Few"]]), 
"Keep": building_kind.Building_Kind("Keep", 0, 0, [professions_groups["Stronghold Family"], professions_groups["Maid Some"], professions_groups["Guard Some"]]), 
"Castle (Small)": building_kind.Building_Kind("Castle (Small)", 1000, 0, [professions_groups["Stronghold Family"], professions_groups["Maid Some"], professions_groups["Guard Some"]]), 
"Castle (Large)": building_kind.Building_Kind("Castle (Large)", 8000, 0, [professions_groups["Stronghold Family"], professions_groups["Maid Many"], professions_groups["Guard Many"]]), 
"Shrine": building_kind.Building_Kind("Shrine", 0, 5, [professions_groups["Master Shrine"]]), 
"Church": building_kind.Building_Kind("Church", 1000, 2, [professions_groups["Master Church"], professions_groups["Acolyte Few"]]), 
"Cathedral": building_kind.Building_Kind("Cathedral", 8000, 1, [professions_groups["Master Cathedral"], professions_groups["Acolyte Few"], professions_groups["Priest Few"]]), 
"School": building_kind.Building_Kind("School", 1000, 5, [professions_groups["Master School"]]), 
"University": building_kind.Building_Kind("University", 8000, 1, [professions_groups["Master University"], professions_groups["Scholar Many"]]), 
"Prison": building_kind.Building_Kind("Prison", 500, 5, [professions_groups["Master Prison"], professions_groups["Guard Some"]]), 
"Barrack": building_kind.Building_Kind("Barrack", 1000, 5, [professions_groups["Master Barrack"], professions_groups["Guard Many"]]), 
"Fortress": building_kind.Building_Kind("Fortress", 8000, 1, [professions_groups["Master Fortress"], professions_groups["Guard Many"]]), 
"Thieves Den": building_kind.Building_Kind("Thieves Den", 1000, 1, [professions_groups["Master Thieves Den"], professions_groups["Thief Some"]]), 
"Criminal Front": building_kind.Building_Kind("Criminal Front", 1000, 1, [professions_groups["Master Criminal Front"]]), 
"Artists Guild": building_kind.Building_Kind("Artists Guild", 1000, 5, [professions_groups["Master Artists Guild"], professions_groups["Artist Some"]]), 
"Circus": building_kind.Building_Kind("Circus", 3000, 2, [professions_groups["Master Circus"], professions_groups["Artist Some"]]), 
"Museum": building_kind.Building_Kind("Museum", 8000, 1, [professions_groups["Master Museum"], professions_groups["Guard Few"]]), 
"Homeless": building_kind.Building_Kind("Homeless", 0, 0, []), 
} 

cultures["Human"].fill_names_lists(["Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd", "Bor", "Fodel", "Glar", "Grogor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Melcer", "Stor", "Toman", "Urth"], ["Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele", "Alethra", "Kara", "Katernin", "Mara", "Natali", "Olma", "Tana", "Zora", "Amafrey", "Betha", "Cefrey", "Kethra", "Olga", "Silifrey", "Westra"], ["Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag", "Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag", "Brightwood", "Helder", "Hornraven", "Stormwind", "Windrivver"], ["Aberdovy", "Abergavenny", "Abingdon", "Acre", "Adderbury", "Adwick", "Albans", "Alberbuty", "Aldbourne", "Aldbrough", "Aldeburgh", "Alford", "Alfreton", "Alnwick", "Alton", "Amersham", "Ampthill", "Ancaster", "Appleby", "Arundel", "Asaph", "Ashburton", "Ashby", "Ashingdon", "Ashton", "Auckland", "Aust", "Avon", "Axbridge", "Axminster", "Aylesbury", "Bakewell", "Baldock", "Bamburgh", "Bampton", "Banbury", "Bangor", "Barborough", "Bardney", "Barfreston", "Barney", "Barnstaple", "Barton", "Basingstoke", "Bath", "Beaminster", "Beaulieu", "Beaumaris", "Bebington", "Beetham", "Belsay", "Belvoir", "Benfleet", "Berkeley", "Berkhamsted", "Berwick", "Beverly", "Bewcastle", "Billinghame", "Birmingham", "Bloxham", "Bodiam", "Bodmin", "Boews", "Boiam", "Bolingbroke", "Bolton", "Bordesly", "Boston", "Bosworth", "Bowes", "Brackley", "Bradford", "Brading", "Bramber", "Brancaster", "Brandon", "Brandwell", "Brassington", "Brecon", "Bridgeorth", "Bridgewater", "Bridport", "Brinkburn", "Bristol", "Broadway", "Brough", "Brougham", "Broughton", "Brton", "Buckden", "Buckfast", "Buckingham", "Buildwas", "Builth", "Bungay", "Burgh", "Burnell", "Burnley", "Burton", "Bury", "Bushbury", "Buttington", "Byland", "Bytham", "Caerleon", "Caerphilly", "Caerwent", "Caister", "Calne", "Cambridge", "Camelford", "Campden", "Canderbury", "Carew", "Carisbrooke", "Carlisle", "Carmarthen", "Carnarvon", "Cartmel", "Castor", "Catterick", "Ccooling", "Cennen", "Cerne", "Chagford", "Chalgrove", "Chatham", "Cheltenham", "Chemsford", "Chepstow", "Chersey", "Cheshunt", "Chester", "Chesterfield", "Chichester", "Chilham", "Chillingham", "Chippenham", "Chirbury", "Chirk", "Chorley", "Christechurch", "Cirencester", "Cleeve", "Clifford", "Clun", "Coch", "Cockermouth", "Coggeshaf", "Colchester", "Colne", "Combe", "Compton", "Conway", "Corwen", "Craydon", "Crediton", "Crewkerne", "Criccieth", "Cricklade", "Croston", "Crowland", "Crucis", "Darley", "Deal", "Deanwy", "Deerhurst", "Denanwy", "Denbigh", "Derby", "Dereham", "Devizes", "Dorchester", "Dorking", "Dover", "Drayton", "Dudley", "Dunmow", "Dunstable", "Dunstanburgh", "Dunwich", "Durham", "Dyserth", "Ebbsfleet", "Eccleshall", "Edington", "Edmunds", "Egremount", "Elmham", "Elsing", "Elstow", "Ely", "Epping", "Escomb", "Etal", "Eton", "Evesham", "Exeter", "Farindon", "Farnham", "Faversham", "Ffestiniog", "Finchale", "Flint", "Folkingham", "Forde", "Fotheringhay", "Fountains", "Fowey", "Framlingham", "Frith", "Furness", "Gainsborough", "Gastonbury", "Gawood", "Gilling", "Gillingham", "Gloucester", "Goodrich", "Grantham", "Gravesend", "Greenwich", "Grimsby", "Grinstead", "Grosmont", "Guildford", "Haddon", "Hadleigh", "Harcourt", "Harlech", "Harrow", "Hartlepool", "Hastings", "Hatfield", "Haughmond", "Havan", "Haverfordwest", "Hawarden", "Hay", "Haydon", "Hayton", "Hedingham", "Hedon", "Helens", "Helmsley", "Helston", "Herford", "Herstmonceux", "Hertford", "Hever", "Hexham", "Hindon", "Hitchin", "Holbeach", "Holyhead", "Holywell", "Hope", "Horsham", "Hulne", "Hurley", "Hutingdon", "Hutton", "Huyton", "Hythe", "Ilchester", "Ipswich", "Ive", "Jarrow", "Jervaulx", "Kempsford", "Kendal", "Kenilworth", "Kersey", "Kidwelly", "Kimbolton", "Kingsbridge", "Kirby", "Kirdford", "Kirkoswald", "Knaresborough", "LLandaff", "LLawhaden", "Lacock", "Landercost", "Lavenham", "Leicester", "Leiston", "Lewes", "Lichfield", "Lincoln", "Liskeard", "Liverpool", "Llanberis", "Llandovery", "Llaneilian", "Llanstephan", "Llanthony", "Llantwit", "Looe", "Lostwithiel", "Loughborough", "Louth", "Lovell", "Ludgershall", "Ludlow", "Lydbury", "Lydford", "Lyme", "Lympne", "Lynn", "Machylleth", "Maidstone", "Malling", "Malmesbury", "Malton", "Manchester", "Manfield", "Manorbier", "Mardon", "Margam", "Masham", "Melcome", "Merton", "Middleham", "Midhurst", "Midurst", "Milford", "Milton", "Minster", "Mold", "Monkwearmouth", "Monmouth", "Montgomery", "Morecambe", "Moretonhampstead", "Neath", "Netley", "Neville", "Newark", "Newbury", "Newcastle", "Newmarket", "Newport", "Newstead", "Norham", "Northhallterton", "Northleach", "Norton", "Norwich", "Nottingham", "Oakham", "Odiham", "Orford", "Oswestry", "Osyth", "Otford", "Otterburn", "Ottery", "Oxford", "Oxted", "Paignton", "Patrington", "Pebmarsh", "Pembroke", "Penmon", "Penrith", "Penshurst", "Pershore", "Peterborough", "Petersfield", "Pevensey", "Pickering", "Plymoth", "Plympton", "Porchester", "Portishead", "Portsmouth", "Preston", "Raby", "Radcliffe", "Raglan", "Ravenglass", "Ravensworth", "Reading", "Reculver", "Repton", "Rhuddlan", "Richborough", "Richmond", "Ripley", "Ripon", "Roehester", "Rogat", "Rogate", "Romney", "Romsey", "Rotherham", "Rothley", "Royston", "Runnymede", "Ruthin", "Ryde", "Rye", "Saffron", "Salford", "Salisbury", "Sandwich", "Saurm", "Scarborough", "Scunthorpe", "Selby", "Sevenoaks", "Seyning", "Shaftesbury", "Sheffield", "Sherborne", "Shoreham", "Silchester", "Sleaford", "Sompting", "Southampton", "Southwark", "Southwell", "Spalding", "St. Bees", "Stafford", "Stamford", "Stanton", "Starford", "Startford", "Stoesay", "Stratford", "Stratton", "Streeton", "Stretton", "Stroud", "Sudbury", "Sutton", "Swansea", "Tamworth", "Tattershall", "Taunton", "Tavistock", "Tawton", "Teignmouth", "Tewkesbury", "Thetford", "Thorton", "Tintagel", "Tiverton", "Tonbridge", "Tong", "Totnes", "Towcester", "Trent", "Truro", "Turbury", "Tynemouth", "Uffington", "Usk", "Walden", "Wallinford", "Walmer", "Walpole", "Walsingham", "Waltham", "Wantage", "Ware", "Warkworth", "Warton", "Warwick", "Watford", "Wayford", "Wedmore", "Wednesbury", "Weighton", "Welbeck", "Wells", "Welshpool", "Wenlock", "Weobley", "Westbury", "Westminster", "Whalley", "Whitby", "Wickham", "Wigan", "Wigmore", "Wilton", "Wimbledon", "Winchcester", "Winchelsea", "Windsor", "Wirksworth", "Wisbech", "Witham", "Woburn", "Wokingham", "Wolverhampton", "Woodbridge", "Woodstock", "Worstead", "Worthing", "Wressle", "Wrotham", "Wroxeter", "Wycombe", "Yarm", "Yarmouth", "Yeavering", "York"]) 
cultures["Dwarven"].fill_names_lists(["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik", "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"], ["Amber", "Artin", "Audhild", "Bardryn", "Dagnal", "Diesa", "Eldeth", "Falkrunn", "Finellen", "Gunnloda", "Gurdis", "Helja", "Hlin", "Kathra", "Kristryd", "Ilde", "Liftrasa", "Mardred", "Riswynn", "Sannl", "Torbera", "Torgga", "Vistra"], ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Luthgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"], ["Dhomladuhr", "Dhaleduhr", "Kal Oluhm", "Khurnkalduhr", "Thughbuldar", "Nerndarth", "Varn Maldur", "Huguluhr", "Bagdun", "Gor Furuhm", "Dhaghrogh", "Nogkuldihr", "Mirndaral", "Bul Thurum", "Kimheim", "Hoghbuldahr", "Khomoldur", "Kirgurum", "Him Falduhr", "Nul Darim", "Bhagkohm", "Dhirnkohm", "Bhigh Borimm", "Khugdaruhm", "Dhamyur", "Thilfalduhr", "Bagh Lodar", "Vurn Boldihr", "Dherarum", "Gern Boldahr", "Dig Falduhr", "Bheg Kuldohr", "Bintaruhm", "Honruhm", "Dorndorth", "Tholdarahl", "Gontarihr", "Momgrun", "Gin Dural", "Doghgarum", "Kherkihm", "Gurnguruhm", "Thortaruhm", "Gaghfaldur", "Malbor", "Therngran", "Thumgaruhm", "Thagh Loduhr", "Bhegh Todihr", "Delfaldur", "Homyahr", "Nigerum", "Dharneruhm", "Nul Darahl", "Mug Gurum", "Bhar Buldahr", "Khirkolduhr", "Bhanum", "Hollodur", "Bur Lodir", "Thirnburimm", "Thol Torum", "Negaldur", "Dug Darum", "Nilyaruhm", "Vuggrim", "Marndarihm", "Nornduhn", "Volbuldar", "Gughrigh", "Mam Faldir", "Gulkalduhr", "Kur Daruhm", "Kalrhia", "Bharoldur", "Bherulur", "Dhil Guruhm", "Homdum", "Meglodahr", "Marruhm", "Nertodur", "Mugtorhm", "Bhum Thurum", "Vug Moldur", "Hig Tharum", "Vil Wohrum", "Hel Loduhr", "Virn Moldir", "Thurlodar", "Kanulihm", "Bigduhr", "Melgolir", "Kol Lodar", "Khonkuldor", "Nulbuldor", "Durguruhm", "Gileduhr", "Damlodir", "Binahm", "Morrugh"]) 
cultures["Elven"].fill_names_lists(["Adran", "Aeler", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"], ["Adrie", "Althaea", "Anastrianna", "Audraste", "Antinua", "Berthrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"], ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Nailo", "Siannodel", "Xiloscient"], ["Sheherius", "O anor", "Nenelean", "Kela Alari", "Gafadell", "Esyana Serine", "Wserius", "Allrannoris", "Mytf Ennore", "Keathlin", "Caathlone", "Amantheas", "Y isari", "Alha Tirion", "Yeaserine", "Faenthemar", "Isyathaes", "Umve Unarith", "Sysrion", "Yi Dorei", "Asena Entheas", "Mythlathyr", "Olyvekadi", "Anmtheas", "Umyaena Allanar", "Esel Asari", "Nilnmelle", "Fahe Aiqua", "Asyannore", "Allve Shaeras", "Osmeshara", "Esseluma", "Yae Caelora", "Nefalenora", "Melltalos", "Illstalos", "Umynalin", "Theasari", "Onyhanaes", "Alren Tirion", "A ran Allanar", "Eyva Aethel", "Nilmalone", "Enana Tirion", "Unenoris", "Ollranmel", "Syla Alari", "Shyln Aethel", "Sletheas", "Illfalenor", "Ilagroth", "Ilyllean", "Fylne Thalor", "Theln Serin", "Alogroth", "Unyeth Thalor", "Umsshara", "Nilh Aiqua", "Kaneas", "Nilmemelle", "Hambelle", "Irath Tirion", "Hevaserin", "Cyslenor", "Asslenora", "Oshhe Ortheiad", "Inle Ancalen", "Ome Alari", "Iyanathemar", "Thyalthalas", "Omyslune", "Cyhe Aethel", "Sylholune", "Enye Unarith", "Sylren Serin", "Faenaes", "Shael Lenora", "Selalond", "Imyalion", "Fylanabel", "Lelvehona", "Amyethnaes", "Galvelune", "Ayel Ennore", "Arlanora", "Ulyo Taesi", "Nan Lenora", "Nythel Serine", "Ui Belanore", "Kyrannas", "Nylalluna", "Eynshara", "Imnadorei", "Jilahone", "Hyse Taesi", "Mythelnoris", "Thellarion", "Nh Alari", "Leaenanaes", "Mythrenluna"]) 
cultures["Halfling"].fill_names_lists(["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"], ["ndry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"], ["Brushgather", "Goodbarrel", "Greenbottle", "High-Hill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"], ["Halfling City"]) 
cultures["Gnomish"].fill_names_lists(["Alston", "Alvyn", "Boodynock", "Brocc", "Burgell", "Dimble", "Eldon", "Erky", "Fonkin", "Frug", "Gerbo", "Gimble", "Glim", "Jebeddo", "Kellen", "Namfoodle", "Orryn", "Roondar", "Seebo", "Sindri", "Warryn", "Wrenn", "Zook"], ["Bimpnottin", "Breena", "Caramip", "Carlin", "Donella", "Duvamil", "Ella", "Ellyjobell", "Ellywick", "Lilli", "Loopmottin", "Lorilla", "Mardnap", "Nissa", "Nyx", "Oda", "Orla", "Roywyn", "Shamil", "Tana", "Waywocket", "Zanna"], ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murning", "Ningel", "Raulnor", "Scheppen", "Timbers", "Turen"], ["Gnome City"]) 
cultures["Half-Elven"].fill_names_lists(["Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd", "Bor", "Fodel", "Glar", "Grogor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Melcer", "Stor", "Toman", "Urth", "Adran", "Aeler", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias", "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"], ["Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele", "Alethra", "Kara", "Katernin", "Mara", "Natali", "Olma", "Tana", "Zora", "Amafrey", "Betha", "Cefrey", "Kethra", "Olga", "Silifrey", "Westra", "Adrie", "Althaea", "Anastrianna", "Audraste", "Antinua", "Berthrynna", "Birel", "Caelynn", "Drusilia", "Enna", "Felosial", "Ielenia", "Jelenneth", "Keyleth", "Leshanna", "Lia", "Meriele", "Mialee", "Naivara", "Quelenna", "Quillathe", "Sariel", "Shanairra", "Shava", "Silaqui", "Theirastra", "Thia", "Vadania", "Valanthe", "Xanaphia"], ["Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag", "Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag", "Brightwood", "Helder", "Hornraven", "Stormwind", "Windrivver", "Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Nailo", "Siannodel", "Xiloscient"], ["Half-Elf City"]) 
cultures["Half-Orcish"].fill_names_lists(["Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd", "Bor", "Fodel", "Glar", "Grogor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor", "Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Melcer", "Stor", "Toman", "Urth", "Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Mhurren", "Ront", "Shump", "Thokk"], ["Arveene", "Esvele", "Jhessail", "Kerri", "Lureene", "Miri", "Rowan", "Shandri", "Tessele", "Alethra", "Kara", "Katernin", "Mara", "Natali", "Olma", "Tana", "Zora", "Amafrey", "Betha", "Cefrey", "Kethra", "Olga", "Silifrey", "Westra", "Baggi", "Emen", "Engong", "Kansif", "Myev", "Neegea", "Ovak", "Ownka", "Shautha", "Sutha", "Vola", "Volen", "Yevelda"], ["Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag", "Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag", "Brightwood", "Helder", "Hornraven", "Stormwind", "Windrivver"], ["Half-Orc City"]) 


Age_search_range = 5 
Wealth_search_range = 0.1 
children_leaving_odds = 80 
