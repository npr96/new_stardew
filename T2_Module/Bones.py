from T2_Module import Cutscene
from T2_Module import Dict


def start():
    char_creator = Cutscene.open_cutscene()
    return char_creator


def input_parser(farm_name):
    imp = input('-' + farm_name + '-')
    parsimp = imp.split()
    return parsimp


def interpreter(player_input, plocation, pwallet):
    try:
        result = dict_of_actions[player_input[0]](player_input, plocation, pwallet)
        return result
    except KeyError:
        print('Stardew didn\'t understand.')
    except IndexError:
        print()


def goto(player_input, _, pwallet):
    updater = [pwallet, player_input[-1]]
    print(Dict.dict_of_location[player_input[-1]])
    return updater


def inspect(player_input, plocation, _):
    try:
        print(Dict.dict_of_inspection[plocation][player_input[-1]])
    except KeyError:
        print('You can\'t inspect that (or can\'t inspect it from here)')


def buy(player_input, plocation, pwallet):
    try:
        pass
    except KeyError:
        print('that isn\'t being sold here')


dict_of_actions = {
    'go': goto,
    'inspect': inspect,
    'buy': buy,
}
