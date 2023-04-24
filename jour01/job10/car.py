class Voiture:
    def __init__(self):
        self.__marque = "Suzuki"
        self.__model = "Swift"
        self.__annee = 2019
        self.__km = 37000
        self.__enmarche = False
        self.__reservoir = 50

#------------------------ Get ----------------------#
    def get_marque(self):
        return self.__marque

    def get_model(self):
        return self.__model
    
    def get_annee(self):
        return self.__annee
    
    def get_km(self):
        return self.__km

    def get_enmarche(self):
        return self.__enmarche

#------------------------ Set ----------------------#
    def set_marque(self, new_marque):
        self.__marque = new_marque

    def set_model(self, new_model):
        self.__model = new_model

    def set_annee(self, new_annee):
        self.__annee = new_annee

    def set_km(self, new_km):
        self.__km = new_km
    
    def set_enmarche(self, new_enmarche):
        self.__enmarche = new_enmarche

    def demarrer(self):
        if self.__verifier_plein() >= 5:
            self.__enmarche = True
        else:
            self.__enmarche = False

    def arreter(self):
        self.__enmarche = False

    def __verifier_plein(self):
        return self.__reservoir
    
voiture = Voiture()
print("Marque:", voiture.get_marque())
print("Model:", voiture.get_model())
print("Annee:", voiture.get_annee())
print("Kilometage:" , voiture.get_km())
print("En marche", voiture.get_enmarche())
voiture.demarrer()
print("En marche après le démarrage:", voiture.get_enmarche())
voiture.arreter()

print("---------------------")
voiture.set_marque("Renault")
print("Marque:", voiture.get_marque())
voiture.set_model("Clio")
print("Model:", voiture.get_model())
voiture.set_annee(1920)
print("Annee:", voiture.get_annee())
voiture.set_km(1222333)
print("Kilometage:" , voiture.get_km())
print("En marche", voiture.get_enmarche())
voiture.demarrer()
print("En marche après le démarrage:", voiture.get_enmarche())
