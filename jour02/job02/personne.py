class Personne:
    def __init__(self):
        self.age = 14

    def AfficherAge(self):
        print(self.age)
    
    def bonjour(self):
        return "Hello"

    def ModifierAge(self, new_age):
        try:
            self.age = int(new_age)
        except ValueError:
            print("L'âge doit être un nombre entier.")

class Eleve(Personne):
    def __init__(self):
        super().__init__()

    def allerEnCours(self):
        return "je vais en cours"

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
        return "le cours va commencer"


personne= Personne()
eleve = Eleve()
professeur = Professeur()

print(eleve.bonjour(),",", eleve.allerEnCours())
eleve.ModifierAge(15)

professeur.ModifierAge(40)
print("Le nouvelle age du prof:", professeur.age)
print(professeur.bonjour(), "," ,professeur.enseigner())
#print(eleve.age)

#eleve.AfficherAge()

# professeur.set_matiereEns("mathématiques")
# print(professeur.enseigner())