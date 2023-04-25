class Vehicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

#-----Get-----#
    def get_marque(self):
        return self.marque
    
    def get_model(self):
        return self.model
    
    def get_annee(self):
        return self.annee
    
    def get_prix(self):
        return self.prix

    def informationsVehicule(self):
        print("Marque:", self.get_marque())
        print("Modèle:", self.get_model())
        print("Année:", self.get_annee())
        print("Prix:", self.get_prix())

    def demarrer(self):
        return "Attention je roules"
    
class Voiture(Vehicule):
    def __init__(self, marque, model, annee, prix):
        super().__init__(marque, model, annee, prix)
        self.porte = 4

    def get_porte(self):
        return self.porte
    
    def demarrer(self):
        return "Attention je roules en Merco"
    
    def informationsVehicule(self):
        print("Marque:", self.get_marque())
        print("Modèle:", self.get_model())
        print("Année:", self.get_annee())
        print("Prix:", self.get_prix())
        print("Nombres de portes :", self.get_porte())


class Moto(Vehicule):
    def __init__(self, marque, model, annee, prix):
        super().__init__(marque, model, annee, prix)
        self.roue = 2

    def get_roue(self):
        return self.roue

    def informationsVehicule(self):
        print("Marque:", self.get_marque())
        print("Modèle:", self.get_model())
        print("Année:", self.get_annee())
        print("Prix:", self.get_prix())
        print("Nombres de roues :", self.get_roue())

    def demarrer(self):
        return "Attention je roules en 2 roues"

        
vehicule = Vehicule("Mercedes", "Classe A", "2020", 18500)
voiture = Voiture("Mercedes", "Classe A", "2020", 18500)
moto = Moto("Yamaha","1200 Vmax", "1987", 4500)

vehicule.informationsVehicule()
print("--------------------")
voiture.informationsVehicule()
print("--------------------")
moto.informationsVehicule()
print("--------------------")
print(vehicule.demarrer())
print(voiture.demarrer())
print(moto.demarrer())
