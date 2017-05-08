

# Lists used when generating all other objects
# Should be the only thing that require modification to create a new world type

# Sources:
#   Medieval demographics made easy By S. John Ross http://www222.pair.com/sjohn/blueroom/demog.htm
#   What did people do in a Medieval City? By Shawn Vincent http://www.svincent.com/MagicJar/Economics/MedievalOccupations.html



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

classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard', 'Expert', 'Warrior']


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




