# Intervalle, nombre positif, nombre négatif
#   Cet programme permet de saisir un nombre puis déterminer s'il appartient à un intervlle donné


print(" Intervalous ".center(30, '•'))
print("• Ce programme te permet de  •\n• savoir si un nombre que tu •\n• auras saisi est dans un    •\n• intervalle ou pas !!       •")
print(''.center(30, '•'))

ordonnee = True
while ordonnee:
    try:
        firstValue = int(input("Tape la première valeur : "))
        secondValue = int(input("Tape la seconde valeur : "))
        ordonnee = firstValue > secondValue
        if ordonnee:
            print("La première valeur doit être la plus petite.")
        else:
            break
    except:
        print("Warning : taper uniquement des nombres entiers !")
        print("".center(30, '='))

print("• Taper une troisième valeur pour savoir s'il fait partie de l'intervalle prédéfini •")
while True:
    try:
        thirdValue = int(input("·.·.·. "))
        if thirdValue.isnumeric():
            if thirdValue in range(firstValue, secondValue+1):
                print("Votre valeur est bien dans notre intervalle")
                break
            else:
                print("Notre valeur n'est pas l'intervalle")
                break
        else:
            print("veuillez retaper la valeur.")

    except TypeError: 
        print("Please taper de vrai nombre cette fois-ci ·.·.")



