import random
import string

def Generar_contraseña(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("De que longitud deseas la contraseña: "))
        if length <= 0:
            print("La longitud de la contraseña debe ser entero positivo")
            return
        password = Generar_contraseña(length)
        print("Contraseña Creada:", password)
    except ValueError:
        print("NUMERO INVALIDO. Por favor intruduzca un numero valido")

if __name__ == "__main__":
    main()




