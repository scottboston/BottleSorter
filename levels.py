from bottle import Bottle


def get_games(bottle_number: int, bottle_contents: dict, bottle_volume: int):
    """Create a list of bottles with the intial contents"""
    list_bottles = {}
    for i in range(1, bottle_number + 1):
        list_bottles[f'b{i}'] = Bottle(bottle_volume, f'b{i}')

    for b in list_bottles.values():
        if bottle_contents.get(b.name):
            for c in bottle_contents[b.name]:
                b.add_contents(c)
    return list_bottles


level_dict = {1: {'bottle_contents': {'b1': ['0'],
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
              4: {'bottle_contents': {'b1': [*'KYPP'],
                                      'b2': [*'PYPY'],
                                      'b3': [*'KPYK']},
                  'bottle_number': 5,
                  'bottle_volume': 4,
                  }
              }
