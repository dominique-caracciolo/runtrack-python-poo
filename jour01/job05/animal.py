class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
    
    def show_age(self):
        self.age = int(input("Entrez l'age de l'animal: "))
        print("L'animal a", self.age, "ans")

    def viellir(self):
        self.age +=1 
        print("L'animal a", self.age, "ans")

    def nommer(self, nom):
        self.nom = nom
        print("L'animal se nomme" , self.nom)

animal = Animal()
animal.show_age()
animal.viellir()
animal.nommer("Pascale")
