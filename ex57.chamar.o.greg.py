import os
perguntas = ["Telefonou para a vítima?","Esteve no local do crime?","Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?"]
veredito = 0

for i in range (0,5):
    print(perguntas[i], "\n[S] - Sim\n[N] - Não\n")
    resposta = input()
    os.system('cls')
    if resposta != "":
        if resposta == "s" or resposta == "S":
            veredito = veredito+1
            continue
        elif resposta == "n" or resposta == "N":
            continue

if veredito >=0 and veredito < 2:
    print("Você é Inocente!")
elif veredito == 2:
    print("Você é Suspeito(a)!")
elif veredito == 3 or veredito == 4:
    print("Você é Cúmplice!")
else:
    print("Você é o(a) Assasino(a)!")