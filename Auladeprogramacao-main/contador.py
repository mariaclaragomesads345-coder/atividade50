lista_nomes = []

print("Digite 5 nomes:")
for i in range(5):
    nome = input(f"Nome {i + 1}: ")
    lista_nomes.append(nome)

    lista_nomes.sort()

    print("\nExibindo os nomes em ordem alfabetica:")


    for contador,nome in enumerate(lista_nomes,start=1):
        print(f"{contador} - {nome}")