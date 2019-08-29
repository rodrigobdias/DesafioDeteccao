import random

class Desafio_Deteccao():
    """ Modelando a Classe Desafio_Deteccao"""

    def __init__(self, menor_valor_perfil=1, maior_valor_perfil=100, quantidade_elementos_perfil=80):
        """ Inicializa os atributos, por padrão,
            os valores de self._menor_valor_perfil,
            self._maior_valor_perfil e
            self._quantidade_elementos_perfil, serão carregados com 1, 100 e 80 respectivamente,
            esses valores podem ser configuráveis ao instanciar a classe.
        """
        self._perfil_valores = []
        self._finaliza = False
        self._menor_valor_perfil = menor_valor_perfil
        self._maior_valor_perfil = maior_valor_perfil
        self._quantidade_elementos_perfil = quantidade_elementos_perfil


    def carrega_perfil_valores_aleatoriamente(self):
        """ Por padrão, serão gerados 80 números aleatoriamente entre 1 a 100 (valores configuráveis) e salvo em self._perfil_valores. """
        self._perfil_valores = [random.randint(self._menor_valor_perfil, self._maior_valor_perfil) for contador in range(self._quantidade_elementos_perfil)]

    def __getitem__(self, item):
        return self._perfil_valores[item]

    @property
    def finaliza(self):
        return self._finaliza

    @finaliza.setter
    def finaliza(self, booleano):
        self._finaliza = booleano



if __name__== '__main__':

    desafio = Desafio_Deteccao()
    desafio.carrega_perfil_valores_aleatoriamente()

    print("Digite 'quit' para encerrar.\n")

    while not desafio.finaliza:

        resposta = input('Digite um valor: ')

        if resposta == 'quit':
            desafio.finaliza = True
        else:
            try:
                resultado = 'ok' if ( int(resposta) in desafio ) else 'Valor fora do espectro já recebido'
            except ValueError:
                print('Somente números inteiros serão aceitos.\n')
            else:
                print(resultado + "\n")