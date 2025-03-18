import hashlib

# Função para hash da senha
def hash_password(data):
    return hashlib.md5(data.encode()).hexdigest()

# Função para transformar dados em um novo hash
if __name__ == "__main__":
    username = input("Digite o nome do usuário: ")
    password = input("Digite a senha: ")

    hashed_password = hash_password(password)

    with open("output.txt", "w") as file:
        file.write(f"{username}\n")
        file.write(f"{hashed_password}\n")

    print("Dados salvos em output.txt")
