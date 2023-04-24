class Rectangle:
    def __init__(self):
        self.__longueur = 10
        self.__largeur = 5

    def get_value(self):
        print("La longueur est", self.__longueur,"\nLa largeur est", self.__largeur)
    
    def set_value(self,new_longueur,new_largeur):
        self.__longueur = new_longueur
        self.__largeur = new_largeur
        print("La nouvelle longueur est", self.__longueur,"\nLa nouvelle largeur est", self.__largeur)


rectangle = Rectangle()
rectangle.get_value()
rectangle.set_value(30,20)
