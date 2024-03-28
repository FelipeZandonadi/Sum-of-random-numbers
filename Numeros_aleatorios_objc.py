from random import randint as r
import numpy as np


class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def Insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida!')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = valor
        self.ultima_posicao += 1

    def Excluir(self):
        if self.ultima_posicao == -1:
            return -1
        temp = self.valores[0]
        for i in range(0, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]
        self.ultima_posicao -= 1
        return temp


class Numbers:

    def __init__(self, valores, sorteios, somas=-1):
        self.quantidade = int(valores)

        self.sorteios = int(sorteios)

        self.somas = int(somas)
        if somas <= 0:
            self.somas = 1

        self.quantidade_de_valores = VetorOrdenado(sorteios)

    # Esta função computa os valores sorteados e faz todos os calculos nescessarios.
    def Computer(self):
        # 1º Etapa: Sorteio
        # Ele ira retornar 'self.sorteios' numeros aleatorios sorteados somados, que serão somados self.somas vezes.
        for _ in range(self.sorteios):
            numero = 0
            for _ in range(self.somas):
                num = r(0, self.quantidade)
                numero += num
            # Na linha abaixo ele insere em um vetor ordenado o número sorteado somado.
            self.quantidade_de_valores.Insere(numero)

        # 2º Etapa: Imprime
        # Ele imprime, o 'for' é limitado pelo números de colunas que devem ser criados.
        for i in range(self.somas * self.quantidade + 1):
            k = 0
            # se o primeiro número do vetor não for o da coluna então K recebe 0
            if self.quantidade_de_valores.valores[0] != i:
                k = 0
            else:
                # Se ele passar significa que o primeiro número é o número da coluna ('i')
                # Este 'while' ira repitir x vezes, até que todos os números iguais a coluna ('i') forem removidos (que estão em ordem)
                # E indicara através da variavel k quantas vezes foi removido, para ser mostrada no gráfico.
                while True:
                    # Registra qual número foi removido em temp.
                    temp = self.quantidade_de_valores.Excluir()
                    # se o valor de temp for igual a -1 então quer dizer que todos os números do vetor já foi removido (Fim do programa)
                    if temp == -1:
                        break
                    # K é adicionada + 1 para comtabilizar que mais um número foi removido (isso representa uma '#' do gráfico)
                    k += 1
                    # Verifica se o próximo número do vetor ainda corresponde ao número da coluna ('i')
                    if self.quantidade_de_valores.valores[0] != i:
                        break

            # apenas uma forma para facilitar a vizualização
            # Perceba que o que muda é estes espaços: |f'{i}     :'| --> |f'{i}:'|
            # Muda confome a quantidade de caracteres.
            if i < 10:
                print(f'{i}     :', '\033[1;33mX' * k+'\033[m', f'  {k}')
            elif 10 <= i < 100:
                print(f'{i}    :', '\033[1;33mX' * k+'\033[m', f'  {k}')
            elif 100 <= i < 1000:
                print(f'{i}   :', '\033[1;33mX' * k+'\033[m', f'  {k}')
            elif 1000 <= i < 10000:
                print(f'{i}  :', '\033[1;33mX' * k+'\033[m', f'  {k}')
            elif 10000 <= i < 100000:
                print(f'{i} :', '\033[1;33mX' * k+'\033[m', f'  {k}')
            else:
                print(f'{i}:', '\033[1;33mX' * k+'\033[m', f'  {k}')


Number = Numbers(5, 100, 3)
Number.Computer()
