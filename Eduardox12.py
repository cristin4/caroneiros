def offer_ride(list_ride, usuarios):
    cpf = input('Digite seu CPF: ')
    if cpf not in usuarios:
        print('CPF não encontrado.')
        return

    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')
    valor = int(input('Digite o valor da corona: '))

    carona = {
        'origem': origem,
        'destino': destino,
        'nome': usuarios[cpf]['nome'],
        'carro': usuarios[cpf]['carro'],
        'valor' : valor
    }

    list_ride.append(carona)
    print('CARONA DIVULGADA COM SUCESSO!')


def search_ride(list_ride, usuarios):
    cpf = input('Digite seu CPF: ')
    if cpf not in usuarios:
        print('CPF não encontrado.')
        return

    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')

    ride_found = []
    for ride in list_ride:
        if ride['origem'] == origem and ride['destino'] == destino:
            ride_found.append(ride)

    if not ride_found:
        print('Nenhuma carona encontrada.')
        return

    print('Caronas encontradas:')
    for i, ride in enumerate(ride_found, start=1):
        print('='*30)
        print(f'({i})')
        print(f"Origem: {ride['origem']}")
        print(f"Destino: {ride['destino']}")
        print(f"Nome: {ride['nome']}")
        print(f"Carro: {ride['carro']}")
        print(f"Valor da viagem: R${ride['valor']}")
        print('='*30)
        

    option = int(input('Qual carona deseja? (Digite o número correspondente): '))
    if option < 1 or option > len(ride_found):
        print('Opção inválida!')
        return

    selected_ride = ride_found[option - 1]
    print('='*30)
    print('Pedido concluído!')
    print('='*30)

    print('Carona selecionada: ')
    print(f"Origem: {selected_ride['origem']}")
    print(f"Destino: {selected_ride['destino']}")
    print(f"Nome: {selected_ride['nome']}")
    print(f"Carro: {selected_ride['carro']}")
    print(f"Valor da viagem: R${selected_ride['valor']}")
    print('='*30)
