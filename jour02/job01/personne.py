class Personne:
    def __init__(self):
        self.age = 14

    def AfficherAge(self):
        print(self.age)
    
    def bonjour(self):
        return "Hello"

    def ModifierAge(self,new_age):
        self.age = new_age
        new_age is int

class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        return "Je vais en cours"

    def AffichageAge(self):
        print("J'ai ",self.age, "ans") 





class Professeur(Personne):
    def __init__(self):
        super().__init__()
        self.__matiereEnseigner = ""

    def get_matiereEns(self):
        self.__matiereEnseigner

    def set_matiereEns(self,new_matiere):
        self.__matiereEnseigner = new_matiere

    def enseigner(self):
        return "Le cours va commencer"


personne= Personne()
eleve = Eleve()
professeur = Professeur()

eleve.AfficherAge()

# professeur.set_matiereEns("mathématiques")
# print(professeur.enseigner())