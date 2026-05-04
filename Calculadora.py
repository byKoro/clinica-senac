import utilidades as ut
from utilidades import cores as cr
def media_de_velocidade():
    distancia = int(input("Digite a distância"))
    tempo = int(input("Digite o tempo"))
    velocidade = distancia / tempo
    return velocidade
resultado = media_de_velocidade()
print(f"{cr.amarelo}A velocidade média é: {resultado}")
