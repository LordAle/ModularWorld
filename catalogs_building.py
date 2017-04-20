import catalogs_city

kinds = ['House', 'Service', 'Shop', 'Workshop', 'Castle', 'Religious', 'Education', 'Military', 'Criminal', 'Art',
         'Other']


# Each kind is a key associated with a list of lists, each list contains [subkind, min_city_size, relative weight]
subkinds = {'House': [['Farmer',0,20],
                      ['Commoner',0,10],
                      ['Bourgeois',0,2],
                      ['Noble',1,1]],
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
            'Castle': [['Keep',0,1],
                       ['Castle',2,100]],
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

kinds_all = ['House (Noble)', 'House (Bourgeois)', 'House (Commoner)', 'House (Farmer)',
             'Service (Inn)', 'Service (Tavern)', 'Service (Museum)', 'Service (Hospital)', 'Service (Whorehouse)',
             'Service (Other)',
             'Shop (General)', 'Shop (Food)', 'Shop (Health)', 'Shop (Book)', 'Shop (Magic)', 'Shop (Luxury)', 'Shop (Resource)',
             'Workshop (Blacksmith)', 'Workshop (Tailor)', 'Workshop (Leatherwork)', 'Workshop (Woodwork)', 'Workshop (Other)',
             'Castle (Keep)', 'Castle (Castle)',
             'Religious (Shrine)', 'Religious (Monastery)', 'Religious (Church)', 'Religious (Cathedral)',
             'Education (School)', 'Education (University)',
             'Military (Barrack)', 'Military (Prison)', 'Military (Fortress)',
             'Other (Thieves Den)', 'Other (Artists Guild)', 'Other (Circus)', 'Other (Homeless)',
             'Other (Army)', 'Other (Ship)']

kinds_0 = ['House (Commoner)', 'House (Farmer)',  'Service (Tavern)', 'Shop (General)', 'Shop (Food)',
           'Shop (Resource)', 'Workshop (Blacksmith)', 'Workshop (Tailor)', 'Workshop (Leatherwork)', 'Workshop (Woodwork)',
           'Workshop (Other)', 'Castle (Keep)', 'Religious (Shrine)', 'Religious (Monastery)', 'Other (Thieves Den)', 'Other (Homeless)']

kinds_1 = kinds_0 + ['House (Noble)', 'House (Bourgeois)', 'Service (Inn)', 'Service (Hospital)', 'Service (Whorehouse)',
                     'Shop (Health)',  'Shop (Luxury)', 'Religious (Church)', 'Military (Barrack)', 'Military (Prison)',
                     'Other (Artists Guild)', 'Other (Circus)']

kinds_2 = kinds_1 + ['Shop (Book)', 'Shop (Magic)', 'Service (Other)', 'Castle (Castle)', 'Religious (Cathedral)',
                           'Education (University)', 'Military (Fortress)']

kinds_3 = kinds_2 + ['Service (Museum)', ]

kinds_old = {catalogs_city.kinds[0]:kinds_0,
         catalogs_city.kinds[1]:kinds_1,
         catalogs_city.kinds[2]: kinds_2,
         catalogs_city.kinds[3]: kinds_3}

