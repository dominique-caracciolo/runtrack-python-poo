class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self):
        print("Je suis", self.prenom , self.nom)

personne = Personne("Dominique", "Caracciolo")
personne1 = Personne("John", "Doe")

personne.SePresenter()
personne1.SePresenter()
