"""Filtra uma lista de dez nomes, ignorando os que começam com A."""

nomes = [
    "Ana",
    "Bruno",
    "Amanda",
    "Carlos",
    "Alice",
    "Daniela",
    "André",
    "Eduarda",
    "Arthur",
    "Fernanda",
]

print("=== Nomes que não começam com a letra A ===")

for nome in nomes:
    if nome.casefold().startswith("a"):
        continue

    print(nome)
