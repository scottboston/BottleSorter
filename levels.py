from bottle import Bottle


def get_games(bottle_number: int, bottle_contents: dict, bottle_volume: int) -> dict:
    """Create a dictionary of bottles with the initial contents defined by level_dict"""
    dict_bottles = {}
    for i in range(1, bottle_number + 1):
        dict_bottles[f'b{i}'] = Bottle(bottle_volume, f'b{i}')

    for b in dict_bottles.values():
        if bottle_contents.get(b.name):
            for c in bottle_contents[b.name]:
                b.add_contents(c)
    return dict_bottles


level_dict = {1: {'bottle_contents': {'b1': ['O'],
                                      'b2': [*'OO']},
                  'bottle_number': 2,
                  'bottle_volume': 3},
              2: {'bottle_contents': {'b1': [*'BOBO'],
                                      'b2': [*'OBOB']},
                  'bottle_number': 3,
                  'bottle_volume': 4,
                  },
              3: {'bottle_contents': {'b1': [*'BORB'],
                                      'b2': [*'OORB'],
                                      'b3': [*'RBOR']},
                  'bottle_number': 5,
                  'bottle_volume': 4,
                  },
              4: {'bottle_contents': {'b1': [*'BROO'],
                                      'b2': [*'BRBR'],
                                      'b3': [*'OBRO']},
                  'bottle_number': 5,
                  'bottle_volume': 4,
                  },
              5: {'bottle_contents': {'b1': 'NG O B PK'.split(),
                                      'b2': 'O NG B PK'.split(),
                                      'b3': 'PK R O R'.split(),
                                      'b4': 'O PK R B'.split(),
                                      'b5': 'NG NG R B'.split()},
                  'bottle_number': 7,
                  'bottle_volume': 4},
              6: {'bottle_contents': {'b1': 'R NG NG NG'.split(),
                                      'b2': 'O R PK NG'.split(),
                                      'b3': 'PK O R O'.split(),
                                      'b4': 'B PK O PK'.split(),
                                      'b5': 'B B B R'.split()},
                  'bottle_number': 7,
                  'bottle_volume': 4},
              }
