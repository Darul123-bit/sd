#   Système de reservation de billets de cinéma

'''
- Rèles:

• Le film est interdit au moins de 12 ans
• Le tarif normal est 5 000 francs
• POur les séances de matinée (avant 12h) le tarifs est 400 francs
• Les étudiants ont un réduction de 1500 francs
• séances après 20h offrent un siège prémium sans frais supplémentaires
normalement ce siège coûte 1000 de plus
'''

print(" Bienvenu(e) pour la reservation ".center(40, '•'))

restart = True

ticketPrice = 5000


while restart:
    try:
        age = int(input("• Veuillez entrer votre âge : "))
        estEtudiant = input("Êtes-vous étudiant ? O (oui) N (Non): ")
        estEtudiant = estEtudiant.lower()
        if estEtudiant == 'o':
            estEtudiant = True 
        else:
            estEtudiant = False

        heure = int(input("Heure de la séance choisie : "))
        restart = False

    except:
        print("Les informations entrer sont incorrectes")




if age < 12:
    print("• Vous n'êtes pas éligible. Désolé !!!")

else:
    if estEtudiant:
        ticketPrice -= 1500
        if heure < 12:
            ticketPrice -= 1000
            print(f"Votre ticket est à {ticketPrice}")
        elif heure >= 20:
         
            print("Vous avez un siège premium gratuit")
            print(f"votre ticket est à {ticketPrice}")
        else:
            print(f"Votre ticket est à {ticketPrice}")
    else:
        if heure < 12:
            ticketPrice -= 1000
            print(f"Votre ticket est à {ticketPrice}")
        elif heure >= 20:
            print("Vous avez obtenu un billet premium gratuitement.")
            print(f"Votre ticket est à {ticketPrice}")

        else:
            print(f"Votre ticket est à {ticketPrice}")