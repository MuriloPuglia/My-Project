import subprocess
from cryptography.fernet import Fernet
import time


#1 Conteudo
print("Modelo de resposta: /home/user/teste.dir")
print("")
conteudo = input("Qual arquivo/diretorio voce gostaria de copiar? ")

divisao = conteudo.split('/')
divisao = divisao[1:-1]

print(divisao)


#2 Fazer a copia em um diretorio de backup
subprocess.run(["mkdir", "-p", f"{conteudo}.bkp"]) 
subprocess.run(["cp", "-avr", conteudo, f"{conteudo}.bkp/"])

subprocess.run("clear")

#3 Destino
print("Modelo de resposta: usuario@servidor:/destino/")
print("")
destino = input(f"Para onde voce gostaria de mandar a copia de {conteudo}:  ")



print("Iniciando backup...")
time.sleep(3)

subprocess.run(["rsync", "-avz", f"{conteudo}.bkp", destino])





    
