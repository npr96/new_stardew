from T2_Module import Bones


class Player:

    def __init__(self, wallet=0, location='home', start=0, name='', farm_name=''):
        self.wallet = wallet
        self.location = location
        self.start = start
        self.name = name
        self.farm_name = farm_name
        self.imp = ''


char_create = Bones.start()
player1 = Player(name=char_create[0], farm_name=char_create[1])


def engine(player):

    while True:
        try:
            player1.start = 1
            player1.name = char_create[0]
            player1.farm_name = char_create[1]
            player1.imp = Bones.input_parser(player1.farm_name)
            act_output = Bones.interpreter(player1.imp)
            player1.wallet = act_output[0]
            player1.location = act_output[1]
        except TypeError:
            pass


if __name__ == '__main__':
    engine(player1)
