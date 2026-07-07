# Expressions booléennes et conditions

print(" Attraction ".center(20, '*'))
while True:
    try:
        age = int(input("Entrer votre âge : "))

        break
    except:
        print("Veuillez entrer un nombre merci !")


estEligible = False
peutMonter = 'no'

if 10 < age <= 60:
    estEligible = True
    peutMonter = 'Yes'