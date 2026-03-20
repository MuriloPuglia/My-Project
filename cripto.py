from cryptography.fernet import Fernet
import subprocess
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

pergunta1 = int(input("""[1] para criptografar um arquivo:
[2] para descriptografar um arquivo: """))


while pergunta1 != 1 and pergunta1 != 2:
    subprocess.run("clear")
    pergunta1 = int(input("Por favor, inserir 1 para criptografia ou 2 para descriptografia: "))
    subprocess.run("clear")
    

if pergunta1 == 1:
   
    subprocess.run("clear")
    pergunta2 = int(input("""[1] criptografar o mesmo arquivo
[2] criar um novo arquivo com o conteudo criptografado (recomendado)
""" ))
    
    while pergunta2 != 1 and pergunta2 != 2:
        subprocess.run("clear")
        pergunta2 = int(input("""Por favor, inserir:
[1] criptografar o mesmo arquivo
[2] criar um arquivo novo com o conteudo criptografado (recomendado)
""" ))
        subprocess.run("clear")

    subprocess.run("clear")

    if pergunta2 == 2:
        #1 criar uma chave simetrica
        key = Fernet.generate_key()
        f = Fernet(key)

        #2 perguntar ao usuario qual arquivo ele gostaria de criptografar.
        question = input("Qual arquivo voce gostaria de criptografar? (Por favor inserir o path inteiro) ")
        
        result = subprocess.run(
                    ["find", question],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
        )
    
        codigo = result.returncode
    
        while codigo != 0:
            subprocess.run("clear")
            print("Path nao encontrado.")
            question = input("Qual arquivo voce gostaria de criptografar? (Por favor inserir o path inteiro) ")
            result = subprocess.run(
                    ["find", question],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
            )

            codigo = result.returncode

        subprocess.run("clear")    

        #3 lendo o conteudo do arquivo com subprocess (bem mais facil que o os)
        mensagem = subprocess.getoutput(f"cat {question}")
        binario = mensagem.encode("utf-8")

        #4 criptografando a mensagem
        token = f.encrypt(binario)

        #deixar o nome do arquivo novo mais bonito
        splited = question.split('/')
        name = splited[-1]

        #guardar a mensagem criptografada em outro arquivo
        with open(f"{question}.cripto", "wb") as sla:
            file = sla.write(token)

        print(f"Arquivo sendo criptografado...")
        time.sleep(4)
        print("Arquivo criptografado com sucesso.")
        print(" ")
        print(f"Nome do arquivo: {name}.cripto")
        time.sleep(3)
        subprocess.run("clear")

    elif pergunta2 == 1:
        #1 criar a chave simetrica
        key = Fernet.generate_key()
        f = Fernet(key)
        
        #2 perguntar ao usuario qual arquivo ele gostaria de criptografar.
        question = input("Qual arquivo voce gostaria de criptografar? (Por favor inserir o path inteiro) ")
        
        result = subprocess.run(
                ["find", question],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)

        codigo = result.returncode

        while codigo != 0:
            subprocess.run("clear")
            print("Path nao encontrado.")
            question = input("Qual arquivo voce gostaria de criptografar? (Por favor inserir o path inteiro) ")
            result = subprocess.run(
                    ["find", question ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
            )
            codigo = result.returncode
            
        subprocess.run("clear")

        #3 lendo o conteudo do arquivo com subprocess (bem mais facil que o os)
        mensagem = subprocess.getoutput(f"cat {question}")
        binario = mensagem.encode("utf-8")

        #4 criptografando a mensagem
        token = f.encrypt(binario)

        #5 substituindo a mensagem original com a criptografada
        with open(question, "wb") as file:
            subs = file.write(token)

        #6 mudando o nome do arquivo
        subprocess.run(["mv", f"{question}", f"{question}.cripto"])

        print(" ")
        print("Substituindo conteudo...")
        time.sleep(3)
        print("Substituicao concluida com sucesso.")
        subprocess.run("clear")   

    pergunta3 = input("Voce deseja usar Criptografia Assimétrica parar proteger a chave simétrica? [Y/N] " ).upper()

    while pergunta3 != "Y" and pergunta3 != "N":
        subprocess.run("clear")
        pergunta3 = input("""Por favor, inserir:
[Y] usar Criptografia Assimétrica parar proteger a chave simétrica. 
[N] nao usar Criptografia Assimétrica parar proteger a chave simétrica

                          """).upper()

    if pergunta3 == "Y":
        subprocess.run("clear")

        #gerando par de chaves
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        print("Gerando protecao da chave...")
        time.sleep(3)

        simetrica_cripto = public_key.encrypt(
            key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open("chave_simetrica.enc", "wb") as f:
            f.write(simetrica_cripto)

        divisao = question.split("/")
        divisao = divisao[:-1]
        s2 = "/".join(divisao)
        subprocess.run(["mv", "chave_simetrica.enc", s2])
        
        print(f"Concluido. Chave simetrica criptografada encontrada em {s2}...")
        time.sleep(3)
        subprocess.run("clear")
       
        private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

        #armazenando a chave privada
        with open("chave_privada", "wb") as chp:
            chp.write(private_bytes)
        
        subprocess.run(["chmod", "400", "chave_privada"])

        divisao2 = question.split("/")
        divisao2 = divisao2[:-1]
        s3 = "/".join(divisao2)
        subprocess.run(["mv", "chave_privada", s3])
        subprocess.run("clear")
    
        print(f"Arquivos criados: 'chave_privada' | 'chave_simetrica.enc' | '{name}.cripto'")

    elif pergunta3 == "N":
        # guardando a chave simetrica
            with open("chave_simetrica", "wb") as cs:
                chave = cs.write(key)
            divisao = question.split("/")
            divisao = divisao[:-1]
            s2 = "/".join(divisao)
            subprocess.run(["mv", "chave_simetrica", s2])
            subprocess.run("clear")
            print(f"Arquivos criados: 'chave_simetrica | '{name}.cripto'")
elif pergunta1 == 2:

    subprocess.run("clear")
    path = input("Qual arquivo voce gostaria de descriptografar? (por favor inserir o path inteiro) ")

    result = subprocess.run(
                        ["find", path],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
            )
   
    codigo = result.returncode
  
    while codigo != 0:
        subprocess.run("clear")
        print("Path nao encontrado.")
        path = input("Qual arquivo voce gostaria de descriptografar? (Por favor inserir o path inteiro) ")
        result = subprocess.run(
                ["find", path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
        )
  
        codigo = result.returncode
    
        subprocess.run("clear")

    decisao = input("A chave simetrica desse arquivo foi criptografada? [Y/N] ").upper()

    while decisao != "Y" and decisao != "N":
            subprocess.run("clear")
            decisao = input("""Por favor, inserir:
    [Y] se a chave simetrica foi criptografada 
    [N] se a chave simetrica NAO foi criptograda
   
                            """).upper()

    subprocess.run("clear")
    if decisao == "Y":
        subprocess.run("clear")
        chave = input("Qual o arquivo da chave simétrica criptografada? (por favor inserir o path inteiro) ")

        result = subprocess.run(
                      ["find", chave],
                      stdout=subprocess.DEVNULL,
                      stderr=subprocess.DEVNULL
        )
  
        codigo = result.returncode
  
        while codigo != 0:
            subprocess.run("clear")
            print("Path nao encontrado.")
            chave = input("Qual o arquivo da chave simétrica criptografada? (por favor inserir o path inteiro) ")
            result = subprocess.run(
                    ["find", chave],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
            )
  
            codigo = result.returncode

        subprocess.run("clear")
        
        privada = input("Qual o arquivo da chave privada? (por favor inserir o path inteiro) ")

        result = subprocess.run(
                      ["find", privada],
                      stdout=subprocess.DEVNULL,
                      stderr=subprocess.DEVNULL
         )
  
        codigo = result.returncode
  
        while codigo != 0:
            subprocess.run("clear")
            print("Path nao encontrado.")
            privada = input("Qual o arquivo da chave privada? (por favor inserir o path inteiro) ")
            result = subprocess.run(
                    ["find", privada],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
            )
  
            codigo = result.returncode
  
            subprocess.run("clear")

        with open(chave, "rb") as j:
            chave2 = j.read()

        with open(privada, "rb") as pv:
            privada2 = serialization.load_pem_private_key(
            pv.read(),
            password=None  # ou senha.encode() se estiver protegida
        )

        sym_key = privada2.decrypt(
                chave2,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
        )
        
        subprocess.run("clear")

        with open(path, "rb") as pt:
            ciphertext = pt.read()

        cipher = Fernet(sym_key)
        final = cipher.decrypt(ciphertext)

        subprocess.run("clear")
        print(f"""Chave simetrica criptografada: 
            {chave2}""")
        time.sleep(4)
        subprocess.run("clear")
        print(f"""Chave simetrica descriptografada:
            {sym_key}""")
        time.sleep(4)
        subprocess.run("clear")
        print(f"""Conteudo criptografado: 
            {ciphertext}""")
        time.sleep(4)
        subprocess.run("clear")
        print(f"""Conteudo descriptografado: 
            {final}""")

    elif decisao == "N":

        chave = input("Qual o arquivo da chave simétrica? (por favor inserir o path inteiro) ")

        result = subprocess.run(
                        ["find", chave],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
          )
  
        codigo = result.returncode
  
        while codigo != 0:
            subprocess.run("clear")
            print("Path nao encontrado.")
            chave = input("Qual o arquivo da chave simétrica? (por favor inserir o path inteiro) ")
            result = subprocess.run(
                    ["find", chave],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
            )
  
            codigo = result.returncode
  
            subprocess.run("clear")


        subprocess.run("clear")
        with open(path, "rb") as p:
            ciphertext = p.read()

        with open(chave, "rb") as c:
            key = c.read()

        cipher = Fernet(key)
        plaintext = cipher.decrypt(ciphertext)
        
        print(f"Conteudo criptografado: {ciphertext}")
        print("")
        print(f"Conteudo original: {plaintext}")


