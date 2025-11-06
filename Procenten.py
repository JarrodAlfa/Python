# hoeveel is x% van y
# hoevel % is x van y
# x neemt toe met y%
# x neemt af met y%
# x is toegenomen naar y (met hoeveel procent is het toegenomen)
# x is afgenomen naar y (met hoeveel procent is het afgenomen)
# x neemt toe met y% en is nu z (wat was x eerst)
# x neemt af met y% en is nu z (was was x eerst)

print('[1] hoeveel is X% van Y')
print('[2] hoeveel % is X van Y')
print('[3] X neemt toe met Y%')
print('[4] X neemt af mey Y%')
print('[5] X is toegenomen naar Y (met hoeveel procent is het toegenomen)')
print('[6] X is afgenomen naar Y (met hoeveel procent is het afgenomen)')
print('[7] Z neemt toe met X% en is nu Y (wat was x eerst)')
print('[8] Z neemt af met X% en is nu Y (wat was x eerst)')
print('')

_input = int(input('Welk procenten som wil jij oplossen?: '))

match _input:
    case 1:
        # hier vraag ik om de values van X en Y
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        _Oplossing = _X / 100 * _Y

        # hier voer ik de som uit
        print('')
        print(f'{_X}% van {_Y} = {_Oplossing}')
        print(f'De berekening is {_X} : 100 x {_Y} = {_Oplossing}')
    case 2:
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        _Oplossing = _X / _Y

        print('')
        print(f'{_X} is {round(_Oplossing * 100, 2)}% van {_Y}')
        print(f'De berekening is {_X} : {_Y} = {round(_Oplossing * 100, 2)}')
    case 3:
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        _Oplossing = _X * ((_Y / 100) + 1)
        print('')
        print(f'Het antwoord is {_Oplossing}')
        print(f'De berekening is {((_Y / 100) + 1)} x {_X} = {_Oplossing}')
    case 4:
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        _Oplossing = (1 - (_Y / 100)) * _X

        print('')
        print(f'Het antwoord is {_Oplossing}')
        print(f'De berekening is {(1 - (_Y / 100))} x {_X} = {_Oplossing}')
    case 5:
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        # y / x = z. z - 1 x 100
        _Oplossing = _Y / _X

        print('')
        print(f'Het antwoord is {((round(_Oplossing, 2) - 1) * 100)}%')
        print(f'De berekening is {_Y} : {_X} = {round(_Oplossing, 2)} - 1 x 100 = {((round(_Oplossing, 2) - 1) * 100)}%')
    case 6:
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        # x / y = z. 1 - z x 100
        _Oplossing = (1 - (_X / _Y)) * 100

        print('')
        print(f'Het antwoord is {round(_Oplossing, 2)}%')
        print(f'De berekening is 1 - {round(_X / _Y, 2)} = {round(1 - (_X / _Y), 2)} * 100 = {round(_Oplossing, 2)}%')
    case 7:
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        _Oplossing = _Y / ((_X / 100) + 1)

        print('')
        print(f'Het antwoord is {round(_Oplossing, 2)}')
        print(f'De brekening is {_Y} : (({_X} / 100) + 1) = {((_X / 100) + 1)} = {round(_Oplossing, 2)}')
    case 8:
        _X = int(input('Toets je X in: '))
        _Y = int(input('Toets je Y in: '))

        _Oplossing = _Y / (1 - (_X / 100))

        print('')
        print(f'Het antwoord is {round(_Oplossing, 2)}')
        print(f'De berekening is {_Y} : (1 - ({_X} / 100) = {round(_Oplossing, 2)})')