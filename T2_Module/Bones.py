from T2_Module import Cutscene


def start():
    char_creator = Cutscene.open_cutscene()
    return char_creator


def input_parser(farm_name):
    imp = input('-' + farm_name + '-')
    parsimp = imp.split()
    return parsimp


def interpreter(player_input):
    try:
        return dict_of_actions[player_input[0]]
    except KeyError:
        print('Stardew didn\'t understand.')
    except IndexError:
        print()


def goto():
    pass


dict_of_actions = {
    'go': goto(),
}
