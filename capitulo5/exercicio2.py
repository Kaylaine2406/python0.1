def resultadoFinal(numSomandos,valentia):
    return (f"Somandos todos os valores e subtraindo por 10 o resultado é {numSomandos - valentia}")

num1 = int(input("digite um numero"))
num2 = int(input("digite outro numero"))
num3 = int(input("digite mais um numero"))
num4 = int(input("digite o último numero"))

numSomandos = (num1 + num2 + num3 + num4)
valentia = 10

resultadoFinal(numSomandos,valentia)