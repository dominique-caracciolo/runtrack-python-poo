import math
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
    
    
class Cercle(Forme):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def aire(self):
        return (self.radius **2)* math.pi
    

    
forme = Forme()
rectangle = Rectangle(10,5)
cercle = Cercle(6)

print("aire du cercle:", cercle.aire())
print("aire du rectangle",rectangle.aire())

