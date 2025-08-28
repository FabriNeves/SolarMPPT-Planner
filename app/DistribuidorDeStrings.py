# A Joia da Coroa

def distribuir_strings(total_modulos, openCircuitVoltage, stringsPerMppt, voltageRangeMax, voltageRangeMin, inverterPower, modulePower):

    # Inicialização de variáveis
    totalStrings = 0
    modulos_restantes = total_modulos
    modulos_por_string_max = int(voltageRangeMax // openCircuitVoltage)
    modulos_por_string_min = int(voltageRangeMin // openCircuitVoltage)

    # print(f'Módulos por string máximo permitido: {modulos_por_string_max}')
    # print(f'Módulos por string mínimo permitido: {modulos_por_string_min}')

    # Calcular o total de strings disponíveis inicialmente
    for mppt in stringsPerMppt:
        totalStrings += stringsPerMppt[mppt]
    # print(f'Total de strings disponíveis inicialmente: {totalStrings}')

    # Calcular o máximo de módulos possíveis
    max_modulos_possiveis = totalStrings * modulos_por_string_max
    # print(f'Máximo de módulos possíveis com a configuração atual: {max_modulos_possiveis}')

    if total_modulos > max_modulos_possiveis:
        total_modulos = max_modulos_possiveis
        print(f'Total de módulos alterado para: {total_modulos}')
        modulos_restantes = total_modulos

    # Calcular a porcentagem de uso com base na potência do inversor
    porcentagem_uso = (total_modulos * modulePower / inverterPower*0.9) * 100
    # print(f"\nPorcentagem de módulos usados em relação ao máximo possível: {porcentagem_uso:.2f}%")

    if (porcentagem_uso > 100):
      porcentagem_uso = 100

    # Calcular a quantidade ideal de strings a serem usadas
    idealStrings = round((porcentagem_uso / 100) * totalStrings)
    if idealStrings < 1:
        idealStrings = 1  # Garantir que pelo menos uma string seja usada

    # print(f"Ideal de strings a serem usadas: {idealStrings}")

    # Ajustar o objeto stringsPerMppt com base na quantidade ideal de strings
    adjustedStringsPerMppt = {}
    total_count = 0

    # Ajustar o número de strings por MPPT até atingir o número ideal
    for mppt, num_strings in stringsPerMppt.items():
        if total_count + num_strings <= idealStrings:
            adjustedStringsPerMppt[mppt] = num_strings
            total_count += num_strings
        else:
            adjustedStringsPerMppt[mppt] = idealStrings - total_count
            break

    # print(f"Ajuste final de strings por MPPT: {adjustedStringsPerMppt}")

    # Recalcular o total de strings com o ajuste
    totalStrings = sum(adjustedStringsPerMppt.values())
    max_modulos_possiveis = totalStrings * modulos_por_string_max
    # print(f"\nNovo total de strings disponíveis: {totalStrings}")
    # print(f"Novo máximo de módulos possíveis: {max_modulos_possiveis}")

    # Recalcular a distribuição com o novo ajuste
    modulos_na_string = min(int(total_modulos / totalStrings), modulos_por_string_max)
    # print(f"\nDistribuição inicial de módulos por string: {modulos_na_string}")
    # print(f"Módulos restantes para distribuir: {modulos_restantes}")

    # Inicializar a distribuição de módulos com a nova configuração
    distrib = {mppt: [] for mppt in adjustedStringsPerMppt.keys()}

    for mppt, num_strings in adjustedStringsPerMppt.items():
        if modulos_restantes <= 0:
            break
        for _ in range(num_strings):
            modulos_atual = min(modulos_na_string, modulos_restantes)
            distrib[mppt].append(modulos_atual)
            modulos_restantes -= modulos_atual

        # print(f"\nEstado atual das strings para o MPPT '{mppt}': {distrib[mppt]}")
        # print(f"Módulos restantes após distribuir para o MPPT '{mppt}': {modulos_restantes}")

        # Adicionando a lógica para evitar loop infinito
    max_iterations = 7  # Definindo um limite máximo de iterações

    iteration_count = 0
    emEspera = 0

    while True:
        iteration_count += 1

        # Simular comportamento do 'do...while'
        if modulos_restantes <= 0:
            break

        if iteration_count > max_iterations:
            # print("Aviso: Atingido o limite máximo de iterações. Saindo do loop para evitar loop infinito.")
            break

        for mppt in distrib:
            if len(distrib[mppt]) == 0:  # Verifica se a lista está vazia
                continue

            # Distribuição de módulos quando a condição é atendida
            if (modulos_restantes - emEspera) % len(distrib[mppt]) == 0:
                for i in range(len(distrib[mppt])):
                    if modulos_restantes > 0 and distrib[mppt][i] < modulos_por_string_max:
                        distrib[mppt][i] += 1
                        modulos_restantes -= 1
                    if modulos_restantes == 0:
                        break



        # Verifica se não há mais módulos para distribuir
        emEspera += 1
        if modulos_restantes == 0:
            break

    # Ajustar as strings para garantir que todas tenham o mesmo número de módulos
    # print("\nAjustando todas as strings para ter o mesmo número de módulos...")
    for mppt in distrib:
        if distrib[mppt]:  # Verifica se a lista não está vazia
            min_modulos = min(distrib[mppt])  # Encontra o menor número de módulos nas strings desse MPPT
            distrib[mppt] = [min_modulos] * len(distrib[mppt])  # Define todas as strings para o menor valor

    # Verificar se as strings atendem ao voltageRangeMin
    # print("\nVerificando se as strings atendem ao voltageRangeMin...")
    for mppt, strings in distrib.items():
        # print(f"Verificando MPPT '{mppt}':")
        # print(f"Strings: {strings}")
        for i, num_modulos in enumerate(strings):
            total_voltage = num_modulos * openCircuitVoltage
            if total_voltage < voltageRangeMin:
                print(f"A string {i + 1} no MPPT '{mppt}' não atende à tensão mínima ({voltageRangeMin} V). Tensão total atual: {total_voltage} V")

    # print("\nDistribuição final dos módulos por MPPT:", distrib)
    # print(f"Módulos Excedentes: {modulos_restantes}")
    return distrib



