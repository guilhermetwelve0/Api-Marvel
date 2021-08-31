import hashlib #Biblioteca usada para realizar o algoritmo MD5
import time
import requests

#Chaves da API para aplicação
publica = "ee4138ab80d8f80fa4ca13ab3fa9e7aa"
particular = "57cfbc8ba352ea34da5d226390f7f5a34b7d00af"

#Construindo o MD5
m = hashlib.md5()
ts = str(time.time())

#Adicionando todas as parcelas da criptografia na forma de bytes
m.update(bytes(ts,'utf-8')) # o tempo atual
m.update(bytes(particular,'utf-8')) #A chave particular (private key)
m.update(bytes(publica,'utf-8')) # Adiciona a chave publica (public key)
hasht = m.hexdigest() # Cria o MD5

#Montando URL da requisição
base = "https://gateway.marvel.com" # Página base para todas as requisições
personagem = input("Digite o nome em inglês do personagem: \n") #Pede pro usuário digitar o nome
requisicao = "/v1/public/characters?name=" + personagem + "&orderBy=name&limit=1" #O que queremos da requisicao

#Juntando todas as partes da URL
URL = base + requisicao + "&ts" + ts + "&apikey" + publica + "&hash=" + hasht

#Fazendo a requisicão
dados = requests.get(URL).json() # Os dados são recebidos a partir da requisição

#Verifica se existe uma descrição dentro dos dados recebidos
try:
    descricao = dados["data"]["results"][0]["description"]
except:
    exit("Você digitou um personagem inválido") #Avisa ao usuário do erro e para o programa
print(descricao) #Apresentamos na tela esse resultado