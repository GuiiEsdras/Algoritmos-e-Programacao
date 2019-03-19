crimeDelator = input()

VCDOR = 0

if (crimeDelator != 'roubo' and crimeDelator != 'tráfico' and crimeDelator != 'homicídio'):
    print('Crime inválido.')

else:
    if (crimeDelator == 'roubo' or crimeDelator == 'tráfico'):
        valorCrimeDelator = float(input())
        VCDOR = valorCrimeDelator
        crimeDelato = input()
    else:
        crimeDelato = input()

    if (crimeDelato != 'roubo' and crimeDelato != 'tráfico' and crimeDelato != 'homicídio'):
        print('Crime inválido.')

    else:
        VCDO = 0
    if (crimeDelato == 'roubo' or crimeDelato == 'tráfico'):
        valorCrimeDelatado = float(input())
        VCDO = valorCrimeDelatado
    if (crimeDelato == 'roubo' or crimeDelato == 'tráfico' or crimeDelato == 'homicídio'):

        if ((crimeDelator == 'roubo' or crimeDelator == 'tráfico') and (crimeDelato == 'homicídio')):
            print('Delação concedida.')
        elif ((crimeDelator == 'roubo' and crimeDelato == 'roubo') and VCDO > (5 * VCDOR)):
            print('Delação concedida.')
        elif ((crimeDelator == 'roubo' and crimeDelato == 'tráfico') and VCDO > (3 * VCDOR)):
            print('Delação concedida.')
        elif ((crimeDelator == 'tráfico' and crimeDelato == 'tráfico') and VCDO > (5 * VCDOR)):
            print('Delação concedida.')
        elif (crimeDelator == 'homicídio' and crimeDelato == 'homicídio'):
            print('Delação concedida.')
        else:
            print("Delação rejeitada.")