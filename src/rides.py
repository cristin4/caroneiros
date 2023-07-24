# ----------------------- Oferecer ----------------------- #
def offer_ride(caronas, usuarios, id_carona, quant_avaliacao, quant_usuarios):
    cpf = input('Digite seu CPF: ')
    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')
    vagas = int(input("Digite o número de vagas disponíveis: "))
    valor = input("Digite o valor necessário de contribuição para gasolina: ")

    try:
        nova_carona = {
            'id': id_carona,
            'origem': origem,
            'destino': destino,
            'cpf': usuarios[cpf]['cpf'],
            'nome': usuarios[cpf]['nome'],
            'carro': usuarios[cpf]['carro'],
            'vagas': vagas,
            'valor': float(valor),
            'avaliacao': float(quant_avaliacao),
            'quant_usuarios': int(quant_usuarios)
        }
    except KeyError:
        print("CPF não encontrado! Tente de novo ou cadastre-se!")
        return

    caronas[id_carona] = nova_carona

    print('Corrida cadastrada com sucesso!\n')


# ----------------------- Procurar ----------------------- #
def search_ride(caronas, usuarios):
    cpf = input('Digite seu CPF: ')
    origem = input('Digite a origem: ')
    destino = input('Digite o destino: ')
    vagas = int(input("Quantas vagas você precisa? "))
    caronas_encontradas = []

    for carona in caronas:
        if caronas[carona]['origem'] == origem and caronas[carona]['destino'] == destino and caronas[carona]['vagas'] \
                >= vagas:
            caronas_encontradas.append(carona)

    if len(caronas_encontradas) == 0:
        print('Nenhuma carona compatível encontrada.')
        return
    else:
        j = 1
        print('Caronas encontradas: ')
        for carona in caronas_encontradas:
            print(f'{j}- {caronas[carona]}')
            j += 1

    opcao = int(input('Qual carona deseja? '))

    if caronas_encontradas[opcao - 1] == 0:
        print('Opção inválida!')
        return

    else:
        id_carona = caronas_encontradas[opcao - 1]
        opcao_pagamento = int(input("Qual o método de pagamento da contribuição?\n"
                                    + "1 - Carteira\n" + "2 - Outros (Dinheiro, cartão, pix)\n"))
        if opcao_pagamento == 1:
            if usuarios[cpf]['carteira'] >= caronas[id_carona]['valor'] * vagas:
                usuarios[cpf]['carteira'] -= caronas[id_carona]['valor'] * vagas
                usuarios[caronas[id_carona]['cpf']]['carteira'] += caronas[id_carona]['valor'] * vagas
            else:
                print("Valor na carteira insuficiente! Alterando para outras formas de pagamento...")

        usuarios[cpf]['historico'][id_carona] = caronas[id_carona]
        usuarios[caronas[id_carona]['cpf']]['historico'][id_carona] = caronas[id_carona]
        usuarios[caronas[id_carona]['cpf']]['historico'][id_carona]['quant_usuarios'] += 1
        if vagas == caronas[id_carona]['vagas']:
            caronas.pop(id_carona)
            print("Carona totalmente preenchida! Acerte os detalhes com o motorista!")
        else:
            caronas[id_carona]['vagas'] -= vagas
            print("Esse carona ainda tem vagas, verifique com o motorista se ele vai aguardar ou já irá iniciar!")

        print('Pedido de carona concluído!\n')


# ----------------------- Sugerir ----------------------- #
def suggested_ride(carona_sugerida, id_carona):
    origem = input("Qual origem da carona que deseja sugerir? ")
    destino = input("Qual destino da carona que deseja sugerir? ")
    vagas_desejadas = int(input("Quantas vagas deseja? "))
    nova_carona_sugerida = {
        'id': id_carona,
        'origem': origem,
        'destino': destino,
        'vagas': vagas_desejadas
    }
    carona_sugerida[id_carona] = nova_carona_sugerida


# ----------------------- Adquirir sugestão ----------------------- #
def confirm_ride(carona_sugerida, caronas, usuarios):
    print("lista de caronas sugeridas pelo usuários:")

    j = 1
    print('Caronas encontradas: ')
    for carona in carona_sugerida:
        print(f'{j}- {carona_sugerida[carona]}')
        j += 1

    confirm = input("Gostaria de adquirir alguma sugestão?[S/N] ")
    confirm = confirm.lower()
    if confirm == 'n':
        return
    elif confirm == 's':
        number = int(input("Informe qual número da carona que gostaria de adquirir: "))
        cpf = input("Informe seu CPF: ")
        valor = float(input("Digite o valor necessário de contribuição para gasolina: "))
        option = input("Gostaria de alterar a quantidade de vagas?[S/N] ")
        option = option.lower()
        if option == 's':
            nova_vagas = int(input("Quantas vagas deseja oferecer: "))
            carona_sugerida[number]['vagas'] = nova_vagas

        caronas[number] = carona_sugerida[number]

        caronas[number]['cpf'] = usuarios[cpf]['cpf']
        caronas[number]['carro'] = usuarios[cpf]['carro']
        caronas[number]['valor'] = valor

        carona_sugerida.pop(number)


# ----------------------- Avaliação ----------------------- #
def rate_ride(usuarios, quant_avaliacao, caronas):
    cpf = input("Digite o CPF do usuário para verificar caronas sem avaliação: ")
    caronas_encontradas = []

    for carona in usuarios[cpf]['historico']:
        if usuarios[cpf]['historico'][carona]['quant_usuarios'] > 0:
            caronas_encontradas.append(carona)

    if len(caronas_encontradas) == 0:
        print('Nenhuma carona sem avaliação encontrada.')
        return
    else:
        j = 1
        print('Caronas sem avaliação: ')
        for carona in caronas_encontradas:
            print(f'{j}- {usuarios[cpf]["historico"][carona]}')
            j += 1

    opcao = int(input('Qual carona deseja avaliar? '))

    if caronas_encontradas[opcao - 1] == 0:
        print('Opção inválida!')
        return
    else:
        id_carona = caronas_encontradas[opcao - 1]
        nota = float(input("Digite a nota para essa carona, de 1 a 5: "))
        cpf_motorista = usuarios[cpf]['historico'][id_carona]['cpf']
        if quant_avaliacao == 1:
            usuarios[cpf_motorista]['historico'][id_carona]['avaliacao'] = nota
        else:
            nota += usuarios[cpf_motorista]['historico'][id_carona]['avaliacao']
            nota = nota / quant_avaliacao
            usuarios[cpf_motorista]['historico'][id_carona]['avaliacao'] = nota
        usuarios[cpf]['historico'][id_carona]['quant_usuarios'] -= 1
        print("Avaliação registrada com sucesso!")
