print("=== Contador de vogais ===")
palavra = input("Digite uma palavra:")

#define vogais(incluindo maiusculas e minusculas e acentuadas)
vogais = "aeiouAEIOU"
contador = 0

# percorre cada letra da palavra informada
for letra in palavra:
    if letra in vogais:
        contador += 1

# Exibe o resultado final
print(f"A palavra '{palavra}' contém {contador} vogais.")