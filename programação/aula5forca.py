#escolhe aleatoriamente uma palavra do arquivo palavras.txt 
import random

#abre arquivo para leitura
arquivoEntrada = open("palavras.txt","r")

#Coloca todas as linhas em memória
palavras = arquivoEntrada.readline()

# Fecha o arquivo
arquivoEntrada.close()

palavraEscolhida = palavras[
    random.randint(0, len(palavras) -1)].upper().strip()