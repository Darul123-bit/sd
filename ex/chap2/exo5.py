#   Ecrivons un programme qui permet de calculer le montant des heures supplémentaires d'un employé

'''
Voici-ci le barème:
•   Les 39 premières heures sans supplément.
•   De la 40e à la 44e heure sont mojorées de 50 %
•   De la 45e à la 49e sont majorées de 75 %
•   De la 50e heure ou plus sont majorées de 100 %
'''

#   Affichage de début de programme

print(" Bienvenu(e) pour évaluer votre prime ".center(46, '•'))

#   Un peu d'espace ici hihihi
print("\n".center(20, '•'))

heure = int(input("• Entrer votre heure total de travail : "))
salaire = int(input("• Entrer votre salaire : "))


if 0 < heure <= 39:
    print("• Vous n'avez aucune prime sorry !!!")
    print(f"• Votre salaire est donc {salaire} F CFA")
elif 40 <= heure <= 44:
    salaire += 0.5
    print("• Vous avez une majoration de 50 %")
    print(f"• Votre salaire est donc {salaire}")
elif 45 <= heure <= 49:
    salaire += 0.75
    print("• Vous avez une majoration de 75 %")
    print(f"• Votre salaire final est donc de {salaire}")
elif heure >= 50:
    salaire *= 2
    print(f"• Félicitations vous avez le Jackpot\• Vous avez une majoration de 100 %")
    print(f"• Votre salaire est {salaire}")
else:
    print("\n")
    print("• ERROR •"*4)
    print("\n")
    print("• Tell me which kind of people are you ???\n• Just tell me \U0001F612.")
    
