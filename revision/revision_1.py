# Exercice 1

#   Listes comme structures de données et dictionnaires comme structure de données

estValide = True

try:
    while estValide:
        chaine = input("Veuillez entrer la chaine à analyser : ")
        estValide = chaine.isalpha
        chaine = chaine.lower()
        chaine = "".join(chaine.split())
        
        if estValide:
            print(chaine.count('a'))
            print(chaine)
            break
        
        estValide = True
except:
    print("Veuillez taper uniquement une chaine de caractère sans caractères spéciaux ni espace")  





