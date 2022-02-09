#import numpy as np
import random
kanji_num = 0
#kanji_lista1 = list()
#kanji_lista2 = list()
kanji_lista_lista = [list()]

def main():

    class Kanji:
        def __init__(self,stg,kun,on,traducao, utilizar):
            self.stg = stg
            self.kun = kun
            self.on = on
            self.leitura = list()
            self.leitura.extend(kun)
            self.leitura.extend(on)
            self.traducao = traducao

            global kanji_num
            kanji_num += 1
            self.num = kanji_num
            utilizar = utilizar

            if utilizar == '1':
                '''global kanji_lista1
                kanji_lista1.append(self)
                '''
                global kanji_lista_lista
                for lista in kanji_lista_lista:
                    if len(lista) < 100:
                        lista.append(self)
                        if len(lista) == 100:
                            kanji_lista_lista.append(list())

                        break

            # 1,一,k,いち,o,ひと,s,1,u,1
            organizador = '{},{},k'.format(self.num, stg)
            for kun1 in self.kun:
                organizador += ','+ kun1
            organizador += ',o'
            for on1 in self.on:
                organizador += ',' + on1
            organizador += ',s,' + self.traducao + ',u,' + utilizar + '\n'
            with open('kanjis.txt', 'a', encoding='utf8') as f:
                f.write(organizador)
                print(f'{stg} salvo{kanji_num} k:{kun} o:{on}')

            '''organizador = '{},{},{},{},{}\n'
            with open('kanjis.txt', 'a', encoding='utf8') as f:
                f.write(organizador.format(self.num , stg, leitura, traducao, utilizar))
                print(stg, ' salvo.', str(kanji_num))'''

        def dic(self):
            print(f'''
        {self.num}    {self.stg}
            k: {self.kun} o: {self.on}
            traduçao: {self.traducao}''')
            #np.savetxt('kanjis.txt', [stg, leitura, traducao])


    def novokanji():
        novokanji_stg = str()
        novokanji_kun = list()
        novokanji_on = list()
        novokanji_sig = str()
        novokanji_usar = str()

        print('kanji:')
        novokanji_stg = str(input())
        print('kun:')
        while 1:
            novokanji_kun1 = input()
            if novokanji_kun1 == '':
                break
            else:
                novokanji_kun.append(novokanji_kun1)
        print('on:')
        while 1:
            novokanji_on1 = input()
            if novokanji_on1 == '':
                break
            else:
                novokanji_on.append(novokanji_on1)
        print('significado:')
        novokanji_sig = input()

        novokanji_usar = input()
        if novokanji_usar == 'n':
            novokanji_usar = '0'
        else:
            novokanji_usar = '1'
        Kanji(novokanji_stg, novokanji_kun, novokanji_on, novokanji_sig, novokanji_usar)

        '''print('kanji:')
        nome = str(input())
        print('leitura:')
        leitura = str(input())
        print('tradução:')
        traducao = str(input())
        usar = input()
        if usar == 'n':
            usar = 0
        else:
            usar = 1

        Kanji(nome, leitura, traducao, usar)
        '''

    def dicionario():

        def buscar(item, tag):
            retorno = list()
            for lista in kanji_lista_lista:
                if tag == 'stg':
                    for kanji in lista:
                        if kanji.stg == item:
                            retorno.append(kanji)
                elif tag == 'kun':
                    for kanji in lista:
                        if kanji.kun == item or item in kanji.kun:
                            retorno.append(kanji)
                elif tag == 'on':
                    for kanji in lista:
                        if kanji.on == item or item in kanji.on:
                            retorno.append(kanji)
                elif tag == 'traducao':
                    for kanji in lista:
                        if kanji.traducao == item:
                            retorno.append(kanji)
            return retorno

        #selecionar uma lista expecifica, ou procurar por um kanji nas listas
        print('Listas(lista) (procurar)')
        while 1:
            resposta = input()
            ## Selecionar
            if resposta == 'lista':
                print(f'Selecione a lista: entre 0 e {len(kanji_lista_lista) - 1}')
                listaSelecionada= int(input())
                atual = 0
                while 1:
                    print(listaSelecionada)
                    kanji_lista_lista[listaSelecionada][atual].dic()

                    comando = input()
                    if comando == 's':
                        atual += 1

                        if atual == 100:
                            atual = 0
                            listaSelecionada += 1
                            if listaSelecionada > len(kanji_lista_lista) - 1:
                                listaSelecionada = 0
                        continue

                    elif comando == 'a':
                        atual -= 1

                        if atual == -1:
                            listaSelecionada -= 1
                            atual = len(kanji_lista_lista[listaSelecionada]) - 1
                        continue
                    elif comando == 'q':
                        break
            elif resposta == 'procurar':
                print('Item')
                item = input()
                print('Tag (kun,on,stg,traducao)')
                tag = input()
                respostas  = buscar(item,tag)

                print(f'foram encontradas {len(respostas)} respostas')
                if respostas == list():
                    input()
                else:
                    n = 1
                    while 1:
                        respostas[n].dic()
                        comando = input()

                        if comando == 'a':
                            n -= 1
                            if n < 0:
                                n = len(respostas) - 1
                        elif comando == 'q':
                            break
                        else:
                            n += 1
                            if n == len(respostas):
                                n = 0
            break


##### Leitura dos kanjis
    with open('kanjis.txt', encoding='utf8') as f:
        linhas_lista = f.read().split('\n')
    with open('kanjis.txt','w') as f:
        f.write(' ')
    for linhas in linhas_lista:
        if linhas == '' or linhas == ' ':
            pass
        else:
            dados = linhas.split(',')
            dado_atual = 0
            dado_tipo = str()

            kanji_stg = str()
            kanji_kun = list()
            kanji_onn = list()
            kanji_sig = str()
            kanji_usar = str()

            for dado in dados:
                if dado_atual == 0:
                    pass
                elif dado_atual == 1:
                    kanji_stg = dado
                elif dado == 'k':
                    dado_tipo = 'k'
                elif dado == 'o':
                    dado_tipo = 'o'
                elif dado == 's':
                    dado_tipo = 's'
                elif dado == 'u':
                    dado_tipo = 'u'

                elif dado_tipo == 'k':
                    kanji_kun.append(dado)
                elif dado_tipo == 'o':
                    kanji_onn.append(dado)
                elif dado_tipo == 's':
                    kanji_sig = dado
                elif dado_tipo == 'u':
                    kanji_usar = dado
                dado_atual += 1
            Kanji(kanji_stg, kanji_kun, kanji_onn, kanji_sig, kanji_usar)
            #Kanji( dados[1], dados[2], dados[3], dados[4])

# Rodando o Programa
    parar = False
    while not parar:
        print('(teste) (novo kanji) (dicionario)')
        resp = input()
        if resp == 'novo kanji':
            while not parar:
                novokanji()
                if input() == 'parar':
                    parar = True
        elif resp == 'teste':

            print('0 ou 1')
            resp_lista = input()
            random.shuffle(kanji_lista_lista[int(resp_lista)])
            print('(escrita) (pronuncia) (significado)')
            resp = input()
            for questao in kanji_lista_lista[int(resp_lista)]:
                if parar:
                    break
                while 1:
                    if resp == 'escrita':
                        gabarito = questao.stg
                        dica = questao.stg
                    elif resp == 'pronuncia':
                        gabarito = questao.leitura
                        dica = questao.stg
                    elif resp == 'significado':
                        gabarito = questao.traducao
                        dica = questao.stg

                    print(dica)
                    questao_resp = input()
                    if type(gabarito) == type(str()):
                        if questao_resp == gabarito:
                            print('certo')
                            break
                        elif questao_resp == 'parar':
                            parar = True
                            break

                        elif questao_resp == 'dic':
                            questao.dic()
                            input()
                            continue

                        else:
                            print('errado')
                            continue
                    elif type(gabarito) == type(list()):
                        if questao_resp in gabarito:
                            print('certo')
                            break
                        else:
                            print('errado')
                            continue
                    #else:
                     #   print('errado')
                      #  continue
        elif resp == 'dicionario':
            dicionario()

                #questao = random.choice(kanji_lista)


if __name__ == '__main__':
    main()
