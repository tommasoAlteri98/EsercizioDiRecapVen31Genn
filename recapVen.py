import random

nomeUtente = input("Inserisci il tuo nome")
print("Ciao " + nomeUtente + ", benvenuto nel gioco Pari o Dispari vs CPU")
vittorie = 0
sconfitte = 0

while True :
    pariOdispari = input("Scegli pari o scegli dispari?").lower()
    if pariOdispari != "pari" or pariOdispari !="dispari" :
        print
