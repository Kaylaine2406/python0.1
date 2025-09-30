#Faça um programa que receba a idade do Usuário e verifique se a idade se a idade é maoir oou igual a 18 anos
def verificar_idade(idade):
        if idade >=18:
            return "você é maior de idade."
        else:
            return "você não é maoir de idade"

idade = int(input("digite sua idade"))

resultado = verificar_idade(idade)
print(resultado)