#import
from colorama import Fore, Style

import os



#Creo un array di utenti
users = [
    {
        "name": "Lorenzo",
        "surname": "Moccia",
        "email": "moccialorenzo98@gmail.com",
        "username": "xcholito",
        "password": "marco12",
        "saldo" : 50,
    },
    {
        "name": "Lorenzo",
        "surname": "Moccia",
        "email": "moccialorenzo98@gmail.com",
        "username": "padrepio",
        "password": "marco12",
        "saldo" : 50,
    },
    {
        "name": "Lorenzo",
        "surname": "Moccia",
        "email": "moccialorenzo98@gmail.com",
        "username": "giuseppedibitonto",
        "password": "marco12",
        "saldo" : 50,
    },
    {
        "name": "Lorenzo",
        "surname": "Moccia",
        "email": "moccialorenzo98@gmail.com",
        "username": "mariadefilippi",
        "password": "marco12",
        "saldo" : 10000,
    },
]



#Flag
logged_in = False

#Ciclo affinchè logged_in non è True
while not logged_in:
    # Prendo gli input dall'utente
    username = input("Inserisci nome utente: ")
    password = input("Inserisci la password: ")

    for user in users:
        if username == user["username"] and password == user["password"]:

            # clear console
            os.system('cls' if os.name == 'nt' else 'clear')

            print(Fore.LIGHTGREEN_EX + "Accesso effettuato come:", username + Style.RESET_ALL)
            logged_in = True
            break  # esce dal ciclo for

    if not logged_in:
        # viene eseguito solo se il ciclo for non viene interrotto da break
        print("Credenziali errate! Riprova.")

#Funzioni
def printSaldo():
    #Cast da integer a string
    saldoString = str(user["saldo"])
    print(saldoString + "€")

def printEmail():
    print(user["email"])

def printMenu():
    print(Fore.RED + "[USAGE]: -saldo, -email, -exit" + Style.RESET_ALL)


#Ciclo che richiede all'utente di inserire una funzione.
while True:
    printMenu()
    option = input("Inserisci option desiderata:")

    if option == "-exit":
        break
    elif option == "-saldo":
        printSaldo()
    elif option == "-email":
        printEmail()
    else:
        print("Opzione non valida")
