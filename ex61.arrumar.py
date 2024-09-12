nota = []

for i in range (4):
    nota.append(float(input(f"Informe a {i+1}ª nota: ")))

media = sum(nota)/4
print(f"A média das notas é {media}")

for i in range (4):
  if (nota[i] >= media):
    print (f"A nota {nota[i]} é maior ou igual a média")