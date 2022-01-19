import random

R_EATING = "Eu não posso comer nada, pois eu sou apenas um robo"


def unknown():
    response = ['Poderia reformular a pergunta por favor?',
                "...",
                "Ah entendi",
                "O que isso significa?"][random.randrange(4)]
    return response