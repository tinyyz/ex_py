print("\33[1;35;40mAnálise de um Triângulo!\33[m")
lado1 = int(input("\33[1;36;40mInforme o 1º lado: \33[m"))
lado2 = int(input("\33[1;36;40mInforme o 2º lado: \33[m"))
lado3 = int(input("\33[1;36;40mInforme o 3º lado: \33[m"))

if (lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1 ):
    if(lado1==lado2 and lado1==lado3):
        print("\33[1;35;40mTriângulo Equilátero!\33[m")
    elif (lado1==lado2 or lado1==lado3 or lado2==lado3):
        print("\33[1;35;40mTriângulo Isóceles!\33[m")
    else:
        print("\33[1;35;40mTriângulo Escaleno!\33[m")       
else:
    print("\33[1;31;40mOs lados não formam um triângulo.\33[m")