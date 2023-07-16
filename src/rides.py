def offer_ride(caronas, usuarios):
    cpf = input('Digite seu CPF: ')
    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')

    carona = {
        'origem': origem,
        'destino': destino,
        'nome': usuarios[cpf]['nome'],
        'carro': usuarios[cpf]['carro']
    }

    caronas.append(carona)
    print('CORRIDA DIVULGADA COM SUCESSO!')


def search_ride(caronas):
    # cpf = input('Digite seu CPF: ')
    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')
    ride_found = []

    for key in caronas:
        if key['origem'] == origem and key['destino'] == destino:
            ride_found.append(key)
    j = 1
    if len(ride_found) > 0:
        print('Caronas encontradas: ')
        for i in ride_found:
            print(f'{j}- {i}')
            j += 1

    option = int(input('qual corona deseja ?: '))

    if ride_found[option - 1] == 0:
        print('opção inválida!')
        return

    else:
        print('Pedido concluído!')
