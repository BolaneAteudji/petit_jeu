import random

class Jeu:
    def __init__(self, m):
        self.k = random.randint(0, m)
        print(f"Un nombre entre 0 et {m} a été choisi.")  # Choisit un nombre aléatoire

    def test(self, nombre):
        if nombre > self.k:
            return "Trop grand !"  # Si le nombre est plus grand que le nombre à deviner
        elif nombre < self.k:
            return "Trop petit !"  # Si le nombre est plus petit que le nombre à deviner
        else:
            return "Bravo, tu as gagné !"  # Si le nombre est correct

    def jouer(self):
        while True:
            try:
                k = int(input("Entre un nombre : "))  # Demande à l'utilisateur de deviner un nombre
                resultat = self.test(k)  # Compare le nombre donné (k) avec le nombre à deviner (self.k)
                print(resultat)
                if resultat == "Bravo, tu as gagné !":
                    break  # Si le joueur a trouvé la bonne réponse, on arrête la boucle
            except ValueError:
                print("Ceci n'est pas un entier, réessayez.")  # Gestion des erreurs si l'utilisateur entre autre chose qu'un nombre

    def jouer_avec_limite(self, essais_max):
        essais = 0
        while essais < essais_max:
            try:
                k = int(input(f"Essai {essais + 1}/{essais_max} - Entre un nombre : "))
                resultat = self.test(k)  # Compare le nombre donné avec le nombre à deviner
                print(resultat)
                if resultat == "Bravo, tu as gagné !":
                    break
                essais += 1
            except ValueError:
                print("Ceci n'est pas un entier, réessayez.")  # Gestion des erreurs
        
        if essais == essais_max:
            print(f"Désolé, vous avez épuisé vos {essais_max} essais.")  # Si le joueur n'a pas trouvé après le nombre maximum d'essais

if __name__ == '__main__':
    m = 10  # Nombre maximum que l'ordinateur peut choisir
    essais_max = 5  # Nombre maximum d'essais
    jeu = Jeu(m)  # Crée un jeu avec un nombre maximum de 10
    jeu.jouer_avec_limite(essais_max)  # Lance le jeu avec un nombre maximum de 5 essais
