class Forme:
    def __init__(self):
        pass 

    def aire(self):
        return 0

        

class Rectangle(Forme):
    def __init__(self,longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return 6
    
forme = Forme()
rectangle = Rectangle(34,12)

print(rectangle.aire())
