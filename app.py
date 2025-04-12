while True:
    try:
        score_equipe = int(input("Saisis le score de ton équipe : "))
        break
    except ValueError:
        print("Merci de renseigner un nombre valide pour le score de ton équipe.")

while True:
    try:
        score_adversaire = int(input("Saisis le score de l'équipe adverse : "))
        break
    except ValueError:
        print("Merci de renseigner un nombre valide pour le score de l'équipe adverse.")


if score_equipe > score_adversaire:
    print("Bravo beau gosse, t'es trop fort !")
else:
    print("[texte à remplacer]")

     
#print("Le score exact était donc de", score_equipe, "pour toi et de", score_adversaire, "pour tes adversaires")