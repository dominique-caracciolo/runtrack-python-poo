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
        return self.longueur * self.largeur
    
forme = Forme()
rectangle = Rectangle(10,5)

print(rectangle.aire())
