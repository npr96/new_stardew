from T2_Module import Dict


def open_cutscene():
    name = input('Welcome to Stardew Valley, what is your name?: ')
    Dict.dict_of_flags['Open cutscene'] = 1
    print(Dict.dict_of_open_cutscene[1])
    _ = input('press [enter] to continue')
    print(Dict.dict_of_open_cutscene[2])
    _ = input('press [enter] to continue')
    print('Lewis: ' + name + Dict.dict_of_open_cutscene[3])
    _ = input('press [enter] to continue')
    print(Dict.dict_of_open_cutscene[4])
    power_switch = 1
    while power_switch == 1:
        res = input('''1. let\'s go!
    2. Who are you?
    : ''')
        if res == '1':
            break
        elif res == '2':
            print(Dict.dict_of_open_cutscene[5])
            power_switch2 = 1
            while power_switch2 == 1:
                res2 = input('''
    1. I remember!
    2. I'm sorry...
    : ''')
                if res2 == '1':
                    print(Dict.dict_of_open_cutscene[6])
                    break
                elif res2 == '2':
                    print(Dict.dict_of_open_cutscene[7])
                    break
                else:
                    print('Stardew didn\'t understand, please type 1 or 2')
                    continue
            break
        else:
            print('Stardew didn\'t understand, please type 1 or 2')
            continue
    print(Dict.dict_of_open_cutscene[8])
    power_switch3 = 1
    while power_switch3 == 1:
        res3 = input('What would you like to do?: ')
        if res3 == 'go to farm' or res3 == 'go farm':
            break
        else:
            print('''please type go to farm (or go farm) to follow Lewis''')
            continue
    print(Dict.dict_of_open_cutscene[9])
    _ = input('press [enter] to continue')
    print(Dict.dict_of_open_cutscene[10])
    _ = input('press [enter] to continue')
    print(Dict.dict_of_open_cutscene[11])
    farm_name = input('I think the name was... : ')
    print('Lewis: ' + farm_name + Dict.dict_of_open_cutscene[12])
    _ = input('press [enter] to continue')
    print(Dict.dict_of_open_cutscene[13])
    result = [name, farm_name]
    return result
