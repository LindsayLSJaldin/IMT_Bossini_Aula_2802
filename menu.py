def menu():
    while True:
        opcao = input("\n1.Somar  2.Subtrair  3.Multiplicar  4.Dividir  0.Sair\nEscolha: ")
        if opcao == "0":
            print("Saindo...")
            break
        if opcao in "1234":
            try:
                a, b = float(input("Número 1: ")), float(input("Número 2: "))
                if opcao == "1": print(f"Resultado: {a + b}")
                elif opcao == "2": print(f"Resultado: {a - b}")
                elif opcao == "3": print(f"Resultado: {a * b}")
                elif opcao == "4": print(f"Resultado: {a / b if b != 0 else 'Erro: divisão por zero'}")
            except ValueError:
                print("Entrada inválida!")
        else:
            print("Opção inválida!")

menu()