def calculadora():
    while True:
        print("Escolha a operação desejada:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = int(input("Digite o número da operação: "))

        if opcao == 0:
            print("Saindo da calculadora...")
            break

        if opcao not in range(1, 5):
            print("Opção inválida.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = num1 + num2
        elif opcao == 2:
            resultado = num1 - num2
        elif opcao == 3:
            resultado = num1 * num2
        else:  # opcao == 4
            if num2 == 0:
                print("Divisão por zero não permitida.")
            else:
                resultado = num1 / num2

        print("Resultado:", resultado)

calculadora()
